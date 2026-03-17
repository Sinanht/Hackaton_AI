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

def extract_themes(text):
    themes = []
    text_lower = str(text).lower()
    
    if "salary" in text_lower or "underpaid" in text_lower or "pay" in text_lower:
        themes.append("Salary issue")
    
    if "workload" in text_lower or "stress" in text_lower:
        themes.append("Workload")
        
    if "manager" in text_lower or "leader" in text_lower or "micromanagement" in text_lower:
        themes.append("Management")
        
    if "balance" in text_lower or "hours" in text_lower:
        themes.append("Work-life balance")
        
    if not themes:
        themes.append("Other")
        
    return ", ".join(themes)

# Apply NLP transformations
feedback["sentiment_score"] = feedback["FeedbackText"].apply(get_sentiment_score)
feedback["sentiment_label"] = feedback["sentiment_score"].apply(get_sentiment_label)
feedback["theme"] = feedback["FeedbackText"].apply(extract_themes)

# Save results
feedback.to_csv("outputs/feedback_with_sentiment.csv", index=False)

print("NLP analysis complete.")
print("Results saved to 'outputs/feedback_with_sentiment.csv'.")
