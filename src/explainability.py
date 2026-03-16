import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt
import os

# Create plots directory
os.makedirs("outputs/plots", exist_ok=True)

# Load final dataset
df = pd.read_csv("outputs/final_dataset.csv")

# Prepare features (same as training)
y = df["Termd"]
X = df.drop(columns=["Termd"])
for id_col in ["EmpID", "Employee_ID"]:
    if id_col in X.columns:
        X = X.drop(columns=[id_col])

# One-hot encoding (must match training)
X_encoded = pd.get_dummies(X, drop_first=True)

# Load trained model
model = joblib.load("outputs/model.pkl")

# SHAP Explainability
print("Generating SHAP values...")
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_encoded)

# Handle different output formats of shap_values
# (For binary classification, shap_values is a list of [neg_class, pos_class] or just one array)
if isinstance(shap_values, list):
    # Select the positive class (class 1)
    values = shap_values[1]
else:
    values = shap_values

# Generate and save SHAP summary plot
plt.figure(figsize=(10, 6))
shap.summary_plot(values, X_encoded, show=False)
plt.tight_layout()
plt.savefig("outputs/plots/shap_summary.png")
print("SHAP summary plot saved to 'outputs/plots/shap_summary.png'.")
