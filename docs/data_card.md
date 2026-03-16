# Data Card - HR Resignation Dataset

## Dataset Description
This dataset is a combination of structured HR records and synthetic employee feedback text.

## Size
- HR Data: 311 employees (demonstration uses 10 sample records).
- Feedback: 10 synthetic text feedback records.

## Target Column
- **Termd**:
  - `0`: Active employee.
  - `1`: Left the company.

## Sensitive Attributes (Isolated for Audit)
- **Sex**: Gender.
- **RaceDesc**: Ethnicity.

## Personal Identifiers (Anonymized)
- `Employee_Name` (Removed)
- `DOB` (Removed)
- `Zip` (Removed)

## Preprocessing & Security
- All direct identifiers were removed before any analysis.
- Sensitive attributes were excluded from the training set to prevent structural bias.
- Leakage columns like `TermReason` and `DateofTermination` were removed.
- categorical variables were one-hot encoded.

## Merged Features
- **sentiment_score**: Polarity derived from feedback text using NLP.
- **theme**: Categorical theme identified from feedback (e.g., Salary, Work-Life Balance).

## Risks & Limitations
- **Small Pilot Scale**: Currently based on a synthetic demonstration subset.
- **Bias**: While sensitive attributes are removed, proxy variables might still exist. Continuous auditing is required.
- **Privacy**: NLP feedback should be handled carefully to avoid identity inference through text.
