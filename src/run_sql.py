import pandas as pd
import sqlite3
df = pd.read_csv("../data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
conn = sqlite3.connect(":memory:")
df.to_sql("telco_churn", conn, index=False, if_exists="replace")
with open("churn_analysis.sql", "r") as file:
    sql_script = file.read()
queries = sql_script.strip().split(";")
for i, query in enumerate(queries[:-1], 1):
    if query.strip():
        print(f"=== QUERY {i} RESULTS ===")
        result = pd.read_sql_query(query, conn)
        print(result)
        print("\n")