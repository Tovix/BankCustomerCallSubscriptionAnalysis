import pandas as pd
import seaborn as sns
from typing import Dict
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

class BaseEDAAnalyzer(ABC):
    """Abstract base class defining the complete interface for exploratory data analysis (EDA).
    
    This abstract class serves as a contract that enforces consistent implementation of core EDA operations
    across all concrete analyzer classes. It guarantees that all child classes will provide these fundamental
    analytical capabilities regardless of their specific domain implementation.
    
    The class maintains a strict 1:1 correspondence with the existing EDADataAnalyzer method signatures,
    ensuring seamless integration while providing more detailed documentation standards.
    """

    @abstractmethod
    def __init__(self, data: pd.DataFrame) -> None:
        """Initializes the EDA analyzer with the dataset to be analyzed.
        
        Args:
            data: The pandas DataFrame containing the raw dataset for analysis. Expected to contain
                both numeric and categorical columns. The DataFrame should be in tidy format where:
                - Each row represents an observation
                - Each column represents a variable
        Note:
            Concrete implementations should store the input data as an instance variable and initialize
            any necessary dictionaries for storing analysis results and conclusions.
        """
        pass

    @abstractmethod
    def categorizeDataColumnsTypes(self) -> None:
        """Performs column type classification for the entire dataset.
        
        Analyzes each column in the DataFrame and categorizes it as either:
        - 'numeric' for continuous/discrete numerical data (int, float)
        - 'categorical' for nominal/ordinal data (object, category, bool)
        
        The classification results should be stored in an instance variable dictionary (dataColsType)
        with column names as keys and type strings as values.
        
        Side Effects:
            - Prints the lists of numeric and categorical columns to stdout
            - Modifies the instance's dataColsType dictionary
        """
        pass

    @abstractmethod
    def generateDescriptiveStatistics(self) -> None:
        """Generates comprehensive descriptive statistics and visualizations.
        
        For all columns in the dataset (both numeric and categorical), this method:
        1. Calculates and prints standard descriptive statistics including:
        - Count, mean, std, min/max, quartiles for numeric columns
        - Count, unique, top, frequency for categorical columns
        2. Generates histogram visualizations for all numeric columns using:
        - 50 bins per histogram
        - Black edge colors on bars
        - Automatic subplot layout
        - Figure size of 12x8 inches
        3. Generates bar visualizations for all categorical columns using:
        - Automatic subplot layout
        - Figure size of 12x8 inches
        
        Note:
            The histograms are displayed using matplotlib's show() function and are not returned.
            Statistics are printed directly to stdout.
        """
        pass
    
    

    @abstractmethod
    def generateCorrelationMatrix(self) -> pd.DataFrame:
        """Computes and visualizes pairwise correlations between numeric features.
        
        Performs the following analytical operations:
        1. Automatically converts boolean 'y' column to integers (1/0) if present
        2. Calculates Pearson correlation coefficients between all numeric columns
        3. Displays an annotated heatmap visualization with:
        - Coolwarm color palette (-1 to +1 scale)
        - Numeric values displayed in each cell
        - Black grid lines between cells
        - Color bar showing correlation strength
        - 45-degree rotated x-axis labels
        4. Returns the computed correlation matrix
        
        Returns:
            A pandas DataFrame containing the correlation coefficients with:
            - Index and columns matching the numeric column names
            - Values ranging from -1.0 to +1.0
            - Diagonal values always equal to 1.0
            
        Visualization Features:
            - Title: "BANK DATA CORRELATIONS" in bold
            - Value annotations with 1 decimal place
            - Square aspect ratio for all cells
        """
        pass

    @abstractmethod
    def addConclusion(self, key: str, conclusion: str) -> None:
        """Stores analytical conclusions derived during the EDA process.
        
        Provides a standardized way to capture and organize insights discovered during analysis.
        The conclusions are stored in an internal dictionary for later reporting.
        
        Args:
            key: A unique string identifier for the conclusion (e.g., "balance_outliers")
            conclusion: The textual description of the finding (e.g., "Found 12 extreme balance values")
            
        Storage:
            Conclusions are maintained in an instance variable dictionary (generalConclusions)
            where keys are the provided identifiers and values are the conclusion texts.
            
        Note:
            This method does not perform any validation on the conclusions, simply stores them.
        """
        pass


class BankEdaDataAnalyzer(BaseEDAAnalyzer):
    """Concrete implementation performing EDA on banking/financial datasets.
    
    Inherits from BaseEDAAnalyzer and implements all required abstract methods.
    """

    def __init__(self, data: pd.DataFrame) -> None:
        """Initialize with banking dataset.
        
        Args:
            data: Banking data containing features like 'balance', 'duration', etc.
        """
        self.data = data
        self.questions: Dict[str, str] = {}
        self.generalConclusions: Dict[str, str] = {}
        self.dataColsType: Dict[str, str] = {}

    def categorizeDataColumnsTypes(self) -> None:
        """Classify columns as numeric or categorical.
        
        Stores classification in dataColsType and prints results.
        """
        for column in self.data.columns:
            if column in self.data.select_dtypes(include='number').columns:
                self.dataColsType[column] = 'numeric'
            else:
                self.dataColsType[column] = 'categorical'
        print("Column {} is {}".format(
            [col for col, colType in self.dataColsType.items() if colType == 'numeric'], 
            'numeric'))
        print("Column {} is {}".format(
            [col for col, colType in self.dataColsType.items() if colType == 'categorical'], 
            'categorical'))

    def generateDescriptiveStatistics(self) -> None:
        """Calculate and display descriptive statistics.
        
        Shows statistics for all columns and visualizes numeric distributions.
        """
        columns = [col for col, colType in self.dataColsType.items() 
        if colType == 'numeric' or colType == 'categorical']
        for column in columns:
            print(self.data[column].describe())
        self.data.select_dtypes(include='number').plot(
            kind='hist',
            subplots=True,
            bins=50,
            figsize=(12, 8),
            layout=(-1, 3),
            edgecolor='black',
            grid=False,
            density=True  
        )
        plt.figure(figsize=(12, 8))
        cat_cols = self.data.select_dtypes(include='category').columns.drop('y', errors='ignore')
        for i, col in enumerate(cat_cols, 1):
            plt.subplot((len(cat_cols)+2)//3, 3, i)
            pd.crosstab(self.data[col], self.data['y']).plot(
                kind='bar',
                stacked=True,
                ax=plt.gca()
            )
            plt.title(f'{col} Distribution by Target')
            plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


    def generateCorrelationMatrix(self) -> pd.DataFrame:
        """Compute and visualize feature correlations.
        
        Returns:
            DataFrame containing correlation coefficients.
        """
        self.data['y'] = self.data['y'].map({True: 1, False: 0}).astype('int8')
        corrMatrix = self.data.select_dtypes(include='number').corr()
        
        heatmap = sns.heatmap(
            corrMatrix,
            annot=True,            
            fmt=".1f",             
            cmap="coolwarm",       
            vmin=-1, vmax=1,       
            linewidths=1,          
            linecolor='black',     
            square=True,           
            cbar=False,            
            annot_kws={"size": 12, "color": "black"}  
        )
        plt.title("BANK DATA CORRELATIONS", fontsize=14, weight='bold', pad=20)
        plt.xticks(fontsize=10, rotation=45)
        plt.yticks(fontsize=10, rotation=0)
        cbar = plt.colorbar(heatmap.collections[0])
        cbar.set_label('Correlation Strength', rotation=270, labelpad=15)
        plt.tight_layout()
        plt.show()
        
        return corrMatrix

    def addConclusion(self, key: str, conclusion: str) -> None:
        """Store analytical findings.
        
        Args:
            key: Unique identifier for the conclusion.
            conclusion: Textual description of the insight.
        """
        self.generalConclusions[key] = conclusion
    
    def answerQuestion(self, question: str, answer: str) -> None:
        self.questions[question] = answer
    
    def calculateConversionRate(self, ColsType: str = "Demographic"):
        conversionRate = {}
        columnsSelected = []
        self.data['balanceGroup'] = pd.cut(
        self.data['balance'],
        bins=range(
            int(self.data['balance'].min()), 
            int(self.data['balance'].max()) + 1000, 
            1000
        ),
        right=False
    )
        if ColsType == 'Demographic':
            columnsSelected = ['age', 'job', 'marital', 'education', 'default', 'balanceGroup', 'housing', 'loan']
        elif ColsType == "Economic":
            columnsSelected = ['balanceGroup', 'default', 'housing', 'loan', 'job']
        def process_demographic(column, ax=None):
            """Helper function to process each columns group"""
            if column == 'y':
                return
            columnYesCount = self.data[self.data['y'] == 1].groupby(column).aggregate({'y': 'count'})\
                .reset_index().set_index(column)
            totalRecCount = self.data.groupby(column).aggregate({'y': 'count'})\
                .reset_index().set_index(column)
            columnYesCount['conversionRate'] = (columnYesCount['y'] / totalRecCount['y']) * 100
            if ax is not None:
                plot_data = columnYesCount.sort_values('conversionRate', ascending=False).head(5).reset_index()
                sns.barplot(x=column, y='conversionRate', data=plot_data, ax=ax, palette='coolwarm')
                ax.set_title(f'{column.capitalize()}')
                ax.tick_params(axis='x', rotation=45)
            conversionRate[column] = columnYesCount.sort_values(by='conversionRate', ascending=False)\
                .reset_index().iloc[[0]][[column, 'conversionRate']]
            print(f"{column}: Group {conversionRate[column][column].values[0]} has highest conversion rate {round(conversionRate[column]['conversionRate'].values[0], 2)} %")
            print("#-----------------------------------------------------------------#")
        fig1, axes1 = plt.subplots(2, 2, figsize=(15, 12))
        fig1.suptitle('Conversion Rates - Part 1/2', fontsize=16)
        for idx, column in enumerate(columnsSelected[:4]):
            process_demographic(column, ax=axes1.flatten()[idx])
        plt.tight_layout()
        plt.show()
        fig2, axes2 = plt.subplots(2, 2, figsize=(15, 12))
        fig2.suptitle('Conversion Rates - Part 2/2', fontsize=16)
        for idx, column in enumerate(columnsSelected[4:]):
            process_demographic(column, ax=axes2.flatten()[idx])
        plt.tight_layout()
        plt.show()

    def calculateOptimalContactTiming(self, per: str = 'all'):
        success_data = self.data[self.data['y'] == 1].copy()
        durationPerSub = success_data.groupby(per).agg({'y': 'count'})
        print("Top converting call durations:")
        print(durationPerSub.sort_values('y', ascending=False).head(10))
        perOrder = []
        if per == "month":
            perOrder = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 
                        'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        elif per == 'day':
            perOrder = [i for i in range(1, 32)]
        success_data['month'] = pd.Categorical(success_data[per], 
                                            categories=perOrder,
                                            ordered=True)
        plt.figure(figsize=(12, 6))
        perDuration = success_data[per].value_counts().sort_index()
        x = range(len(perDuration))
        plt.plot(x, perDuration.values, marker='o', color='#4C72B0', 
                linewidth=2, markersize=8)
        plt.xticks(x, perDuration.index)
        peak_idx = perDuration.argmax()
        plt.annotate(f'Peak: {perDuration.index[peak_idx]}\n({perDuration.max()} conversions)',
                    xy=(peak_idx, perDuration.max()),
                    xytext=(15, 15), 
                    textcoords='offset points',
                    arrowprops=dict(arrowstyle='->', color='red'),
                    bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.3))
        plt.title(f'Optimal Contact Timing Analysis\n{per.capitalize()} Conversion Trends', pad=20, fontsize=14)
        plt.xlabel(per.capitalize(), fontsize=12)
        plt.ylabel('Conversions', fontsize=12)
        plt.grid(axis='y', alpha=0.3)
        plt.xticks(rotation=45)
        avg_duration = success_data['duration'].mean()
        plt.text(0.02, 0.95, 
                f'Avg successful call duration: {avg_duration:.1f} seconds',
                transform=plt.gca().transAxes,
                bbox=dict(facecolor='white', alpha=0.8))
        plt.tight_layout()
        plt.show()
        return {
            'peak_{}'.format(per): perDuration.index[peak_idx],
            'peak_conversions': perDuration.max(),
            'avg_duration': avg_duration,
            'top_durations': durationPerSub.sort_values('y', ascending=False).head(5).index.tolist()
        }

    def calculateCommunicationConversionRate(self, columnName:str):
        """
        Calculates and visualizes conversion rates for a single column.
        
        Args:
            column (str): Column name to analyze
            plot (bool): Whether to generate visualization (default True)
        """
        columnYesCount = self.data[self.data['y'] == 1].groupby(columnName).agg({'y': 'count'})\
            .reset_index().set_index(columnName)
        totalRecCount = self.data.groupby(columnName).agg({'y': 'count'})\
            .reset_index().set_index(columnName)
        columnYesCount['conversionRate'] = (columnYesCount['y'] / totalRecCount['y']) * 100
        top_group = columnYesCount.sort_values('conversionRate', ascending=False)\
            .reset_index().iloc[[0]][[columnName, 'conversionRate']]
        print(f"{columnName}: Group {top_group[columnName].values[0]} has highest conversion rate {round(top_group['conversionRate'].values[0], 2)} %")
        print("#-----------------------------------------------------------------#")
        
        plt.figure(figsize=(10, 5))
        plot_data = columnYesCount.sort_values('conversionRate', ascending=False).head(10).reset_index()
        sns.barplot(
            x=columnName, 
            y='conversionRate', 
            data=plot_data, 
            palette='coolwarm',
            hue=columnName,  
            legend=False
        )  
        plt.title(f'Conversion Rates by {columnName}')
        plt.ylabel('Conversion Rate (%)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        return {
            'column': columnName,
            'top_group': top_group.to_dict('records')[0],
            'conversion_rates': columnYesCount.reset_index().to_dict('records')
        }

        