from EDAAnalysis import BankEdaDataAnalyzer
from dataCleaningPipeline import BankDataOptimizationPipeline


if __name__ == "__main__":
    
    #region init Data
    data = BankDataOptimizationPipeline('Data/bank/bank-full.csv', ';').DataFrame
    analyzer = BankEdaDataAnalyzer(data)
    #endregion
    
    #region General Analysis
    analyzer.categorizeDataColumnsTypes()
    analyzer.generateDescriptiveStatistics()
    analyzer.addConclusion("General Data Distributions",
    "From preliminary exploration, it is evident that most numerical features deviate significantly from normality—either through skewness, "
    "heavy tails, or discrete concentration—parametric tests like the t-test may not be appropriate "
    "without transformation. For statistical testing (e.g., A/B testing), non-parametric methods such "
    "as the Mann-Whitney U test or Monte Carlo Test are more suitable for these variables. For the categorical data we will"
    " use chi-square tests to compare the distributions between different categories.") 
    
    correlationMatrix = analyzer.generateCorrelationMatrix()
    analyzer.addConclusion("Correlation Matrix", "Based on the correlation matrix, the relation between the"
    " independent variables and dependent variable (Y) is weak at best which confirms out conclusion"
    " General Data Distributions")
    #endregion
    
    #region Answer Task 1: Question (1):
    analyzer.calculateConversionRate("Demographic")
    questionOneConc = """
        **Bank Marketing Conversion Analysis Conclusions**

        1. Age Demographics:
        - Highest conversion: 68-year-olds at 65.22%
        - Action: Target retirement-age customers aggressively

        2. Job Categories:
        - Most responsive: Students (26.06%)
        - Action: Create student-focused savings campaigns

        3. Marital Status:
        - Best conversion: Singles (11.42%)
        - Action: Develop messaging for unmarried customers

        4. Education Level:
        - Top performers: Tertiary-educated (11.73%)
        - Action: Use more sophisticated financial language

        5. Financial Health:
        - Best prospects: Customers without defaults (8.39%)
        - Warning: Avoid targeting those with credit defaults

        6. Balance Insights:
        - Perfect conversion: £4101 balance group (100%)
        - Note: Verify if this is a special customer segment

        7. Loan Status:
        - Housing loans: Non-loan holders convert better (13.38%)
        - Personal loans: Non-loan holders perform better (9.27%)

        STRATEGIC RECOMMENDATIONS:
        - Primary Targets: Retirees (68+) and students
        - Secondary Focus: Single, educated customers without loans
        - Avoid: Customers with poor credit history
        - Investigation Needed: Validate the 100% conversion group

        Note: All rates are percentage of 'yes' responses per demographic group.
        """
    analyzer.answerQuestion("Q1: Which customer demographics show the highest conversion rates?",questionOneConc)
    #endregion
    
    #region Answer Task 1: Question (2):
    print(correlationMatrix)
    questionTwoConc = """
        Based on the correlation matrix, it seems that both the contact duration and campaign frequency both have
        Slight association or rather insignificant correlation with the subscription probability
        """
    analyzer.answerQuestion("Q2: How do contact duration and campaign frequency correlate with subscription probability?", questionTwoConc)
    #endregion
    
    #region Answer Task 1: Question (3):
    topMonth = analyzer.calculateOptimalContactTiming(per='month')
    topDay = analyzer.calculateOptimalContactTiming(per='day')
    print(topMonth)
    print(topDay)
    questionThreeConc = """
    Based on the time trend analysis of the contact timing the optimal contact timing
    for maximizing conversions is {} with {} conversions. and based on the days of the month the best day is
    considered {} with {} conversions.
    """.format(topMonth['peak_month'], topMonth['peak_conversions'], topDay['peak_day'], topDay['peak_conversions'])
    analyzer.answerQuestion("Q3: What is the optimal contact timing for maximizing conversions?", questionThreeConc)
    #endregion
    
    #region Answer Task 1: Question (4):
    analyzer.calculateConversionRate("Economic")
    questionFourConc = economic_impact_conclusion = """
        **Economic Indicators Impact on Campaign Conversion Rates**

        Key Findings:
        1. **Account Balance**:
        - Optimal Range: £3,116 - £4,116
        - Conversion Rate: 18.8% (highest among financial metrics)
        - Implication: Customers with moderate savings show greatest propensity for term deposit adoption

        2. **Credit Status**:
        - Non-defaulting customers convert at 8.39%
        - Risk Insight: Creditworthy clients are significantly more receptive (8× conversion vs defaulters)

        3. **Debt Burden**:
        | Debt Type       | Conversion Rate (No Debt) |
        |-----------------|--------------------------|
        | Housing Loans   | 13.38%                   |
        | Personal Loans  | 9.27%                    |
        - Strategic Takeaway: Debt-free customers demonstrate 44% higher conversion potential

        4. **Employment Factor**:
        - Student Segment: 26.06% conversion (peak performance)
        - Comparative Advantage: 2.1× higher conversion than average economic segments

        Strategic Recommendations:
        ✓ Primary Targeting:
        - Students and young professionals with $3K-$4K balances
        - Debt-free customers with clean credit histories

        ✓ Portfolio Optimization:
        - Develop student-focused financial products
        - Create balance-tiered marketing campaigns

        ✓ Risk Mitigation:
        - De-prioritize high-debt segments
        - Implement credit-risk scoring for campaign eligibility

        Note: All findings derived from empirical conversion rate analysis of bank marketing data.
        Conversion rates reflect percentage of positive responses ('yes') per segment.
        """
    analyzer.answerQuestion("Q4: How do economic indicators affect campaign success? ",questionFourConc)
    #endregion
    
    #region Answer Task 1: Question (5):
    analyzer.calculateCommunicationConversionRate('contact')
    questionFiveConc = """
        **Communication Channel Effectiveness Analysis**
        
        Key Finding:
        - Optimal Channel: Cellular
        - Conversion Rate: 11.41%

        Actionable Insight:
        The data strongly suggests cellular communication should be the primary channel for customer
        outreach campaigns, with other channels serving supplementary roles.
        """
    analyzer.answerQuestion("Q5: Which communication channels yield the best response rates?", questionFiveConc)
    #endregion
    
    

    
    