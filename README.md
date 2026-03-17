# SecureFair AI 🛡️
**AI-Powered Ethical HR Decision Assistant**

## The Product Vision
SecureFair AI is not just another predictive model. It is a comprehensive **AI-powered ethical HR decision assistant**. 
We don’t replace HR decisions; we augment them with ethical, explainable AI. By predicting resignation risks through both quantified metrics and unquantified textual feedback, we empower Human Resources to move from reactive attrition management to proactive talent retention.

## Core Value Highlights
- **Explainability (SHAP)**: We crack the black box open. Every risk score is accompanied by transparent, human-readable rationales.
- **Fairness & EU AI Act Compliance**: Built for the High-Risk AI sector. Protected classes (Gender, Ethnicity) are structurally isolated from training to avoid structural bias. Live fairness audits run concurrently.
- **Frugal AI**: We favor highly optimized Random Forests over resource-draining, massive LLMs, meaning the AI is lightning-fast, cheap to run, and environmentally responsible.
- **Cybersecurity Built-In**: Features input sanitization against prompt injection, and rigorous pre-pipeline PII anonymization for GDPR adherence.

## Architecture

```text
          HR DATA (Structured + Text)
                     │
                     ▼
        GDPR Anonymization Layer
                     │
                     ▼
            Secure Data Storage
                     │
        ┌────────────┴────────────┐
        ▼                         ▼
 ML Prediction Model        NLP Engine
 (Turnover Risk)         (Sentiment + Topics)
        │                         │
        └────────────┬────────────┘
                     ▼
           Explainability Layer (SHAP)
                     │
                     ▼
              Fairness Audit (AIF360-style)
                     │
                     ▼
          SecureFair Dashboard (UI)
```

## System Scope & Persona
- **Primary Persona**: HR Managers / Talent Retention Specialists seeking an intelligent dashboard.
- **In Scope**: A combined quantitative/NLP risk likelihood score, explainable outcomes, UI-based fairness monitoring, security input validation.
- **Out of Scope**: Automated firing, automated promotions. This tool requires human oversight.

## Project Structure
- `data/`: Raw HR and Feedback datasets.
- `src/`: Core logic (Preprocessing, NLP, Training, Fairness, Dashboard).
- `outputs/`: Cleaned data, trained model binaries, plots.
- `docs/`: Technical, architecture, AI Act Model Card, Executive Summary, Pitch Slides.

## Installation & Instructions
1. **Requirements**: `pip install -r requirements.txt`
2. **Setup**: `python src/preprocess.py`
3. **Analyze**: `python src/nlp_analysis.py`
4. **Merge**: `python src/merge_data.py`
5. **Train**: `python src/train_model.py`
6. **Dashboard**: `streamlit run src/app.py`

---
*Developed for the AI Hackathon 2026.*
