import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from analysis import load_and_clean_data
df = load_and_clean_data("../data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
X = df.drop(columns=['Churn'])
y = df['Churn']
X = pd.get_dummies(X, drop_first=True)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from analysis import load_and_clean_data
df = load_and_clean_data("../data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
X = df.drop(columns=['Churn'])
y = df['Churn']
X = pd.get_dummies(X, drop_first=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
model = RandomForestClassifier(
    n_estimators=150,
    max_depth=10,
    class_weight='balanced',  # Handles 73/27 class imbalance
    random_state=42
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

print("=== BALANCED MODEL CLASSIFICATION REPORT ===")
print(classification_report(y_test, y_pred))

print("=== ROC-AUC SCORE ===")
print(f"ROC-AUC: {roc_auc_score(y_test, y_proba):.4f}")