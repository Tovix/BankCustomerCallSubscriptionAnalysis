import streamlit as st
from EDA.EDAAnalysis import BankEdaDataAnalyzer
from EDA.dataCleaningPipeline import BankDataOptimizationPipeline 


if __name__ == "__main__":
    
    # region Introduction
    st.title("Bank Customer Call Subscription EDA Analysis")
    st.subheader("https://archive.ics.uci.edu/dataset/222/bank+marketing")
    st.header("Preliminary Data cleaning to check for nulls, duplicates or any anomalies in the data")
    st.text("We will begin by checking the data for any duplicates or any null values and if found in case of "
            "duplicates we will drop them and in case of null values we will drop them as well if "
            "their numbers is small otherwise we will choose a sutiable value to replace them")
    #endregion
    
    #region init Data
    data = BankDataOptimizationPipeline('Data/bank/bank-full.csv', ';').DataFrame
    st.dataframe(data)
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
    
    #region Task 1:
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
    #endregion
    
    #region Task 2:
    #region Task 2: Question (1):
    questionOneConc = """
        ### Sample Size Estimation for Detecting a 20% Increase in Conversion Rate

        ### Objective:
        To determine the minimum sample size required to detect a 20% relative increase in the current term deposit subscription rate (`y`) from a marketing campaign, with:

        - Significance level (α) = 0.05  
        - Statistical power (1 - β) = 0.80  
        - Two-sided test

        ### Baseline Stats from Dataset:

        - Baseline conversion rate = 11.7% (derived from the dataset)
        - Target conversion rate = 14.04% (20% increase over baseline)

        ### Result:

        The sample size needed to detect a 20% increase in conversion rate is **4,714 clients per group**.

        This means you would need at least 4,714 observations in each group (e.g., control vs treatment) to have an 80% chance of detecting this difference, assuming it exists.

        ### Statistical Theory

        #### What kind of test did we perform?

        We performed a **power analysis for a two-proportion z-test**.

        #### Test Name:
        **Two-Sample Proportion Z-Test Power Analysis**

        This is not a hypothesis test, but a planning procedure used to estimate the sample size needed before running an experiment.

        ### Theoretical Background:

        Power analysis revolves around four main components:

        | Component         | Description |
        |-------------------|-------------|
        | Effect Size       | The standardized difference between the two proportions (baseline vs. target). |
        | Alpha (α)         | The probability of a Type I error — falsely rejecting the null hypothesis. |
        | Power (1 - β)     | The probability of correctly detecting a true effect — avoiding a Type II error. |
        | Sample Size       | The number of observations needed per group to achieve the desired power. |

        In this case:
        - p1 = 0.117 (baseline)
        - p2 = 0.1404 (20% increase)
        - effect_size = Cohen’s h = 2 * arcsin(√p1) - 2 * arcsin(√p2)

        The Z-test for proportions checks whether the difference between two proportions is statistically significant.

        ### Why Use This Test?

        - The variable `y` is binary (yes/no).
        - You're comparing two proportions — the current conversion rate vs. an improved version.
        - You’re in the planning phase of an experiment or marketing intervention.
        - You want to know how many samples are needed to detect a meaningful increase.
    """
    analyzer.answerQuestion("Q1: What sample size is needed to detect a 20% increase in conversion rate?",questionOneConc)
    #endregion
    #region Task 2: Question (2):
    questionTwoConc = """
        ## Conclusion: Impact of Significance Level (α) on Test Duration and Cost

        We conducted a sensitivity analysis to understand how varying the significance level (α) impacts the **required sample size**, **test duration**, and **operational cost**.

        ### Key Parameters:
        - **Effect Size Target**: 20% increase in baseline conversion rate
        - **Power (1 - β)**: 0.80
        - **Daily Traffic**: 5,000 users (split between 2 groups)
        - **Cost per User**: $0.40

        ### Observations:

        - As **α decreases** (i.e., the test becomes more stringent), the **required sample size increases**.
        - This increase leads to **longer test durations** and **higher costs**, even though the traffic and cost per user remain constant.
        - For example:
        - At **α = 0.15**, the test requires ~3,125 users per group, resulting in ~1.25 days of duration and ~$2,500 total cost.
        - At **α = 0.01**, the sample size increases to ~7,015 per group, which translates into ~2.8 days and ~$5,612 in cost.

        ### Interpretation:

        - Lowering α reduces the risk of a Type I error (false positive), which is statistically safer, but comes at the expense of **more time and cost**.
        - In high-traffic, low-cost environments, a stricter α may be feasible.
        - In low-traffic or cost-sensitive environments, a higher α might be a better tradeoff to run tests more quickly.

        ### Recommendation:

        Choose a significance level based on:
        - **Business risk tolerance** (how bad is a false positive?)
        - **Traffic availability**
        - **Budget and operational constraints**

        For most A/B tests in practice, α values between **0.05 and 0.10** offer a reasonable trade-off between confidence and cost.
    """
    analyzer.answerQuestion("Q2: How do different significance levels affect test duration and costs?",questionTwoConc)
    #endregion
    #region Task 2: Question (3):
    questionThreeConc = """
        ### Conclusion:

        As the number of independent hypothesis tests increases, the probability of observing **at least one false positive** (Type I error) rises significantly:

        - With **10 tests**, the chance of getting at least one false positive is approximately **40%**.
        - At **20 tests**, this grows to around **64%**.
        - By **50 tests**, it surpasses **92%**.
        - With **100 tests**, the probability reaches **over 99%**, meaning a false positive is almost certain by chance alone.

        ---

        #### Implications:

        This demonstrates the **multiple testing problem**, where running many tests without adjustment **greatly increases the likelihood of Type I errors** (false positives).

        ---

        #### Best Practices:

        - Apply **multiple testing corrections** such as **Bonferroni**, **Holm-Bonferroni**, or **False Discovery Rate (FDR)** to control the overall false positive rate.
        - Reduce the number of unplanned tests and prioritize hypotheses based on prior research or business goals.
        """
    analyzer.answerQuestion("Q3: What is the probability of false positives in multiple testing?",questionThreeConc)
    #endregion
    #region Task 2: Question (4):
    questionFourConc = """
        ### Statistical Test Conclusion

        We conducted a **Monte Carlo permutation test** and calculated **odds ratios** to assess whether numerical features are significantly associated with a user subscribing to a term deposit (`y`).

        Below is a summary of the statistical conclusions for each numerical variable:

        | Variable   | Null Hypothesis (H₀)                                 | Alternative Hypothesis (H₁)                                 | p-value | Odds Ratio | Conclusion                                                                 |
        |------------|------------------------------------------------------|--------------------------------------------------------------|---------|-------------|----------------------------------------------------------------------------|
        | **age**     | Age distribution is the same across both groups      | Age differs between subscribed and unsubscribed groups       | 0.0004  | 0.78        | **Reject H₀**. Age is statistically significant with a weak inverse effect. |
        | **balance** | Balance has no effect on subscription                | Balance differs between groups                               | 0       | 1.74        | **Reject H₀**. Balance is highly significant and positively associated.    |
        | **day**     | Call day distribution is similar for both groups     | Call day differs between groups                              | 0.0004  | 0.75        | **Reject H₀**. Day is significant but weakly inversely related.            |
        | **duration**| Call duration is unrelated to subscription           | Duration differs between groups                              | 0       | 5.27        | **Reject H₀**. Strongest positive predictor for subscription.              |
        | **campaign**| Number of contacts has no effect                     | Campaign count differs between groups                        | 0       | 0.55        | **Reject H₀**. Significant inverse relationship.                           |
        | **pdays**   | Previous contact timing is unrelated                 | Pdays differs between groups                                 | 1       | NaN         | **Fail to reject H₀**. No significance. Data likely uninformative.         |
        | **previous**| Previous contacts count has no effect                | Previous differs between groups                              | 1       | NaN         | **Fail to reject H₀**. No significance. Possibly due to zero variance.     |

         **Interpretation**:
        - The variables `duration`, `balance`, and `campaign` show the strongest and most interpretable associations with subscription behavior.
        - Variables like `pdays` and `previous` lack statistical evidence or may have skewed/constant values.
        - Monte Carlo results may slightly vary between runs due to randomness, but significance remains consistent across strong predictors.
    """
    analyzer.answerQuestion("Q4: How does customer segment variance affect test reliability?",questionFourConc)
    #endregion
    #endregion
    
    #region Task 1: EDA Analysis StreamLit
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
    #endregion
    
    #region Task 2: Statistical Analysis
    # Q1:
    st.subheader(next(questions))
    analyzer.sampleSizeEstimation(increaseRate=1.2, alpha=0.05, power=0.8)
    st.markdown(next(answers))
    # Q2:
    st.subheader(next(questions))
    sampleSizes = analyzer.SignificanceSensitivityEstimation(increaseRate=1.2, power=0.8)
    results = analyzer.durationAndCostEstimation(sampleSizeList=sampleSizes, totalGroups=2,
    dailyTraffic=5000, costPerUser=0.40)
    st.markdown(next(answers))
    # Q3:
    st.subheader(next(questions))
    results = analyzer.simulateFalsePositiveRate(alpha=0.05, maxTests=100)
    st.markdown(next(answers))
    # Q4:
    st.subheader(next(questions))
    results = analyzer.monteCarloPValueWithOdds()
    st.write(results)
    st.markdown(next(answers))
    #endregion
    
    

    
    

    
    