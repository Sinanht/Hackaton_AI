# SecureFair AI 🛡️
**Ethical & Secure AI for Employee Resignation Prediction**

## Problem
HR teams want to identify employees at risk of leaving to take proactive measures and improve retention.

## Objective
The primary objective is to empower HR departments to predict employee resignation risks early, combining both structured HR metrics (salary, satisfaction, engagement) and unstructured employee feedback seamlessly evaluated via NLP sentiment analysis, ultimately reducing turnover and maintaining a healthy work environment.

## Persona
- **Primary User**: HR Managers / Talent Retention Specialists.
- **Secondary User**: Department Heads looking to monitor their team's well-being.
- **Technical User**: Data Scientists & ML Engineers responsible for ensuring model fairness and accuracy.

## Scope
- **In Scope**: Predicting the likelihood of an employee leaving based on historical records and feedback. Providing explainable AI (XAI) outputs to HR. Ensuring fairness across sensitive attributes.
- **Out of Scope**: Automated firing/hiring systems. Replacing human HR interactions. Full-scale enterprise integrations (this is an MVP approach).

## Key Features
- **Privacy by Design**: Personal identifiers (Names, DOB, Zip) are removed during preprocessing.
- **Fairness Audit**: Sensitive features (Gender, Race) are isolated and excluded from training.
- **Explainable AI**: Integrated SHAP summary plots for transparent model insights.
- **NLP Integration**: Sentiment and theme extracted from feedback for richer predictions.
- **Web Dashboard**: Interactive Streamlit app for real-time risk assessment.

## Project Structure
- `data/`: Raw HR and Feedback datasets.
- `src/`: Core logic (Preprocessing, NLP, Training, Fairness, App).
- `outputs/`: Cleaned data, trained model, and results/plots.
- `docs/`: Responsible AI documentation (Data Card, Model Card).

## Instructions (Installation & Usage)
1. **Requirements**: `pip install -r requirements.txt`
2. **Setup**: `python src/preprocess.py`
3. **Analyze**: `python src/nlp_analysis.py`
4. **Merge**: `python src/merge_data.py`
5. **Train**: `python src/train_model.py`
6. **Dashboard**: `streamlit run src/app.py`

## Responsible AI Section
- **Security**: GDPR-aware anonymization protocol.
- **Fairness**: Structural exclusion of protected classes + prediction rate audit.
- **Explainability**: SHAP value interpretation for every prediction.

---
*Built for the Hackathon AI Project 2026.*
