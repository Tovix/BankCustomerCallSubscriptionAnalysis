from EDAAnalysis import EDADataAnalyzer
from dataCleaningPipeline import BankDataOptimizationPipeline


if __name__ == "__main__":
    
    data = BankDataOptimizationPipeline('Data/bank/bank-full.csv', ';').DataFrame
    analyzer = EDADataAnalyzer(data)
    
    analyzer.categorizeDataColumnsTypes()
    analyzer.generateDescriptiveStatistics()
    analyzer.addConclusion("General Data Distributions",
    "From preliminary exploration, it is evident that most numerical features deviate significantly from normality—either through skewness, "
    "heavy tails, or discrete concentration—parametric tests like the t-test may not be appropriate "
    "without transformation. For statistical testing (e.g., A/B testing), non-parametric methods such "
    "as the Mann-Whitney U test or Monte Carlo Test are more suitable for these variables. For the categorical data we will"
    " use chi-square tests to compare the distributions between different categories.")

    analyzer.generateCorrelationMatrix()
    analyzer.addConclusion("Correlation Matrix", "Based on the correlation matrix, the relation between the"
    " independent variables and dependent variable (Y) is weak at best which confirms out conclusion"
    " General Data Distributions")
    

    
    