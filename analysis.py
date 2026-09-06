import pandas as pd
import numpy as np


def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    if 'customerID' in df.columns:
        df = df.drop(columns=['customerID'])
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'].str.strip(), errors='coerce')
    df['TotalCharges'] = df['TotalCharges'].fillna(0)


    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    return df


if __name__ == "__main__":
    df = load_and_clean_data("WA_Fn-UseC_-Telco-Customer-Churn.csv")
    print("Cleaned Dataset Shape:", df.shape)
    print("Churn Distribution:\n", df['Churn'].value_counts())
    print("\nData Sample:\n", df.head())