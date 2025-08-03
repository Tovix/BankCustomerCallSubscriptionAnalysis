import sys
import psycopg2
import pandas as pd
import streamlit as st
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))
from EDA.EDAAnalysis import BankEdaDataAnalyzer  # noqa: E402
from SQLAnalysis.DataSqlIntegration import BankDataSqlIntegration  # noqa: E402

if __name__ == '__main__':

      # region Introduction
      st.title("Bank Customer Call Subscription SQL Analysis")
      st.header("Preliminary Data cleaning to check for nulls, duplicates or any anomalies in the data")
      st.text("""
      We transformed and optimzed bank data for our EDA analysis to a table in a Postgres SQL database.
      We will use psycopg2 python library, and DataSqlIntegration class to create the table and insert the data.
      The data will be stored in a table called bank_marketing.
      """)
      dataFramePath = "/home/tovix/projects/BankCustomerCallSubscriptionAnalysis/Data/bank/optimizedBankData.csv"
      data = pd.read_csv(dataFramePath)
      st.dataframe(data)
      #endregion

      # region Init Table bank_marketing
      bankDataSqlIntegration = BankDataSqlIntegration(dataPath=dataFramePath)
      connection = psycopg2.connect(database="Bank_Call_Subscription",host="localhost",user="postgres",
                                    password="postgres",port="5433")
      bankDataSqlIntegration.createTable(connection=connection)
      bankDataSqlIntegration.insertRecordsIntoTable(connection=connection, alreadyAdded=False)
      analyzer = BankEdaDataAnalyzer(data=data)
      #endregion

      #region Question One
      questionOneQuery = """
      DROP VIEW IF EXISTS YesResponseCount;
      DROP VIEW IF EXISTS ResponseCount;

      CREATE VIEW YesResponseCount AS
      SELECT
            job,
            COUNT(y) as response_count
      FROM
            bank_marketing
      WHERE
            y = 'True'
      GROUP BY
            job;

      CREATE VIEW ResponseCount AS
      SELECT
            job,
            COUNT(y) as total_response_count
      FROM
            bank_marketing
      GROUP BY
            job;

      SELECT 
            YesResponseCount.job,
            YesResponseCount.response_count,
            ResponseCount.total_response_count,
            ROUND(
            (YesResponseCount.response_count * 100.0 / ResponseCount.total_response_count), 
            2
      ) AS conversion_rate_percentage
      FROM 
            YesResponseCount
      INNER JOIN 
            ResponseCount
      ON 
            YesResponseCount.job = ResponseCount.job
      ORDER BY
            conversion_rate_percentage DESC
      """
      
      questionOneConc = """
      ### Conversion Rate Analysis by Customer Segment

      The campaign performance varies significantly across professional segments:

      **Highest Converting Segments**  
      - **Students (26.06%)**: Demonstrate nearly 3x higher conversion than the lowest segments, suggesting strong product-market fit for this demographic.  
      - **Retirees (15.59%)**: Second highest conversion, likely reflecting need for term deposit products in retirement planning.

      **Mid-Performing Segments**  
      - **Unemployed (11.9%)**: Above-average conversion warrants further investigation into driving factors.  
      - **Management (10.48%)**: Consistent conversion at scale (n=95,130), indicating reliable performance among white-collar professionals.

      **Lower-Performing Segments**  
      - **Technicians (8.01%)**: Underperforms relative to similar professional groups, suggesting messaging may not resonate.  
      - **Self-employed (8.55%)**: Below-average conversion indicates potential misalignment with this segment's banking needs.

      **Strategic Recommendations**:
      1. Maintain and potentially expand student-focused campaigns
      2. Investigate drivers behind unemployed segment performance
      3. Conduct market research with technicians/self-employed to identify barriers
      
      """
      analyzer.answerQuestion("Q1: Which customer segments have the highest conversion rates?", questionOneConc)
      #endregion
      
      #region Question Two
      questionTwoQueryOne = """
            DROP VIEW IF EXISTS YesResponseCount;
            DROP VIEW IF EXISTS ResponseCount;

            CREATE VIEW YesResponseCount AS
            SELECT
                  contact,
                  COUNT(y) as response_count
            FROM
                  bank_marketing
            WHERE
                  y = 'True'
            GROUP BY
                  contact;

            CREATE VIEW ResponseCount AS
            SELECT
                  contact,
                  COUNT(y) as total_response_count
            FROM
                  bank_marketing
            GROUP BY
                  contact;

            SELECT 
                  YesResponseCount.contact,
                  YesResponseCount.response_count,
                  ResponseCount.total_response_count,
                  ROUND(
                  (YesResponseCount.response_count * 100.0 / ResponseCount.total_response_count), 
                  2
            ) AS conversion_rate_percentage
            FROM 
                  YesResponseCount
            INNER JOIN 
                  ResponseCount
            ON 
                  YesResponseCount.contact = ResponseCount.contact
            ORDER BY
                  conversion_rate_percentage DESC
      """
      questionTwoQueryTwo = """
            DROP VIEW IF EXISTS YesResponseCount;
            DROP VIEW IF EXISTS ResponseCount;

            CREATE VIEW YesResponseCount AS
            SELECT
                  month,
                  COUNT(y) as response_count
            FROM
                  bank_marketing
            WHERE
                  y = 'True'
            GROUP BY
                  month;

            CREATE VIEW ResponseCount AS
            SELECT
                  month,
                  COUNT(y) as total_response_count
            FROM
                  bank_marketing
            GROUP BY
                  month;

            SELECT 
                  YesResponseCount.month,
                  YesResponseCount.response_count,
                  ResponseCount.total_response_count,
                  ROUND(
                  (YesResponseCount.response_count * 100.0 / ResponseCount.total_response_count), 
                  2
            ) AS conversion_rate_percentage
            FROM 
                  YesResponseCount
            INNER JOIN 
                  ResponseCount
            ON 
                  YesResponseCount.month = ResponseCount.month
            ORDER BY
                  conversion_rate_percentage DESC
      """
      contactAnalysis = """
            ### Campaign Effectiveness by Contact Method

            **Key Findings:**

            1. **Cellular Contact Dominance**
            - Achieved the highest conversion rate at **11.41%**
            - Accounts for **77035 positive responses** from **675,335 contacts** (88.7% of total successful conversions)
            - Should remain the primary outreach channel

            2. **Telephone Performance**
            - Moderate conversion rate of **9.29%**
            - Lower absolute conversions (**5208**) despite smaller contact pool (**56,079**)
            - Potential for optimization in scripting or call timing

            3. **Unknown Channel Concern**
            - Significantly lower conversion at **1.52%**
            - High contact volume (**317,285**) with poor return
            - Requires investigation into data quality or channel identification

            **Strategic Recommendations:**

            - **Maximize cellular outreach** while maintaining quality
            - **Analyze telephone call patterns** to identify peak conversion times
            - **Audit unknown contact sources** to either:
            - Improve targeting
            - Reallocate resources to higher-performing channels

            **Performance Summary:**
            - **3.3x** difference between top and bottom performing channels
            - **7.5x** more conversions from cellular vs telephone at similar contact-to-conversion ratios      
            """
      monthAnalysis = """
            
            
            ### Campaign Performance by Month

            **Seasonal Trends Analysis:**

            1. **Peak Performance Months**
            - **March (51.49%)**: Highest conversion rate, nearly 8.7x more effective than January
            - **September (44.61%)**: Strong second performer with consistent results
            - **December (43.88%)**: Holiday season shows high customer receptiveness

            2. **Mid-Performance Periods**
            - **October (42.09%)**: Maintains strong performance from Q3/Q4
            - **April (15.81%)**: Significant drop from March despite similar season

            3. **Low-Performance Months**
            - **January (5.95%)**: Worst performing month, potentially impacted by post-holiday financial constraints
            - **June-July-August**: Summer months show consistently lower conversion rates (7-8%)

            **Strategic Insights:**

            - **Q1 Focus**: March delivers exceptional results - consider increasing budget allocation
            - **Q4 Opportunity**: October-December period shows sustained high performance
            - **Summer Challenge**: June-August requires revised messaging or targeting approaches
            - **January Caution**: May warrant reduced outreach or different product positioning

            **Performance Variance:**
            - **46.54 percentage points** between best and worst months
            - **Top 3 months** account for **35.7%** of total conversions despite representing only **15.2%** of total contacts
            
            """
      questionTwoConc = [contactAnalysis, monthAnalysis]
      analyzer.answerQuestion("Q2: What is the campaign effectiveness by contact method and timing?", questionTwoConc)
      #endregion
      
      #region Question Three
      questionFourQueryOne = """
            SELECT
                  job,
                  marital,
                  education,
                  SUM(CASE WHEN y = 'True' THEN 1 ELSE 0 END) as conversions,
                  ROUND((100 * (SUM(CASE WHEN y = 'True' THEN 1 ELSE 0 END)) / COUNT(*)), 2) as conversion_rate_percentage
            FROM 
                  bank_marketing
            GROUP BY
                  job,
                  marital,
                  education
            ORDER BY
                  conversion_rate_percentage DESC
            LIMIT 10
      """
      questionFourQueryTwo = """
            SELECT
                  housing,
                  loan,
                  has_default,
                  CASE
                        WHEN balance > 4000 THEN 'more than 4000$'
                        WHEN balance BETWEEN 2000 AND 4000 THEN 'between 2000$ and 4000$'
                              WHEN balance BETWEEN 0 AND 2000 THEN 'less than 2000$'
                        ELSE 'less than 0$ (-ve balance)'
                  END AS balanceCategory,
                  SUM(CASE WHEN y = 'True' THEN 1 ELSE 0 END) as conversions,
                  ROUND((100 * (SUM(CASE WHEN y = 'True' THEN 1 ELSE 0 END)) / COUNT(*)), 2) as conversion_rate_percentage
            FROM 
                  bank_marketing
            GROUP BY
                  housing,
                  loan,
                  has_default,
                  balanceCategory
            ORDER BY
                  conversion_rate_percentage DESC
            LIMIT 10 
      """
      questionFourQueryThree = """
            SELECT
                  CASE
                        WHEN age >= 50 THEN 'older than 50'
                        WHEN age BETWEEN 20 AND 50 THEN 'between 20 and 50'
					WHEN age BETWEEN 0 AND 20 THEN 'younger than 20'
                        ELSE 'unknown'
                  END AS AgeCategory,
                  SUM(CASE WHEN y = 'True' THEN 1 ELSE 0 END) as conversions,
                  ROUND((100 * (SUM(CASE WHEN y = 'True' THEN 1 ELSE 0 END)) / COUNT(*)), 2) as conversion_rate_percentage
            FROM 
                  bank_marketing
            GROUP BY
                  AgeCategory
            ORDER BY
                  conversion_rate_percentage DESC
      """
      profileAnalysis = """
            ### Most Promising Customer Profiles

            **1. Highest Converting Segments**  
            - **Students (100% conversion)**:  
            - Married students with primary education show perfect conversion (100%)  
            - All student segments dominate top 8 positions  
            - Particularly strong with primary (100%) and unknown (30%) education  

            **2. Retirees Performance**  
            - **Divorced retirees (40%)**:  
            - Second highest converting group overall  
            - Consistent performance across education levels (31-40%)  

            **3. Demographic Patterns**  
            - **Marital status impact**:  
            - Married students outperform single students (100% vs 27-30%)  
            - Divorced individuals show strong conversion across segments  

            **4. Education Level Trends**  
            - **Primary education leads**:  
            - Highest rates in both student (100%) and self-employed (25%) segments  
            - Tertiary education shows variability (33-42%)  

            **Strategic Recommendations**:  
            1. **Prioritize student outreach**, especially married students  
            2. **Develop targeted campaigns** for divorced retirees  
            3. **Test primary education messaging** with other segments  
            4. **Investigate unknown education segment** (30% conversion)  
            5. **Optimize single student approaches** to match married student success  

            **Performance Summary**:  
            - **4:1 ratio** between top and bottom segments  
            - Student segments account for **70%** of top 10 positions  
            - Married status boosts conversion by **3.7x** vs single in student segment  
            """
      financialAnalysis = """
            ### Most Promising Financial Profiles

            **1. Highest Converting Segments**  
            - **Debt-free customers with high balances (37%)**:  
            - No housing/loans/defaults + >$4000 balance converts best  
            - 2.6x higher conversion than average (14%)  

            **2. Financial Stability Patterns**  
            - **Balance is key predictor**:  
            - >$4000: 28-37%  
            - $2000-$4000: 6-22%  
            - <$2000: 4-14%  
            - **Default status impact**:  
            - Customers without defaults convert 3x better (22% vs 4-5%)  

            **3. Debt Burden Impact**  
            - **Housing loans reduce conversion**:  
            - 28% (with mortgage) vs 37% (without) at high balance  
            - 6% (with mortgage) vs 22% (without) at mid-range balance  

            **Strategic Recommendations**:  
            1. **Premium targeting**: Focus on >$4000 balance customers without debt  
            2. **Debt mitigation offers**: Special terms for customers with housing loans  
            3. **Balance-building campaigns**: Incentivize deposits to move customers into higher balance tiers  
            4. **Default risk interventions**: Develop programs to prevent account defaults  
            5. **Tiered messaging**: Customize offers by balance ranges  

            **Performance Summary**:  
            - **9:1 ratio** between top and bottom segments  
            - Debt-free customers represent **83%** of top-performing segments  
            - Balance has **stronger impact** than debt status (>4000$ with debt outperforms <2000$ without)  
            """
      ageAnalysis = """
            ### Most Promising Age Segments

            **1. Highest Converting Segment**  
            - **Younger than 20 (40% conversion)**:  
            - Outperforms other age groups by 4.4x  
            - Despite smaller sample size (1,242 conversions)  

            **2. Age Performance Trends**  
            - **Sharp decline with age**:  
            - 20-50 years: 7% conversion  
            - 50+ years: 9% conversion  
            - **Inverse volume relationship**:  
            - Highest converting segment has lowest absolute conversions  
            - Lowest converting segment (20-50) drives 75% of total conversions  

            **Strategic Recommendations**:  
            1. **Youth-focused campaigns**: Develop products tailored for <20 demographic  
            2. **Life-stage messaging**:  
            - For 20-50: Focus on family/financial planning needs  
            - For 50+: Retirement income solutions  
            3. **Channel optimization**:  
            - Digital channels for younger segments  
            - Traditional channels for older demographics  
            4. **New customer acquisition**: Prioritize <20 segment given exceptional conversion  

            **Performance Summary**:  
            - **5.7:1 ratio** between top and bottom segments  
            - <20 segment converts **5.1x better** than core 20-50 demographic  
            - Despite high conversion, <20 represents only **0.6%** of total conversions  
            """
      questionFourConc = [
            profileAnalysis,
            financialAnalysis,
            ageAnalysis]
      
      analyzer.answerQuestion("Q3: Which customer profiles show the most promising opportunities?", questionFourConc)
      #endregion
      


      questions = analyzer.generateQuestions()
      answers = analyzer.generateAnswers()
      def answerSQLQuestion(connection:psycopg2.connect, queryString:str, y:list) -> None:
            df = bankDataSqlIntegration.answerQueryAnswer(connection=connection,
            queryString=queryString, index=data.index)
            st.dataframe(df)
            st.pyplot(bankDataSqlIntegration.plotConversionRates(df, yColumns=y))
      
      
      # Q1
      st.subheader(next(questions))
      answerSQLQuestion(connection=connection,
      queryString=questionOneQuery, y=['job'])
      st.markdown(next(answers))

      # Q2
      concList = next(answers)
      st.subheader(next(questions))
      answerSQLQuestion(connection=connection,
      queryString=questionTwoQueryOne, y=['contact'])
      st.markdown(concList[0])
      answerSQLQuestion(connection=connection,
      queryString=questionTwoQueryTwo, y=['month'])
      st.markdown(concList[1])

      # Q3:
      st.subheader(next(questions))
      concList = next(answers)
      answerSQLQuestion(connection=connection,
      queryString=questionFourQueryOne, y=['job', 'marital', 'education'])
      st.markdown(concList[0])
      answerSQLQuestion(connection=connection,
      queryString=questionFourQueryTwo, y=['housing', 'loan', 'has_default', 'balancecategory'])
      st.markdown(concList[1])
      answerSQLQuestion(connection=connection,
      queryString=questionFourQueryThree, y=['agecategory'])
      st.markdown(concList[2])
      
