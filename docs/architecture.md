# Architecture Overview

## System Context
The SecureFair AI system ingests HR database records and employee textual feedback, processes them individually, merges the features, and trains a predictive model under strict fairness constraints. A web dashboard then exposes these predictions to HR professionals with Explainable AI overlays.

## Component Flow

```mermaid
graph TD
    A1[(Raw HR Data)] --> B[Preprocessing Anonymization]
    A2[(Text Feedback)] --> C[NLP Sentiment Analysis]
    
    B --> D[Data Merging Module]
    C --> D
    
    D --> E[(Clean Merged Dataset)]
    
    E --> F[Model Training RF]
    F --> G(Trained Model model.pkl)
    
    G --> H[Streamlit UI & API]
    E --> H
    
    H --> I[HR End User Persona]
    
    style B fill:#f9f,stroke:#333,stroke-width:2px;
    style C fill:#bbf,stroke:#333,stroke-width:2px;
    style F fill:#bfb,stroke:#333,stroke-width:2px;
    style H fill:#fbb,stroke:#333,stroke-width:2px;
```

## Security & Privacy Boundary
1. **PII Removal Layer**: `preprocess.py` physically separates names, birthdates, and zip codes before data ever touches the training pipeline.
2. **Fairness Isolation**: Protected attributes (e.g., race, gender) never enter the feature vector feeding the model. They are only utilized post-prediction for fairness auditing within the dashboard.
