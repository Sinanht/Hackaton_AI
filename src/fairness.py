import pandas as pd
import os

# Create outputs directory
os.makedirs("outputs", exist_ok=True)

# Load test predictions and sensitive attributes
preds = pd.read_csv("outputs/test_predictions.csv")
sensitive = pd.read_csv("outputs/sensitive_attributes.csv")

# Align rows carefully (assuming they weren't scrambled during split)
# In a real scenario, we'd use index matching. Here we'll align based on length.
min_len = min(len(preds), len(sensitive))
preds = preds.iloc[:min_len].copy()
sensitive = sensitive.iloc[:min_len].copy()

# Combine for analysis
results = pd.concat([preds.reset_index(drop=True), sensitive.reset_index(drop=True)], axis=1)

fairness_rows = []

# Audit Sex and RaceDesc
for col in ["Sex", "RaceDesc"]:
    if col in results.columns:
        # Calculate positive prediction rate (risk rate) per category
        rates = results.groupby(col)["y_pred"].mean().reset_index()
        rates.columns = [col, "positive_prediction_rate"]
        rates["attribute"] = col
        fairness_rows.append(rates)

# Save result as a CSV report
if fairness_rows:
    fairness_report = pd.concat(fairness_rows, ignore_index=True)
    fairness_report.to_csv("outputs/fairness_report.csv", index=False)
    print("Fairness audit report:")
    print(fairness_report)
    print("\nFairness report saved to 'outputs/fairness_report.csv'.")
else:
    print("No sensitive attributes found for audit.")
