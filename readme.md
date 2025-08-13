# Bank Customer Call Subscription Analysis

> A comprehensive data science project focused on analyzing bank customer call data to understand subscription patterns through advanced data cleaning pipelines, exploratory data analysis, and business intelligence tools.

[![Dataset](https://img.shields.io/badge/Dataset-UCI%20ML%20Repository-blue)](https://archive.ics.uci.edu/dataset/222/bank+marketing)
[![Domain](https://img.shields.io/badge/Domain-Banking%20Analytics-green)](#)
[![Analytics](https://img.shields.io/badge/Analytics-Customer%20Behavior-orange)](#)

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Processing Pipeline](#data-processing-pipeline)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Excel Sheet Analysis](#excel-sheet-analysis)
- [Power BI Analysis](#power-bi-analysis)
- [Results](#results)
- [Contributing](#contributing)

## Overview

This project analyzes bank customer call subscription data using a robust data cleaning pipeline, comprehensive exploratory data analysis (EDA), and business intelligence tools (Excel and Power BI). The system processes banking datasets to identify customer behavior patterns, subscription trends, and key factors influencing customer decisions.

**Key Objectives:**
- Implement comprehensive data cleaning and optimization pipeline
- Perform thorough exploratory data analysis on customer call data
- Identify patterns in customer subscription behavior
- Handle data quality issues including outliers and missing values
- Optimize data types and memory usage for large datasets
- Visualize and analyze data using Excel and Power BI

## Dataset

**Source:** [Bank Marketing Dataset](https://archive.ics.uci.edu/dataset/222/bank+marketing) - UCI Machine Learning Repository

**Description:** 45,211 marketing campaign records from a Portuguese banking institution, containing customer demographics, campaign details, and conversion outcomes.

### Data Schema

| Feature | Type | Description |
|---------|------|-------------|
| `age` | Numeric | Customer age |
| `job` | Categorical | Job type (admin, blue-collar, entrepreneur, etc.) |
| `marital` | Categorical | Marital status (divorced, married, single) |
| `education` | Categorical | Education level (basic, high school, university) |
| `default` | Binary | Credit in default (yes/no) |
| `housing` | Binary | Housing loan (yes/no) |
| `loan` | Binary | Personal loan (yes/no) |
| `contact` | Categorical | Contact type (cellular, telephone) |
| `month` | Categorical | Last contact month |
| `day_of_week` | Categorical | Last contact day |
| `duration` | Numeric | Contact duration (seconds) |
| `campaign` | Numeric | Number of contacts in campaign |
| `pdays` | Numeric | Days since last contact |
| `previous` | Numeric | Previous campaign contacts |
| `poutcome` | Categorical | Previous campaign outcome |
| `emp_var_rate` | Numeric | Employment variation rate |
| `cons_price_idx` | Numeric | Consumer price index |
| `cons_conf_idx` | Numeric | Consumer confidence index |
| `euribor3m` | Numeric | Euribor 3-month rate |
| `nr_employed` | Numeric | Number of employees |
| **`y`** | **Binary** | **Target: Term deposit subscription (yes/no)** |

## Project Structure

```
BankCustomerCallSubscriptionAnalysis/
├── Data/
│   ├── bank/                   # Original bank marketing dataset
│   │   ├── bank-full.csv      # Complete dataset
│   │   ├── bank-names.txt     # Feature descriptions
│   │   └── bank.csv           # Reduced dataset
│   └── bank-additional/        # Additional dataset variations
│       ├── bank-additional-full.csv
│       ├── bank-additional-names.txt
│       └── bank-additional.csv
├── EDA/
│   ├── main.py                # Main execution script with Streamlit integration
│   ├── dataCleaningPipeline.py # Data cleaning and optimization pipeline
│   ├── EDAAnalysis.py         # Exploratory data analysis implementation
│   ├── AnalysisUtilis.py      # Utility functions for plot saving and analysis helpers
│   └── __pycache__/           # Python cache files
├── Figures/                   # Generated visualization outputs
│   ├── NumericalColumnsHistograms.png
│   ├── CategoricalColumnsHistograms.png
│   └── CorrelationMatrix.png
├── ExcelAnalysis/             # Excel files and screenshots
│   └── bank_marketing_analysis.xlsx
├── PowerBI/                   # Power BI dashboards and reports
│   └── bank_marketing_dashboard.pbix
└── README.md
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/BankCustomerCallSubscriptionAnalysis.git
   cd BankCustomerCallSubscriptionAnalysis
   ```
2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Analysis Tasks

### Task 1: Exploratory Data Analysis & Customer Insights 
**Objective:** Explore customer behavior patterns and identify marketing campaign optimization opportunities.

**Key Questions:**
- Which customer demographics show the highest conversion rates?
- How do contact duration and campaign frequency correlate with subscription probability?
- What is the optimal contact timing for maximizing conversions?
- How do economic indicators affect campaign success?
- Which communication channels yield the best response rates?

### Task 2: SQL Analysis & Customer Segmentation 
**Objective:** Build efficient queries for marketing campaign analysis and customer segmentation.

**Key Questions:**
- Which customer segments have the highest conversion rates?
- What is the campaign effectiveness by contact method and timing?
- Which customer profiles show the most promising opportunities?

### Task 3: A/B Test Simulator & Statistical Analysis 
**Objective:** Build Monte Carlo simulations for A/B testing with comprehensive statistical validation.

**Advanced Features:**
- Monte Carlo simulation engine with varying parameters
- Statistical power analysis and sample size calculations


**Statistical Questions:**
- What sample size is needed to detect a 20% increase in conversion rate?
- How do different significance levels affect test duration and costs?
- What is the probability of false positives in multiple testing?
- How does customer segment variance affect test reliability?

---

## Excel Sheet Analysis

Excel was used for:
- Quick data profiling and summary statistics
- Pivot tables for segmenting conversion rates by demographic and campaign features
- Visualizations (bar charts, histograms) for categorical and numerical features
- Filtering and conditional formatting to highlight outliers and trends

**Key Excel Insights:**
- Identified top-performing customer segments by age, job, and education
- Visualized conversion rates by month and contact type
- Summarized campaign effectiveness by frequency and duration

### Excel Analysis Screenshots

![Excel Pivot Table](ExcelAnalysis/excel_ss(2).png)
![Excel Multiple Charts](ExcelAnalysis/excel_ss(1).png)

## Power BI Analysis

Power BI dashboards were created to:
- Provide interactive exploration of customer segments and campaign results
- Visualize conversion rates, campaign timing, and channel effectiveness
- Enable drill-down analysis for business users

**Key Power BI Features:**
- Dynamic filtering by demographic and campaign attributes
- Time series visualizations for campaign performance
- Heatmaps and correlation matrices for feature relationships

### Power BI Analysis Screenshots

![Power BI Dashboard Overview](BiAnalysis/PowerBiBank(1).png)
![Power BI Drill Through Hierarchy](BiAnalysis/PowerBiBank(3).png)


## Analysis Results & Key Findings

**Key Business Insights:**

- **Students**: 26.06% conversion rate (highest performing segment)
- **Age Factor**: 68-year-olds show 65.22% conversion rate
- **Strategic Recommendation**: Target student segment and senior demographics for maximum ROI
- **Duration Impact**: Strong positive correlation (0.258) with subscription probability
- **Campaign Frequency**: Negative correlation (-0.089) - fewer contacts yield better results
- **Best Month**: May (384 conversions)
- **Best Day**: 30th of month (146 conversions)
- **Optimal Balance Range**: £3,116 - £4,116 (18.8% conversion rate)
- **Credit Status**: Non-defaulting customers convert at 8.39% (8× higher than defaulters)
- **Debt Impact**: Debt-free customers show 44% higher conversion potential
- **Housing Loans**: Customers without housing loans convert at 13.38%
- **Cellular**: 11.41% conversion rate (optimal channel)

**Technical Implementation:**
- Comprehensive data cleaning pipeline with outlier detection
- Memory optimization achieving significant storage savings
- Automated visualization generation with figure saving
- Correlation analysis and statistical insights
- Modular code architecture with utility functions

**Business Recommendations:**
1. **Primary Targeting**: Students and customers with £3K-£4K balances
2. **Channel Strategy**: Focus on cellular communication
3. **Timing Optimization**: Schedule campaigns in May, target month-end
4. **Risk Management**: Prioritize debt-free, creditworthy customers
5. **Quality Focus**: Emphasize meaningful contact duration over frequency

---

## Deliverables

### 1. Technical Analysis
- **EDA Notebook** - Comprehensive exploratory data analysis
- **SQL Queries** - Customer segmentation and cohort analysis
- **Statistical Models** - A/B testing frameworks and simulations
- **Visualization Suite** - Interactive charts and dashboards

### 2. Excel & Power BI Analysis
- **Excel Workbook** - Pivot tables, charts, and summary statistics
- **Power BI Dashboard** - Interactive business intelligence reports

---

## Results

### Key Findings
- **Optimal Contact Strategy** - Best timing and channel combinations
- **Customer Segmentation** - High-value target demographics
- **Campaign Optimization** - Data-driven improvement recommendations
- **Statistical Framework** - Robust A/B testing methodology

### Business Impact
- **Conversion Rate Improvement** - Higher ROI through targeted campaigns
- **Cost Optimization** - Reduced campaign costs through better targeting
- **Revenue Growth** - Estimated financial impact of optimizations
- **Testing Infrastructure** - Scalable framework for future experiments

---

## Skills Demonstrated

### Technical Skills
- **Advanced Statistics** - Monte Carlo methods
- **Python Development** - Object-oriented design, statistical libraries
- **Data Visualization** - Interactive dashboards and statistical plots
- **SQL Optimization** - Efficient queries and data engineering
- **Excel & Power BI** - Business intelligence and reporting

### Business Skills
- **A/B Testing Strategy** - Experimental design and interpretation
- **Campaign Optimization** - Data-driven marketing decisions
- **Growth Strategy** - Systematic experimentation framework