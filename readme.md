# Bank Customer Call Subscription Analysis

> A comprehensive data science project focused on analyzing bank customer call data to understand subscription patterns through advanced data cleaning pipelines and exploratory data analysis.

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
- [Results](#results)
- [Contributing](#contributing)

## Overview

This project analyzes bank customer call subscription data using a robust data cleaning pipeline and comprehensive exploratory data analysis (EDA). The system processes banking datasets to identify customer behavior patterns, subscription trends, and key factors influencing customer decisions.

**Key Objectives:**
- Implement comprehensive data cleaning and optimization pipeline
- Perform thorough exploratory data analysis on customer call data
- Identify patterns in customer subscription behavior
- Handle data quality issues including outliers and missing values
- Optimize data types and memory usage for large datasets

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
└── README.md
```


## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/BankCustomerCallSubscriptionAnalysis.git
   cd BankCustomerCallSubscriptionAnalysis
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
- How do economic indicators correlate with campaign success?
- Which customer profiles show the most promising opportunities?
- What are the differences between successful and unsuccessful contacts?

### Task 3: A/B Test Simulator & Statistical Analysis 
**Objective:** Build Monte Carlo simulations for A/B testing with comprehensive statistical validation.

**Advanced Features:**
- Monte Carlo simulation engine with varying parameters
- Statistical power analysis and sample size calculations
- Multiple testing correction (Bonferroni, FDR)
- Sequential testing with early stopping rules
- Bayesian A/B testing with credible intervals

**Statistical Questions:**
- What sample size is needed to detect a 20% increase in conversion rate?
- How do different significance levels affect test duration and costs?
- What is the probability of false positives in multiple testing?
- How does customer segment variance affect test reliability?
- What is the expected ROI impact of different optimization strategies?

### Task 4: Machine Learning & Predictive Modeling
**Objective:** Build predictive models to forecast customer subscription probability and optimize marketing campaigns through advanced ML techniques.

**Core ML Components:**
- **Binary Classification Models** - Predict subscription likelihood (yes/no)
- **Feature Engineering Pipeline** - Transform raw data into ML-ready features
- **Model Ensemble Methods** - Combine multiple algorithms for robust predictions
- **Hyperparameter Optimization** - Automated tuning for peak performance
- **Model Interpretability** - SHAP values and feature importance analysis

**Advanced ML Features:**
- **Customer Lifetime Value (CLV) Prediction** - Forecast long-term customer worth
- **Churn Risk Modeling** - Identify customers likely to discontinue services
- **Propensity Score Matching** - Advanced causal inference for campaign effectiveness
- **Time Series Forecasting** - Predict optimal contact timing patterns
- **Clustering & Segmentation** - Unsupervised customer grouping for targeted campaigns

**Model Development Pipeline:**
1. **Data Preprocessing** - Handle missing values, outliers, and feature scaling
2. **Feature Selection** - Recursive feature elimination and correlation analysis
3. **Model Training** - Random Forest, XGBoost, Logistic Regression, Neural Networks
4. **Cross-Validation** - Stratified K-fold validation with temporal splits
5. **Performance Evaluation** - ROC-AUC, Precision-Recall, F1-Score, Business Metrics
6. **Model Deployment** - Production-ready API with monitoring and retraining

**Business ML Questions:**
- Which features are most predictive of customer subscription behavior?
- How accurately can we predict conversion probability for new prospects?
- What is the optimal customer acquisition cost based on predicted CLV?
- Which customer segments should receive different marketing strategies?
- How can we optimize campaign timing using predictive models?
- What is the expected lift from ML-driven targeting vs. random campaigns?

**Technical Implementation:**
- **`ml_pipeline.py`** - End-to-end ML pipeline with preprocessing and training
- **`feature_engineering.py`** - Advanced feature creation and selection methods
- **`model_evaluation.py`** - Comprehensive model assessment and validation
- **`prediction_api.py`** - REST API for real-time prediction serving
- **`model_monitoring.py`** - Performance tracking and drift detection
- **`explainability.py`** - Model interpretation and feature importance analysis

**Expected Deliverables:**
- Trained ML models with >85% accuracy on subscription prediction
- Feature importance rankings and business insights
- Customer segmentation strategy based on ML clustering
- ROI analysis comparing ML-targeted vs. traditional campaigns
- Production-ready prediction API with documentation
- Model performance dashboard with real-time monitoring

## Analysis Results & Key Findings

### Task 1 Completed: Exploratory Data Analysis & Customer Insights

**Key Business Insights:**

#### **Q1: Customer Demographics with Highest Conversion Rates**
- **Students**: 26.06% conversion rate (highest performing segment)
- **Age Factor**: 68-year-olds show 65.22% conversion rate
- **Strategic Recommendation**: Target student segment and senior demographics for maximum ROI

#### **Q2: Contact Duration & Campaign Frequency Correlation**
- **Duration Impact**: Strong positive correlation (0.258) with subscription probability
- **Campaign Frequency**: Negative correlation (-0.089) - fewer contacts yield better results
- **Insight**: Quality over quantity approach recommended

#### **Q3: Optimal Contact Timing**
- **Best Month**: May (384 conversions)
- **Best Day**: 30th of month (146 conversions)
- **Seasonal Strategy**: Focus campaigns in May, August, April for peak performance

#### **Q4: Economic Indicators Impact**
- **Optimal Balance Range**: £3,116 - £4,116 (18.8% conversion rate)
- **Credit Status**: Non-defaulting customers convert at 8.39% (8× higher than defaulters)
- **Debt Impact**: Debt-free customers show 44% higher conversion potential
- **Housing Loans**: Customers without housing loans convert at 13.38%

#### **Q5: Communication Channel Effectiveness**
- **Cellular**: 11.41% conversion rate (optimal channel)
- **Strategic Focus**: Prioritize cellular communication for customer outreach

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

##  Deliverables

### 1. Technical Analysis
- **EDA Notebook** - Comprehensive exploratory data analysis
- **SQL Queries** - Customer segmentation and cohort analysis
- **Statistical Models** - A/B testing frameworks and simulations
- **Visualization Suite** - Interactive charts and dashboards

### 2. Code Implementation
- **`ab_test_simulator.py`** - Monte Carlo simulation engine
- **`statistical_analysis.py`** - Power analysis and corrections
- **`bayesian_ab_testing.py`** - Bayesian testing framework
- **`dashboard/streamlit_app.py`** - Interactive web application
- **`sql/queries.sql`** - Optimized database queries

### 3. Interactive Dashboard Features
- **Test Designer** - Configure A/B tests with custom parameters
- **Monte Carlo Simulator** - Real-time simulation results
- **Power Calculator** - Optimal sample size determination
- **Results Analyzer** - Statistical significance testing
- **Business Impact Calculator** - Revenue projections and ROI
- **Multi-Armed Bandit Simulator** - Advanced allocation strategies

### 4. Documentation
- **Technical Report (PDF)** - Methodology and findings
- **Business Strategy Report** - Implementation roadmap
- **API Documentation** - Code usage and examples

## Results

### Key Findings
- **Optimal Contact Strategy** - Best timing and channel combinations
- **Customer Segmentation** - High-value target demographics
- **Campaign Optimization** - Data-driven improvement recommendations
- **Statistical Framework** - Robust A/B testing methodology

### Business Impact
- **Conversion Rate Improvemen2. **Create virtual environment:**
   ```bash
   python -m venv venv
- **Cost Optimization** - Reduced campaign costs through better targeting
- **Revenue Growth** - Estimated financial impact of optimizations
- **Testing Infrastructure** - Scalable framework for future experiments

### Statistical Analysis Pipeline
- **Power Analysis** - Calculate required sample sizes
- **P-value Distribution** - Visualize significance patterns
- **Multiple Testing Corrections** - Control error rates
- **Confidence Intervals** - Show uncertainty estimates
- **Bayesian Analysis** - Alternative inference methods

## Skills Demonstrated

### Technical Skills
- **Advanced Statistics** - Monte Carlo methods, power analysis, Bayesian inference
- **Python Development** - Object-oriented design, statistical libraries
- **Data Visualization** - Interactive dashboards and statistical plots
- **SQL Optimization** - Efficient queries and data engineering
- **Web Development** - Streamlit applications and real-time updates

### Business Skills
- **A/B Testing Strategy** - Experimental design and interpretation
- **ROI Analysis** - Business impact measurement
- **Campaign Optimization** - Data-driven marketing decisions
- **Growth Strategy** - Systematic experimentation framework



