import psycopg2
import pandas as pd
from typing import List
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

class DataSqlIntegration(ABC):
      """
      Abstract base class for bank marketing data SQL integration operations.

      This class defines the interface for loading bank marketing data into a SQL database
      and querying results. Concrete implementations must provide the actual database
      interaction logic.

      Attributes:
            dataPath (str): Path to the data file to be processed
      """

      def __init__(self, dataPath: str) -> None:
            """
            Initialize the data integration handler.
            
            Args:
            dataPath: Path to the bank marketing data file
            """
            self.dataPath = dataPath

      @abstractmethod
      def createTable(self, connection: psycopg2.connect) -> None:
            """
            Create the bank_marketing table in the database.
            
            Args:
            connection: Active PostgreSQL database connection
            
            Raises:
            psycopg2.Error: If table creation fails
            """
            pass

      @abstractmethod
      def answerQueryAnswer(self, connection:psycopg2.connect, queryString: str, index: List[str]) -> pd.DataFrame:
            """
            Convert SQL query results into a pandas DataFrame.
            
            Args:
            queryRows: List of tuples from SQL query results
            index: List of index values for the DataFrame
            
            Returns:
            pd.DataFrame: Formatted DataFrame from query results
            """
            pass

      @abstractmethod
      def insertRecordsIntoTable(self, connection: psycopg2.connect) -> None:
            """
            Insert records from the data file into the database table.

            Args:
            connection: Active PostgreSQL database connection

            Raises:
            psycopg2.Error: If data insertion fails
            """
            pass


class BankDataSqlIntegration(DataSqlIntegration):
      """
      Concrete implementation of bank marketing data SQL integration.
      
      Provides PostgreSQL-specific implementation for loading bank marketing campaign data
      and converting query results to pandas DataFrames.
      """
      
      def createTable(self, connection: psycopg2.connect) -> None:
            """
            Create the bank_marketing table with proper schema if it doesn't exist.
                        plt.clf()

            The table includes columns for all bank marketing campaign attributes with
            appropriate data types and constraints.
            
            Args:
            connection: Active PostgreSQL database connection
            
            Raises:
            psycopg2.Error: If table creation fails
            """
            cursor = connection.cursor()
            try:
                  cursor.execute("""
                  CREATE TABLE IF NOT EXISTS bank_marketing (
                        age INTEGER NOT NULL,
                        job VARCHAR(50) NOT NULL,
                        marital VARCHAR(20) NOT NULL,
                        education VARCHAR(50) NOT NULL,
                        has_default VARCHAR(10) NOT NULL,
                        balance INTEGER NOT NULL,
                        housing VARCHAR(10) NOT NULL,
                        loan VARCHAR(10) NOT NULL,
                        contact VARCHAR(20) NOT NULL,
                        day INTEGER NOT NULL,
                        month VARCHAR(10) NOT NULL,
                        duration INTEGER NOT NULL,
                        campaign INTEGER NOT NULL,
                        pdays INTEGER NOT NULL,
                        previous INTEGER NOT NULL,
                        poutcome VARCHAR(20) NOT NULL,
                        y VARCHAR(10) NOT NULL
                  );
            """)
                  connection.commit()
            except psycopg2.Error as e:
                  connection.rollback()
                  raise e
      
      def answerQueryAnswer(self, connection: psycopg2.connect, queryString: str, index: List[str]) -> pd.DataFrame:
            """
            Execute SQL query and convert results to a properly formatted pandas DataFrame.
            
            Args:
                  connection: Active PostgreSQL database connection
            queryString: SQL query to execute
            index: List of index values for the DataFrame
            
      Returns:
            pd.DataFrame: Formatted DataFrame with query results
            
      Example:
            >>> df = answerQueryAnswer(conn, "SELECT age, balance FROM bank_marketing", ['row1', 'row2'])
      """
            cursor = connection.cursor()
            try:
                  cursor.execute(queryString)
                  queryRows = cursor.fetchall()
                  
                  # Debug: Print raw query results
                  print(f"Query returned {len(queryRows)} rows")
                  if queryRows:
                        print("First row sample:", queryRows[0])
                  
                  # Create DataFrame with proper column handling
                  if not queryRows:
                        return pd.DataFrame(index=index)
                        
                  # Convert to DataFrame with column names
                  df = pd.DataFrame.from_records(
                        queryRows,
                        columns=[desc[0] for desc in cursor.description],
                        index=index[:len(queryRows)]  # Ensure index matches row count
                  )
                  return df
                  
            except psycopg2.Error as e:
                  print(f"Database error: {e}")
                  return pd.DataFrame()
            finally:
                  cursor.close()

      def insertRecordsIntoTable(self, connection: psycopg2.connect, alreadyAdded: bool) -> None:
            """
            Efficiently bulk load records from CSV into the database using COPY.
            
            Handles the data file with proper CSV formatting and error handling.
            
            Args:
                  connection: Active PostgreSQL database connection
                  alreadyAdded: boolean value to indicate if values are loaded before
            
            Raises:
                  psycopg2.Error: If data insertion fails
                  IOError: If data file cannot be read
            """
            if not alreadyAdded:
                  cursor = connection.cursor()
                  try:
                        with open(self.dataPath, 'r') as f:
                              next(f)
                              cursor.copy_expert("""
                              COPY bank_marketing FROM STDIN 
                              WITH (
                              FORMAT CSV,
                              DELIMITER ',',
                              NULL 'NULL',
                              QUOTE '"',
                              ESCAPE '\\'
                              )
                              """, f)
                        connection.commit()
                  except (psycopg2.Error, IOError) as e:
                        connection.rollback()
                        raise e


      def plotConversionRates(self, resultsDf: pd.DataFrame, yColumns: list) -> plt.Figure:
            """
            Display conversion rate analysis for single or multiple segment columns.

            Args:
                  resultsDf: DataFrame containing:
                        - segment columns (specified in yColumns)
                        - responseCount
                        - totalResponseCount  
                        - conversion_rate_percentage
                  yColumns: List of column names to group by (e.g., ['job', 'education'])

            Returns:
                  matplotlib.pyplot.Figure: Professional visualization of conversion rates

            Example:
                  plotConversionRates(df, yColumns=['job'])  # Single segment
                  plotConversionRates(df, yColumns=['job', 'marital'])  # Multi-segment
            """
            # Create composite key if multiple columns
            if len(yColumns) > 1:
                  resultsDf['compositeSegment'] = resultsDf[yColumns].apply(
                        lambda row: ' | '.join(row.values.astype(str)), axis=1)
                  yVar = 'compositeSegment'
            else:
                  yVar = yColumns[0]

            # Sort and filter top performers
            resultsDf = resultsDf.sort_values('conversion_rate_percentage', ascending=True)

            # Normalize values for colormap (must be between 0 and 1)
            conv_rates = pd.to_numeric(resultsDf['conversion_rate_percentage'], errors='coerce')
            normed_colors = (conv_rates / 100).fillna(0).clip(0, 1).to_numpy()
            colors = plt.cm.viridis(normed_colors)

            # Create plot
            fig, ax = plt.subplots(figsize=(10, max(6, len(resultsDf) * 0.4)))
            bars = ax.barh(
                  resultsDf[yVar],
                  resultsDf['conversion_rate_percentage'],
                  color=colors,
                  edgecolor='black'
            )

            # Customize plot
            title = 'Conversion Rates by ' + ' + '.join(yColumns)
            ax.set_title(title, fontsize=14, pad=20)
            ax.set_xlabel('Conversion Rate (%)', fontsize=12)
            ax.set_ylabel(' | '.join(yColumns), fontsize=12)
            ax.grid(axis='x', linestyle='--', alpha=0.7)

            # Add value labels and performance tiers
            for p in bars:
                  width = p.get_width()
                  ax.text(width + 0.5, p.get_y() + p.get_height() / 2.,
                        f'{width:.1f}%',
                        ha='left', va='center', fontsize=10)

                  # Add performance tier indicators
                  if width > 30:
                        ax.text(3, p.get_y() + p.get_height() / 2., '★',
                              ha='left', va='center', color='gold', fontsize=14)

            plt.tight_layout()
            return fig
