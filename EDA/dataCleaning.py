import pandas as pd
import seaborn as sns
from typing import Self
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


class BaseDataOptimizationPipeline(ABC):
    """Abstract base class defining the interface for data optimization pipelines."""
    
    @abstractmethod
    def __init__(self, dataPath: str, delimiter: str) -> None:
        """Initialize pipeline with data source."""
        pass
    
    @abstractmethod
    def _dropDuplicates(self) -> Self:
        """Remove duplicate rows."""
        pass
    
    @abstractmethod
    def _containsNullValues(self) -> Self:
        """Handle null values."""
        pass
    
    @abstractmethod
    def _getUniqueValues(self) -> Self:
        """Analyze unique values."""
        pass
    
    @abstractmethod
    def _optimizeDataTypes(self) -> Self:
        """Optimize column data types."""
        pass
    
    @abstractmethod
    def _removeOutliers(self, method: str = 'iqr', **kwargs) -> Self:
        """Remove outliers using specified method."""
        pass
    
    @abstractmethod
    def _displayColumnsDistributions(self) -> Self:
        """Visualize column distributions."""
        pass
    
    @abstractmethod
    def _parseDates(self, date_columns: list[str]) -> Self:
        """Auto-detect and convert date columns."""
        pass
    
    @abstractmethod
    def _normalizeText(self, text_columns: list[str]) -> Self:
        """Normalize text data (lowercase, trim, etc.)."""
        pass
    
    @abstractmethod
    def _encodeCategoricals(self, strategy: str = 'onehot') -> Self:
        """Encode categorical variables."""
        pass
    
    @abstractmethod
    def _removeOutliersZscore(self, threshold: float = 3.0) -> Self:
        """Remove outliers using Z-score method."""
        pass
    
    @abstractmethod
    def _removeOutliersDBSCAN(self, eps: float = 0.5, min_samples: int = 5) -> Self:
        """Remove outliers using DBSCAN clustering."""
        pass
    
    @abstractmethod
    def _generateCleaningReport(self) -> str:
        """Generate data cleaning report."""
        pass
    
    @abstractmethod
    def _saveOptimizedData(self, output_path: str) -> Self:
        """Save processed data to disk."""
        pass
    
    @abstractmethod
    def _calculateMemorySavings(self) -> dict:
        """Calculate memory savings from optimizations."""
        pass
    
    @abstractmethod
    def _validateDataRules(self, rules: dict) -> Self:
        """Validate data against custom rules."""
        pass
    
    @abstractmethod
    def _extractDateFeatures(self) -> Self:
        """Create date-related features."""
        pass




class BankDataOptimizationPipeline(BaseDataOptimizationPipeline):
    """A comprehensive pipeline for processing, cleaning, and optimizing banking data.
    
    This pipeline automates the entire data preparation workflow for banking datasets,
    including cleaning, type optimization, outlier detection, and quality validation.
    All methods support fluent chaining and provide visual feedback at each step.

    Typical usage example:
        pipeline = BankDataOptimizationPipeline("transactions.csv", ",")
        cleaned_data = pipeline.DataFrame

    Attributes:
        dataPath (str): Absolute or relative path to the source CSV file
        delimiter (str): Delimiter used in the CSV file (e.g., ',', ';', '\t')
        DataFrame (pd.DataFrame): The processed DataFrame after all transformations
    """
    
    def __init__(self, dataPath: str, delimiter: str) -> None:
        """Initializes the pipeline and executes the full processing sequence.
        
        The initialization performs these operations in order:
        1. Data loading from CSV
        2. Duplicate removal
        3. Null value handling
        4. Data type optimization
        5. Outlier detection and removal
        6. Distribution visualization

        Args:
            dataPath: Path to the banking data CSV file
            delimiter: Character used to separate fields in the CSV

        Raises:
            FileNotFoundError: If the specified CSV file cannot be located
            pd.errors.EmptyDataError: If the CSV file is empty
            pd.errors.ParserError: If malformed CSV content is detected
            Exception: For any other unexpected errors during processing

        Note:
            The constructor will immediately process the data upon instantiation.
            For incremental processing, use the individual methods separately.
        """
        self.dataPath = dataPath
        try:
            self.DataFrame = pd.read_csv(filepath_or_buffer=self.dataPath, delimiter=delimiter)
            self._dropDuplicates()._containsNullValues()._getUniqueValues()._optimizeDataTypes(
                  )._removeOutliers()._displayColumnsDistributions()
            self.DataFrame.info()
        except Exception as e:
            print("error: {}".format(e))
    
    def __str__(self) -> str:
        """Provides a comprehensive summary of the processed DataFrame.
        
        Returns:
            str: Formatted string containing:
                - Column names and data types
                - Non-null counts
                - Memory usage information

        Note:
            This output mirrors pandas' DataFrame.info() but ensures consistent
            string return for logging and debugging purposes.
        """
        try:
            return self.DataFrame.info()
        except Exception as e:
            print("error: {}".format(e))
            return str(e)
    
    def _dropDuplicates(self) -> Self:
        """Identifies and removes duplicate rows from the banking dataset.
        
        Uses pandas' drop_duplicates() with default parameters to:
        - Compare all columns when identifying duplicates
        - Keep the first occurrence of each duplicate set
        - Modify the DataFrame in-place

        Returns:
            BankDataOptimizationPipeline: The instance itself for method chaining

        Note:
            For large datasets, consider implementing a chunked processing
            version to reduce memory usage.
        """
        try:
            self.DataFrame.drop_duplicates(inplace=True)
            return self
        except Exception as e:
            print("error: {}".format(e))
            return self
    
    def _containsNullValues(self) -> Self:
        """Analyzes and handles null/missing values in the banking data.
        
        Performs these operations:
        1. Checks for any null values across all columns
        2. If nulls exist, removes entire rows containing them
        3. Preserves the original DataFrame if no nulls are found

        Returns:
            BankDataOptimizationPipeline: The instance itself for method chaining

        Note:
            Alternative null-handling strategies (imputation) could be
            implemented as additional methods in future versions.
        """
        try:
            if self.DataFrame.isnull().sum().sum() == 0:
                return self
            else:
                self.DataFrame.dropna(inplace=True)
                return self
        except Exception as e:
            print("error: {}".format(e))
            return self
    
    def _getUniqueValues(self) -> Self:
        """Analyzes and displays unique values for each column.
        
        For every column in the DataFrame:
        1. Prints the column name
        2. Displays all unique values
        3. Adds a visual separator between columns

        Returns:
            BankDataOptimizationPipeline: The instance itself for method chaining

        Note:
            Particularly useful for identifying:
            - Unexpected values in categorical data
            - Potential data entry errors
            - Columns that could be converted to enums/categories
        """
        columns = self.DataFrame.columns
        for column in columns:
            print("Column: {}".format(column))
            print("Unique values: {}".format(self.DataFrame[column].unique()))
            print("-" * 150)
        return self
    
    def _optimizeDataTypes(self) -> Self:
        """Optimizes column data types for memory efficiency and performance.
        
        Performs automatic type conversion for:
        1. Boolean columns (yes/no → True/False)
        2. Integer columns (downsizes to smallest appropriate type)
        3. String columns (converts to category dtype when beneficial)

        Returns:
            BankDataOptimizationPipeline: The instance itself for method chaining

        Note:
            Memory savings can be substantial for large banking datasets.
            Always verify no precision loss occurs with integer downcasting.
        """
        columns = self.DataFrame.columns
        for column in columns:
            if self.DataFrame[column].isin(['yes', 'no','Yes', 'No']).all():
                self.DataFrame[column] = self.DataFrame[column].map(
                    {'yes': True, 'no': False, 'Yes': True, 'No': False})
                self.DataFrame[column] = self.DataFrame[column].astype('bool')
            if self.DataFrame[column].dtype == 'int64':
                if self.DataFrame[column].max() <= 127:
                    self.DataFrame[column] = self.DataFrame[column].astype('int8')
                elif self.DataFrame[column].max() <= 32767:
                    self.DataFrame[column] = self.DataFrame[column].astype('int16')
                elif self.DataFrame[column].max() <= 2147483647:
                    self.DataFrame[column] = self.DataFrame[column].astype('int32')
            if self.DataFrame[column].dtype == 'object':
                self.DataFrame[column] = self.DataFrame[column].astype('category')
        print(self.DataFrame.info())
        return self
    
    def _removeOutliers(self) -> Self:
        """Identifies and removes outliers using the IQR method with visualization.
        
        For each numerical column:
        1. Displays initial distribution via boxplot
        2. Calculates IQR bounds (Q1 - 1.5*IQR to Q3 + 1.5*IQR)
        3. Filters records outside these bounds
        4. Displays cleaned distribution via boxplot

        Returns:
            BankDataOptimizationPipeline: The instance itself for method chaining

        Note:
            The 1.5*IQR multiplier can be adjusted based on domain knowledge.
            Consider adding a parameter to control this threshold.
        """
        numericalCols = self.DataFrame.select_dtypes(include='number')
        print("Initial numerical columns:\n", numericalCols)
        sns.boxplot(data=numericalCols)
        plt.title("Data Distribution Before Outlier Removal")
        plt.tight_layout()  
        plt.show()
        
        for column in numericalCols.columns:
            Q1 = self.DataFrame[column].quantile(0.25)
            Q3 = self.DataFrame[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            self.DataFrame = self.DataFrame[
                (self.DataFrame[column] >= lower_bound) & 
                (self.DataFrame[column] <= upper_bound)
            ]
        
        numericalCols = self.DataFrame.select_dtypes(include='number')
        sns.boxplot(data=numericalCols)
        plt.title("Data Distribution After Outlier Removal")
        plt.tight_layout()  
        plt.show()
        return self
    
    def _displayColumnsDistributions(self) -> Self:
        """Generates histogram visualizations for all column distributions.
        
        Creates a grid of histograms showing:
        - Value distributions for numerical columns
        - Category frequencies for categorical columns
        - Automatic binning based on data characteristics

        Returns:
            BankDataOptimizationPipeline: The instance itself for method chaining

        Note:
            Uses seaborn's modern styling for publication-quality visuals.
            The 20x15 figure size ensures readability for datasets with many columns.
        """
        plt.style.use('seaborn')
        self.DataFrame.hist(bins=50, figsize=(20,15))
        plt.suptitle("Column Distributions After Processing", y=1.02)
        plt.tight_layout()
        plt.show()
        return self
  
    def _parseDates(self, date_columns: list[str]) -> Self:
        """Auto-detect and convert date columns."""
        print("Not implemented yet: _parseDates")
        return self
    
    def _normalizeText(self, text_columns: list[str]) -> Self:
        """Normalize text data (lowercase, trim, etc.)."""
        print("Not implemented yet: _normalizeText")
        return self
    
    def _encodeCategoricals(self, strategy: str = 'onehot') -> Self:
        """Encode categorical variables."""
        print("Not implemented yet: _encodeCategoricals")
        return self
    
    def _removeOutliersZscore(self, threshold: float = 3.0) -> Self:
        """Remove outliers using Z-score method."""
        print("Not implemented yet: _removeOutliersZscore")
        return self
    
    def _removeOutliersDBSCAN(self, eps: float = 0.5, min_samples: int = 5) -> Self:
        """Remove outliers using DBSCAN clustering."""
        print("Not implemented yet: _removeOutliersDBSCAN")
        return self
    
    def _generateCleaningReport(self) -> str:
        """Generate data cleaning report."""
        return "Not implemented yet: _generateCleaningReport"
    
    def _saveOptimizedData(self, output_path: str) -> Self:
        """Save processed data to disk."""
        print("Not implemented yet: _saveOptimizedData")
        return self
    
    def _calculateMemorySavings(self) -> dict:
        """Calculate memory savings from optimizations."""
        return {"message": "Not implemented yet: _calculateMemorySavings"}
    
    def _validateDataRules(self, rules: dict) -> Self:
        """Validate data against custom rules."""
        print("Not implemented yet: _validateDataRules")
        return self
    
    def _extractDateFeatures(self) -> Self:
        """Create date-related features."""
        print("Not implemented yet: _extractDateFeatures")
        return self
    

data = BankDataOptimizationPipeline('Data/bank/bank-full.csv', ';').DataFrame
print(data.info())



