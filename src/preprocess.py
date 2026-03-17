import pandas as pd
import os

# Create outputs directory if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Load dataset
df = pd.read_csv("data/HRDataset_v14.csv")

# Keep sensitive attributes separately for fairness audit
sensitive_cols = [col for col in ["Sex", "RaceDesc"] if col in df.columns]
sensitive_df = df[sensitive_cols].copy()

# Remove direct personal identifiers
drop_cols = [col for col in ["Employee_Name", "DOB", "Zip"] if col in df.columns]
df = df.drop(columns=drop_cols)

# We only want the model to learn from features the user can control in the dashboard
dashboard_features = [
    "EmpID",                     # Needed for merge
    "Salary", 
    "EngagementSurvey", 
    "EmpSatisfaction", 
    "Absences", 
    "DaysLateLast30", 
    "SpecialProjectsCount",
    "Termd"                      # Target variable
]

# Keep only those columns if they exist
keep_cols = [c for c in dashboard_features if c in df.columns]
df = df[keep_cols]

# Fill missing values
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna("Unknown")
    else:
        df[col] = df[col].fillna(df[col].median())

# Save processed datasets
df.to_csv("outputs/cleaned_data.csv", index=False)
sensitive_df.to_csv("outputs/sensitive_attributes.csv", index=False)

print("Preprocessing complete.")
print("Cleaned dataset shape:", df.shape)
print("Files saved to 'outputs/'.")
