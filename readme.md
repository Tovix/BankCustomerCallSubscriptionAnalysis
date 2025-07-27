# 🧪 Digital Marketing A/B Test Optimization Platform

> A comprehensive data science project focused on optimizing marketing campaigns through advanced A/B testing methodologies and statistical analysis.

[![Dataset](https://img.shields.io/badge/Dataset-UCI%20ML%20Repository-blue)](https://archive.ics.uci.edu/dataset/222/bank+marketing)
[![Domain](https://img.shields.io/badge/Domain-Digital%20Marketing-green)](#)
[![Analytics](https://img.shields.io/badge/Analytics-Campaign%20Optimization-orange)](#)

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [Analysis Tasks](#analysis-tasks)
- [Deliverables](#deliverables)
- [Results](#results)
- [Contributing](#contributing)

## Overview

This project leverages the Bank Marketing Dataset to build a comprehensive A/B testing optimization platform for digital marketing campaigns. Using advanced statistical methods, Monte Carlo simulations, and machine learning techniques, we analyze customer behavior patterns and optimize marketing strategies for maximum conversion rates.

**Key Objectives:**
- Identify optimal customer targeting strategies
- Develop statistical frameworks for A/B testing
- Build predictive models for campaign success
- Create interactive dashboards for campaign analysis

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
├── data/
│   ├── raw/                    # Original dataset
│   ├── processed/              # Cleaned and preprocessed data
│   └── external/               # Additional data sources
├── notebooks/
│   ├── 01_eda.ipynb           # Exploratory Data Analysis
│   ├── 02_statistical_analysis.ipynb
│   └── 03_ab_testing.ipynb    # A/B Testing Analysis
├── src/
│   ├── ab_test_simulator.py    # Monte Carlo simulation engine
│   ├── statistical_analysis.py # Power analysis & corrections
│   ├── bayesian_ab_testing.py  # Bayesian A/B testing
│   └── utils/                  # Helper functions
├── sql/
│   └── queries.sql            # Customer segmentation queries
├── dashboard/
│   └── streamlit_app.py       # Interactive dashboard
├── reports/
│   └── technical_report.pdf   # Comprehensive analysis
├── requirements.txt
└── README.md
```

## Key Features

### Advanced A/B Testing
- **Monte Carlo Simulation Engine** - Generate thousands of test scenarios
- **Statistical Power Analysis** - Calculate optimal sample sizes
- **Multiple Testing Correction** - Bonferroni and FDR implementations
- **Sequential Testing** - Early stopping rules and adaptive sizing
- **Bayesian A/B Testing** - Credible intervals and posterior analysis

### Campaign Analytics
- Customer segmentation and targeting
- Conversion rate optimization
- Economic indicator impact analysis
- Contact timing optimization
- Channel effectiveness analysis

### Interactive Dashboard
- Real-time A/B test configuration
- Monte Carlo simulation results
- Power calculation tools
- Statistical significance testing
- Business impact projections

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/BankCustomerCallSubscriptionAnalysis.git
   cd BankCustomerCallSubscriptionAnalysis
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download dataset:**
   ```bash
   # Dataset will be automatically downloaded on first run
   python src/data_loader.py
   ```

## Usage

### Quick Start

```python
from src.ab_test_simulator import ABTestSimulator
from src.statistical_analysis import PowerAnalysis

# Initialize A/B test simulator
simulator = ABTestSimulator()

# Run Monte Carlo simulation
results = simulator.run_simulation(
    baseline_rate=0.11,
    effect_size=0.02,
    sample_size=1000,
    n_simulations=10000
)

# Calculate required sample size
power_calc = PowerAnalysis()
sample_size = power_calc.calculate_sample_size(
    baseline_rate=0.11,
    minimum_effect=0.02,
    power=0.8,
    alpha=0.05
)
```

### Launch Dashboard

```bash
streamlit run dashboard/streamlit_app.py
```

### Run Analysis Notebooks

```bash
jupyter notebook notebooks/
```
## Analysis Tasks

### Task 1: Exploratory Data Analysis & Customer Insights 
**Objective:** Explore customer behavior patterns and identify marketing campaign optimization opportunities.

**Key Questions:**
- Which customer demographics show the highest conversion rates?
- How do contact duration and campaign frequency correlate with subscription probability?
- What is the optimal contact timing for maximizing conversions?
- Which communication channels yield the best response rates?
- How do economic indicators affect campaign success?

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
- **Conversion Rate Improvement** - Projected increase in subscription rates
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



