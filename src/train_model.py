import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score

# Create directories for outputs
os.makedirs("outputs/plots", exist_ok=True)

# Load final dataset (HR + Feedback)
df = pd.read_csv("outputs/final_dataset.csv")

# Set target and features
y = df["Termd"]
# Drop target and any ID columns not useful for training
X = df.drop(columns=["Termd"])
# Drop ID columns that shouldn't be in the model
for id_col in ["EmpID", "Employee_ID"]:
    if id_col in X.columns:
        X = X.drop(columns=[id_col])

# One-hot encoding for categorical variables
X_encoded = pd.get_dummies(X, drop_first=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42, stratify=y
)

# Initialize and train Random Forest (V2 Upgrade)
rf = RandomForestClassifier(
    n_estimators=300,
    max_depth=8,
    class_weight="balanced",
    random_state=42
)
rf.fit(X_train, y_train)

# Predictions
pred = rf.predict(X_test)
prob = rf.predict_proba(X_test)[:, 1]

# Evaluation
print("Accuracy:", accuracy_score(y_test, pred))
print("ROC-AUC:", roc_auc_score(y_test, prob))
print(classification_report(y_test, pred))

# Save model and columns
joblib.dump(rf, "outputs/model.pkl")
joblib.dump(X_encoded.columns.tolist(), "outputs/model_columns.pkl")

# Save test results for fairness step
test_results = X_test.copy()
test_results["y_true"] = y_test.values
test_results["y_pred"] = pred
test_results["y_prob"] = prob
test_results.to_csv("outputs/test_predictions.csv", index=False)

print("Model training complete.")

# Step 10: Feature Importance Plot
feature_importance = pd.Series(rf.feature_importances_, index=X_encoded.columns).sort_values(ascending=False).head(10)

plt.figure(figsize=(8, 5))
feature_importance.sort_values().plot(kind="barh")
plt.title("Top 10 Features for Resignation Prediction")
plt.tight_layout()
plt.savefig("outputs/plots/top_features.png")
print("Feature importance chart saved to 'outputs/plots/top_features.png'.")
