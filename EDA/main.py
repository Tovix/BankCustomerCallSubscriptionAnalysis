import streamlit as st
from EDAAnalysis import BankEdaDataAnalyzer
from dataCleaningPipeline import BankDataOptimizationPipeline


if __name__ == "__main__":
    
    # region Introduction
    st.title("Bank Customer Call Subscription Analysis")
    st.subheader("https://archive.ics.uci.edu/dataset/222/bank+marketing")
    st.header("Preliminary Data cleaning to check for nulls, duplicates or any anomalies in the data")
    st.text("We will begin by checking the data for any duplicates or any null values and if found in case of "
            "duplicates we will drop them and in case of null values we will drop them as well if "
            "their numbers is small otherwise we will choose a sutiable value to replace them")
    #endregion
    
    #region init Data
    data = BankDataOptimizationPipeline('Data/bank/bank-full.csv', ';').DataFrame
    analyzer = BankEdaDataAnalyzer(data)
    st.subheader("Conclusion:")
    st.text("After the Preliminary Data cleaning we didn't find neither duplicates nor nulls and the data seems " 
            "to be clean.")
    #endregion
    
    #region General Analysis
    st.header("General Data Analysis to check data distributions and the relations between "
    "independent variables and target variable")
    analyzer.categorizeDataColumnsTypes()
    st.subheader("Numerical Distribution and Categorical Non indpendent Variables Vs Target Variable (y: Subscription Result)")
    analyzer.generateDescriptiveStatistics()
    st.subheader("Conclusion:")
    analyzer.addConclusion("General Data Distributions",
    "From preliminary exploration, it is evident that most numerical features deviate significantly from normality—either through skewness, "
    "heavy tails, or discrete concentration—parametric tests like the t-test may not be appropriate "
    "without transformation. For statistical testing (e.g., A/B testing), non-parametric methods such "
    "as the Mann-Whitney U test or Monte Carlo Test are more suitable for these variables. For the categorical data we will"
    " use chi-square tests to compare the distributions between different categories.") 
    st.subheader("Correlation Matrix of the data columns:")
    correlationMatrix = analyzer.generateCorrelationMatrix()
    st.subheader("Conclusion:")
    analyzer.addConclusion("Correlation Matrix", "Based on the correlation matrix, the relation between the"
    " independent variables and dependent variable (Y) is weak at best which confirms out conclusion"
    " General Data Distributions")
    #endregion
    
    #region Answer Task 1: Question (1):
    questionOneConc = """
        ### Bank Marketing Conversion Analysis  
        **Key Demographic Insights & Actionable Strategies**  

        ---

        #### Top Performing Segments  
        **1. Age Demographics**  
        - **Peak conversion:** 68-year-olds (65.22%)  
        - *Strategic action:* Prioritize retirement-age targeting  

        **2. Job Categories**  
        - **Most responsive:** Students (26.06%)  
        - *Strategic action:* Launch student-exclusive savings products  

        **3. Marital Status**  
        - **Highest conversion:** Singles (11.42%)  
        - *Strategic action:* Customize messaging for unmarried audiences  

        ---

        #### Education & Financial Profile  
        **4. Education Level**  
        - **Top performers:** Tertiary-educated (11.73%)  
        - *Execution tip:* Use advanced financial terminology  

        **5. Financial Health**  
        - **Best prospects:** Non-default customers (8.39%)  
        - *Risk alert:* Exclude customers with credit defaults  

        **6. Balance Insights**  
        - **100% conversion:** £4101 balance group  
        - *Validation needed:* Investigate this anomaly  

        ---

        #### Loan Behavior  
        **7. Loan Status**  
        - **Housing loans:** Better conversion with non-holders (13.38%)  
        - **Personal loans:** Non-holders outperform (9.27%)  

        ---

        ### Strategic Priorities  

        **Primary Targets**  
        - Retirees (68+ years) – Highest conversion rate  
        - Students – Most responsive group  

        **Secondary Focus**  
        - Single, educated customers without loans  

        **Exclusion Criteria**  
        - Customers with poor credit history  

        **Critical Next Steps**  
        - Validate the 100% conversion group (£4101 balance)  
        - Test retirement-age messaging variants  
        - Develop student-focused campaign materials  

        *Note: All conversion rates reflect 'yes' responses per segment.*  
    """
    analyzer.answerQuestion("Q1: Which customer demographics show the highest conversion rates?",questionOneConc)
    #endregion
    
    #region Answer Task 1: Question (2):
    questionTwoConc = """
        ## Correlation Analysis Findings

        Based on the correlation matrix, we observe the following relationships with subscription probability (`y`):

        | Feature               | Correlation Coefficient | Interpretation                          |
        |-----------------------|-------------------------|-----------------------------------------|
        | `duration`            |    0.3                  | Weak positive correlation               |
        | `campaign`            |   -0.1                  | Negligible negative correlation         |

        ### Key Insights:
        - **Contact Duration (`duration`)**  
        Shows a *weak positive relationship* (r = 0.3) with subscription likelihood  
        * Longer calls tend to have slightly higher conversion rates

        - **Campaign Contacts (`campaign`)**  
        Demonstrates a *negligible negative association* (r = -0.1)  
        * Number of contacts has minimal predictive value for subscriptions
        """
    analyzer.answerQuestion("Q2: How do contact duration and campaign frequency correlate with subscription probability?", questionTwoConc)
    #endregion
    
    #region Answer Task 1: Question (3):
    questionThreeConc = """
        ### Optimal Contact Timing Analysis

        **Monthly Performance**  
        The most effective month for conversions is **May** with **384 conversions**.

        **Daily Performance**  
        The highest-converting day of the month is **30** with **146 conversions**.

        *Recommendation*: Prioritize outreach during these peak periods to maximize conversion rates.
    """
    analyzer.answerQuestion("Q3: What is the optimal contact timing for maximizing conversions?", questionThreeConc)
    #endregion
    
    #region Answer Task 1: Question (4):
    questionFourConc = """
        ### Economic Indicators Impact on Campaign Conversion Rates  
        ---

        #### Key Findings  

        **1. Account Balance**  
            - **Optimal Range:** £3,116 - £4,116  
            - **Conversion Rate:** 18.8% (highest among financial metrics)  
            - **Implication:** Customers with moderate savings show greatest propensity for term deposit adoption  

        **2. Credit Status**  
            - **Non-defaulting customers:** 8.39% conversion  
            - **Risk Insight:** Creditworthy clients are significantly more receptive (8× conversion vs defaulters)  

        **3. Debt Burden**  
            - **Housing Loans:** 13.38% conversion  
            - **Personal Loans:** 9.27% conversion  
            - **Strategic Takeaway:** Debt-free customers demonstrate 44% higher conversion potential  

        **4. Employment Factor**  
            - **Student Segment:** 26.06% conversion (peak performance)  

        ---

        #### Strategic Recommendations  

        **Primary Targeting**  
            - Students and young professionals with £3K-£4K balances  
            - Debt-free customers with clean credit histories  

        **Portfolio Optimization**  
            - Develop student-focused financial products  
            - Create balance-tiered marketing campaigns  

        **Risk Mitigation**  
            - De-prioritize high-debt segments  
            - Implement credit-risk scoring for campaign eligibility  

        ---

        *Note:* All findings derived from empirical conversion rate analysis of bank marketing data.  
        Conversion rates reflect percentage of positive responses ('yes') per segment.  
    """
    analyzer.answerQuestion("Q4: How do economic indicators affect campaign success? ",questionFourConc)
    #endregion
    
    #region Answer Task 1: Question (5):
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
    
    questions = analyzer.generateQuestions()
    answers = analyzer.generateAnswers()
    
    # Q1
    st.subheader(next(questions))
    analyzer.calculateConversionRate("Demographic")
    st.markdown(next(answers))
    
    # Q2
    st.subheader(next(questions))
    st.markdown(next(answers))
    
    # Q3
    st.subheader(next(questions))
    analyzer.calculateOptimalContactTiming(per='month')
    analyzer.calculateOptimalContactTiming(per='day')
    st.markdown(next(answers))
    
    # Q4:
    st.subheader(next(questions))
    analyzer.calculateConversionRate("Economic")
    st.markdown(next(answers))
    
    # Q5:
    st.subheader(next(questions))
    analyzer.calculateCommunicationConversionRate('contact')
    st.markdown(next(answers))
    
    
    
    

    
    

    
    