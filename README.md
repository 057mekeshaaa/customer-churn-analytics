# Telco Customer Churn Analytics & ML Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![License-MIT](https://img.shields.io/badge/License-MIT-green)

---

## Key Results
* **Machine Learning Performance:** I achieved **79% accuracy** and an **82.5% ROC-AUC** score.
* **SQL Key Drivers:** I identified month-to-month contracts (**42.7% churn rate**) and higher monthly charges as the primary drivers of customer attrition.

---

## Visual Dashboard
![Churn Analysis Visualisations](churn_analysis_plots.png)

---

## Project Architecture
* **Data Ingestion & SQL:** I imported raw Telco CSV data into a local SQLite database and ran aggregate queries to find baseline churn rates across demographics.
* **Exploratory Data Analysis (EDA):** I used Pandas and Matplotlib/Seaborn to visualise correlations (e.g., tenure length vs. churn probability).
* **Data Preprocessing:** I handled missing values, applied One-Hot Encoding for categorical variables, and scaled numerical features.
* **Machine Learning:** I trained a Random Forest Classifier, evaluating my model's performance using Accuracy, Precision, Recall, and ROC-AUC.

## Repository Structure
* `data/` - Raw and processed datasets
* `README.md` - Project documentation
* `churn_analysis_plots.png` - Dashboard visualisations

## How to Run
To run this project locally:
1. Clone the repository: `git clone https://github.com/057mekeshaaa/customer-churn-analytics.git`

## Business Recommendations
Based on my model's findings, the business should:
1. Incentivise customers to switch from month-to-month to 1-year or 2-year contracts by offering a small discount.
2. Investigate the services tied to higher monthly charges, as these customers are at the highest risk of leaving.