import pandas as pd
import seaborn as sns
from typing import Self
import matplotlib.pyplot as plt

class DataOptimizationPipeline:
      def __init__(self, dataPath: str, delimiter: str) -> None:
            self.dataPath = dataPath
            try:
                  self.DataFrame = pd.read_csv(filepath_or_buffer=self.dataPath, delimiter=delimiter)
                  self.__dropDuplicates().__containsNullValues().__getUniqueValues().__optimizeDataTypes().__removeOutliers()
                  self.DataFrame.info()
            except Exception as e:
                  print("error: {}".format(e))
      
      def __str__(self) -> str:
            try:
                  return self.DataFrame.info()
            except Exception as e:
                  print("error: {}".format(e))
      
      def __dropDuplicates(self):
            try:
                  self.DataFrame.drop_duplicates(inplace=True)
                  return self
            except Exception as e:
                  print("error: {}".format(e))
      
      def __containsNullValues(self) -> Self:
            try:
                  if self.DataFrame.isnull().sum().sum() == 0:
                        return self
                  else:
                        self.DataFrame.dropna(inplace=True)
                        return self
            except Exception as e:
                  print("error: {}".format(e))
      
      def __getUniqueValues(self) -> Self:
            columns = self.DataFrame.columns
            for column in columns:
                  print("Column: {}".format(column))
                  print("Unique values: {}".format(self.DataFrame[column].unique()))
                  print("-" * 150)
            return self
      
      def __optimizeDataTypes(self) -> Self:
            columns = self.DataFrame.columns
            for column in columns:
                  if self.DataFrame[column].isin(['yes', 'no','Yes', 'No']).all():
                        self.DataFrame[column] = self.DataFrame[column].map({'yes': True, 'no': False, 'Yes': True, 'No': False})
                        self.DataFrame[column].astype('bool')
                  if self.DataFrame[column].dtype == 'int64':
                        if self.DataFrame[column].max() <= 127:
                              self.DataFrame[column] = self.DataFrame[column].astype('int8')
                        elif self.DataFrame[column].max() <=  32767:
                              self.DataFrame[column] = self.DataFrame[column].astype('int16')
                        elif self.DataFrame[column].max() <=  2147483647:
                              self.DataFrame[column] = self.DataFrame[column].astype('int32')
                  if self.DataFrame[column].dtype == 'object':
                        self.DataFrame[column] = self.DataFrame[column].astype('category')
            print(self.DataFrame.info())
            return self
      

      def __removeOutliers(self):
            numericalCols = self.DataFrame.select_dtypes(include='number')
            
            for column in numericalCols.columns:
                  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
                  sns.boxplot(x=self.DataFrame[column], ax=ax1)
                  ax1.set_title(f'Before Outlier Removal: {column}')
                  Q1 = self.DataFrame[column].quantile(0.25)
                  Q3 = self.DataFrame[column].quantile(0.75)
                  IQR = Q3 - Q1
                  lower_bound = Q1 - 1.5 * IQR
                  upper_bound = Q3 + 1.5 * IQR
                  filtered_data = self.DataFrame[(self.DataFrame[column] >= lower_bound) & 
                                                (self.DataFrame[column] <= upper_bound)]
                  sns.boxplot(x=filtered_data[column], ax=ax2)
                  ax2.set_title(f'After Outlier Removal: {column}')
                  plt.tight_layout()  
                  plt.show()
                  self.DataFrame = filtered_data
            return self

data = DataOptimizationPipeline('Data/bank/bank-full.csv', ';')



