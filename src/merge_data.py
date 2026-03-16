import pandas as pd
import os

# Load data
hr = pd.read_csv("outputs/cleaned_data.csv")
feedback = pd.read_csv("outputs/feedback_with_sentiment.csv")

# Merge on EmpID/Employee_ID
# Note: In my HR data EmpID is used, in Feedback Employee_ID is used.
merged = hr.merge(
    feedback[["Employee_ID", "sentiment_score", "sentiment_label", "theme"]],
    left_on="EmpID",
    right_on="Employee_ID",
    how="left"
)

# Fill missing feedback data for employees without feedback
merged["sentiment_score"] = merged["sentiment_score"].fillna(0)
merged["sentiment_label"] = merged["sentiment_label"].fillna("Neutral")
merged["theme"] = merged["theme"].fillna("Other")

# Save merged dataset
merged.to_csv("outputs/final_dataset.csv", index=False)
print("Merged dataset saved to 'outputs/final_dataset.csv'.")
print("Merged shape:", merged.shape)
