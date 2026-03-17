# SecureFair AI - Hackathon Demo Script (10 Mins Max)

## Setting the Stage (1 min)
- **Goal**: Hook the audience and introduce the problem.
- **Talking Points**: "Employee turnover costs companies thousands per person. HR teams often find out too late. What if we could predict resignation risk *before* it happens, but do so ethically, without structural bias?"

## The Technology & Pipeline (2 mins)
- **Goal**: Briefly explain the backend without getting bogged down in code.
- **Talking Points**: "We used a Random Forest model. Our data comes from two sources: structured HR metrics (salary, satisfaction) and unstructured text (employee feedback). We run NLP sentiment analysis on the text to give it a polarity score. Crucially, we strip out all identifying information and isolate protected attributes (Race, Gender) so our model doesn't learn human biases."

## Interactive Dashboard Tour (4 mins)
- **Action**: Open the Streamlit App (`streamlit run src/app.py`).
- **Step 1 - Global View**: Show the SHAP Summary plot. 
  - *Talking Point*: "Here we see what generally drives people to leave—often, low sentiment scores or low salary."
- **Step 2 - Individual Prediction**: Select a mock employee ID from the sidebar.
  - *Talking Point*: "Let's look at Employee 1005. The model predicts a 75% chance of resignation. Why? The SHAP Force Plot shows us exactly what factors pushed that score up (e.g., negative feedback theme) and what pushed it down (e.g., decent salary)."

## Responsible AI & Fairness Audit (2 mins)
- **Action**: Scroll to the Fairness / Disparity section of the Dashboard.
- **Talking Points**: "Predicting human behavior is dangerous if not done fairly. We explicitly removed Gender and Race from training. Post-prediction, we audit the results. As you can see on this chart, the average predicted risk for men vs. women is within a tight, acceptable margin. We aren't penalizing a protected class."

## Conclusion & Future Vision (1 min)
- **Goal**: Wrap up and show business value.
- **Talking Points**: "SecureFair AI provides HR with proactive, explainable, and ethical insights. For next steps, we want to integrate with live HR systems (like Workday) and allow real-time feedback ingestion."
