# Technical Documentation (TECH_DOC)

## 1. System Overview
SecureFair AI is a machine learning pipeline and interactive dashboard designed to predict employee resignation risk while enforcing strict privacy and fairness standards. The backend relies on Python and Scikit-learn, while the frontend utilizes Streamlit for interactive presentation and SHAP for explainable AI.

## 2. Technical Stack
- **Language**: Python 3.10+
- **Data Manipulation**: `pandas`, `numpy`
- **Machine Learning**: `scikit-learn` (RandomForestClassifier)
- **NLP**: `textblob` (Sentiment Analysis)
- **Explainability**: `shap`
- **Frontend / Dashboard**: `streamlit`, `matplotlib`, `seaborn`

## 3. Data Pipeline
The pipeline is broken down into modular steps located in the `src/` directory.

### 3.1 Preprocessing (`src/preprocess.py`)
- **Data Ingestion**: Loads the structured HR dataset (`HRDataset_v14.csv`).
- **Anonymization**: Drops Direct Identifiers (DIs) such as `Employee_Name`, `DOB`, and `Zip`.
- **Fairness Isolation**: Sensitive attributes (`Sex`, `RaceDesc`) are intentionally removed from the feature set to avoid training biased models.
- **Leakage Prevention**: Drops variables intrinsically linked to the target (e.g., `TermReason`, `DateofTermination`).
- **Missing Values & Encoding**: Fills missing values appropriately and one-hot encodes categorical variables (e.g., `Department`, `MaritalDesc`).
- **Output**: Saves `cleaned_hr_data.csv`.

### 3.2 NLP Analysis (`src/nlp_analysis.py`)
- **Text Processing**: Analyzes raw employee feedback text.
- **Sentiment Extraction**: Uses `TextBlob` to compute a polarity score ranging from -1 (Negative) to 1 (Positive).
- **Theme Extraction**: A basic keyword-matching algorithm tags feedback with categories (e.g., "Salary", "Management", "Work-Life Balance").
- **Output**: Generates `feedback_processed.csv`.

### 3.3 Data Merging (`src/merge_data.py`)
- Combines the structure HR data (`cleaned_hr_data.csv`) with the processed feedback (`feedback_processed.csv`) using `EmpID`.
- Fills in default neutral sentiment scores for employees lacking textual feedback.
- **Output**: Creates `final_merged_data.csv`, which serves as the direct input for model training.

## 4. Model Training & Evaluation (`src/train_model.py`)
- **Algorithm**: `RandomForestClassifier` chosen for its robustness and ease of interpretation.
- **Splitting**: 80/20 Train-Test split.
- **Training**: Fits the model on non-sensitive features to predict `Termd` (1 = Terminated, 0 = Active).
- **Evaluation**: Logs Accuracy, Classification Report, and ROC-AUC.
- **Artifacts Saved**: 
  - `model.pkl`: The serialized Random Forest model.
  - `X_test.csv` & `y_test.csv`: Reserved data for evaluation and dashboard explainability.
  - `feature_names.pkl`: Ordered list of columns the model expects.

## 5. Fairness & Explainability Dashboard (`src/app.py`)
- **Interactive UI**: Built with Streamlit, enabling HR users to query individual risk profiles without touching code.
- **Global Explanation**: Uses SHAP Summary Plots to demonstrate which features globally push risk higher or lower.
- **Local Explanation**: Allows selecting a specific employee (via a mock ID) to see a SHAP Waterfall or Force Plot, illustrating exactly *why* a certain resignation probability was assigned.
- **Fairness Audit Panel**: Compares prediction distribution across synthetically rejoined sensitive groups to demonstrate compliance.
