# Model Card - SecureFair Resignation Predictor

## Model Overview
The SecureFair Resignation Predictor is a Random Forest Classifier designed to provide decision support for HR teams to identify employees at risk of leaving.

## Model Details
- **Type**: Random Forest Classifier.
- **Version**: 1.0 (Hackathon MVP).
- **Libraries**: `scikit-learn`, `joblib`, `shap`.

## Inputs
- **Structured HR Data**: Salary, Engagement Survey, Satisfaction, Absences, Project Counts, Tardiness.
- **NLP Features**: Sentiment score and feedback themes.

## Excluded Features (Fairness by Design)
- **Sex** (Gender)
- **RaceDesc** (Ethnicity)

## Evaluation Metrics
- **Accuracy**: Measured on the test split.
- **ROC-AUC**: Probability-based performance.
- **Fairness Disparity**: Prediction rates audited across gender and race groups.

## Interpretability
- **SHAP (Shapley Additive Explanations)**: Used to generate summary plots showing the most influential risk factors.
- **Feature Importance**: Direct ranking of model feature weights.

## Limitations
- **Synthetic Data**: The model is trained on a synthetic dataset for demonstration.
- **Support Only**: This model is meant for decision support, not for automated hiring or firing decisions.
- **Human in the Loop**: HR oversight is mandatory for any intervention.
