import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from analysis import load_and_clean_data
df = load_and_clean_data("../data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.countplot(x="Contract", hue="Churn", data=df, ax=axes[0], palette="Set2")
axes[0].set_title("Customer Churn by Contract Type")
axes[0].set_xlabel("Contract Type")
axes[0].set_ylabel("Customer Count")
sns.kdeplot(data=df, x="MonthlyCharges", hue="Churn", common_norm=False, ax=axes[1], palette="Set2", fill=True)
axes[1].set_title("Monthly Charges Distribution by Churn")
axes[1].set_xlabel("Monthly Charges ($)")

plt.tight_layout()
plt.savefig("churn_analysis_plots.png")
print("Visualizations saved successfully as 'churn_analysis_plots.png'!")
plt.show()