import pandas as pd
from textblob import TextBlob
import os
import nltk

# Download necessary NLTK data
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)

# Create outputs directory
os.makedirs("outputs", exist_ok=True)

# Load feedback data
feedback = pd.read_csv("data/synthetic_feedback.csv")

def get_sentiment_score(text):
    return TextBlob(str(text)).sentiment.polarity

def get_sentiment_label(score):
    if score > 0.1:
        return "Positive"
    elif score < -0.1:
        return "Negative"
    return "Neutral"

def detect_theme(text):
    text = str(text).lower()
    if any(word in text for word in ["salary", "underpaid", "pay", "compensation"]):
        return "Salary"
    elif any(word in text for word in ["manager", "management", "leader", "micromanagement"]):
        return "Management"
    elif any(word in text for word in ["balance", "workload", "stress", "hours"]):
        return "Work-Life Balance"
    elif any(word in text for word in ["promotion", "growth", "career"]):
        return "Career Growth"
    elif any(word in text for word in ["transfer", "department", "role"]):
        return "Internal Mobility"
    return "Other"

# Apply NLP transformations
feedback["sentiment_score"] = feedback["FeedbackText"].apply(get_sentiment_score)
feedback["sentiment_label"] = feedback["sentiment_score"].apply(get_sentiment_label)
feedback["theme"] = feedback["FeedbackText"].apply(detect_theme)

# Save results
feedback.to_csv("outputs/feedback_with_sentiment.csv", index=False)

print("NLP analysis complete.")
print("Results saved to 'outputs/feedback_with_sentiment.csv'.")
