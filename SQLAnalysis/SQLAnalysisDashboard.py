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

      # region Question One
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
      
      # region Question Two
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
      
      questionTwoConc = """
      
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
      analyzer.answerQuestion("Q2: What is the campaign effectiveness by contact method and timing?", questionTwoConc)
      #endregion
      
      #region Question Three
      questionThreeConc = """
      
      """
      analyzer.answerQuestion("Q3: How do economic indicators correlate with campaign success?", questionThreeConc)
      #endregion
      
      #region Question Four
      questionFourConc = """
      
      """
      analyzer.answerQuestion("Q4: Which customer profiles show the most promising opportunities?", questionFourConc)
      #endregion
      
      #region Question Five
      questionFiveConc = """
      
      """
      analyzer.answerQuestion("Q5: What are the differences between successful and unsuccessful contacts?", questionFiveConc)
      #endregion

      questions = analyzer.generateQuestions()
      answers = analyzer.generateAnswers()
      # Q1
      st.subheader(next(questions))
      df = bankDataSqlIntegration.answerQueryAnswer(connection=connection,
      queryString=questionOneQuery, index=data.index)
      st.dataframe(df)
      st.pyplot(bankDataSqlIntegration.plotConversionRates(df, y='job'))
      st.markdown(next(answers))

      # Q2
      st.subheader(next(questions))
      df = bankDataSqlIntegration.answerQueryAnswer(connection=connection,
      queryString=questionTwoQueryOne, index=data.index)
      st.dataframe(df)
      st.pyplot(bankDataSqlIntegration.plotConversionRates(df, y='contact'))
      df = bankDataSqlIntegration.answerQueryAnswer(connection=connection,
      queryString=questionTwoQueryTwo, index=data.index)
      st.dataframe(df)
      st.pyplot(bankDataSqlIntegration.plotConversionRates(df, y='month'))
      st.markdown(next(answers))

      # Q3
      st.subheader(next(questions))
      df = bankDataSqlIntegration.answerQueryAnswer(connection=connection,
      queryString=questionTwoQueryTwo, index=data.index)
      st.dataframe(df)
      st.pyplot(bankDataSqlIntegration.plotConversionRates(df, y='month'))
      st.markdown(next(answers))

      # # Q4:
      # st.subheader(next(questions))
      # analyzer.calculateConversionRate("Economic")
      # st.markdown(next(answers))
      
      # # Q5:
      # st.subheader(next(questions))
      # analyzer.calculateCommunicationConversionRate('contact')
      # st.markdown(next(answers))