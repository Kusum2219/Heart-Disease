# Heart Health Classifier

A machine learning project that classifies reported history of heart attack or coronary heart disease using CDC BRFSS 2023 survey data. It includes a CatBoost model, Flask prediction API, and Streamlit user interface.

> **Disclaimer:** This is an educational classification project, not a medical diagnosis or a clinically validated estimate of future heart disease risk.

## Project Overview

The project explores associations between demographic characteristics, health conditions, and lifestyle survey responses and a reported history of heart attack or coronary heart disease.

The workflow includes data preparation, categorical feature handling, CatBoost training, threshold-based classification, model evaluation, and an interactive prediction interface.

## Dataset

- **Source:** CDC Behavioral Risk Factor Surveillance System (BRFSS), 2023
- **Original records:** 433,323
- **Records with known target labels:** 428,738
- **Target:** Binary classification
- **Final model inputs:** 14 categorical features

### Target Definition

- `1`: Respondent reported a history of heart attack or coronary heart disease.
- `0`: Respondent reported neither condition.
- Records without a known target label were excluded.

The model classifies reported history; it does not predict future heart attacks.

## Features

The model uses these 14 features:

| Feature | Description |
|---|---|
| `SEXVAR` | Sex recorded in survey |
| `_AGEG5YR` | Age group |
| `BPHIGH6` | High blood pressure history |
| `TOLDHI3` | High cholesterol history |
| `DIABETE4` | Diabetes status |
| `_BMI5CAT` | BMI category |
| `PHYSHLTH` | Number of physically unhealthy days |
| `MENTHLTH` | Number of mentally unhealthy days |
| `GENHLTH` | General health status |
| `DIFFWALK` | Difficulty walking or climbing stairs |
| `SMOKE100` | Lifetime smoking history |
| `SMOKDAY2` | Current smoking frequency |
| `EXERANY2` | Physical activity outside regular work |
| `CHCKDNY2` | Kidney disease history |

`SLEPTIM1` was excluded because it was unavailable for the final feature set.

## Tech Stack

- **Language:** Python
- **Model:** CatBoost Classifier
- **Data processing:** Pandas, NumPy
- **Evaluation:** Scikit-learn
- **Backend:** Flask, Flask-CORS
- **Frontend:** Streamlit
- **Development:** Google Colab, VS Code

## Model and Evaluation

- **Algorithm:** CatBoost Classifier
- **Input features:** 14
- **Classification threshold:** 0.20
- **Evaluation:** Held-out test set
- **Metrics:** Accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix

### Reported Test Results

| Metric | Score |
|---|---:|
| Accuracy | 86.41% |
| Precision | 31.78% |
| Recall | 52.70% |
| F1-score | 39.65% |
| ROC-AUC | 84.40% |

Confusion matrix at the 0.20 threshold:

| | Predicted Negative | Predicted Positive |
|---|---:|---:|
| Actual Negative | 70,269 | 8,217 |
| Actual Positive | 3,435 | 3,827 |

These are experimental results on the held-out test set. Precision, recall, and the confusion matrix depend on the selected threshold. The model has not been clinically validated.

## Project Structure

```text
heart-disease-prediction/
├── backend/
│   ├── app.py
│   └── models/
│       ├── heart_disease_catboost_14_features.cbm
│       ├── best_threshold_14.pkl
│       └── feature_names_14.pkl
├── frontend/
│   └── app.py
├── .gitignore
└── README.md
```

Other supporting files may exist in the local development environment.

## Setup and Run Locally

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install catboost pandas numpy scikit-learn flask flask-cors streamlit requests
```

### 3. Start the Flask backend

Open a terminal in the project root:

```powershell
python .\backend\app.py
```

The API runs at `http://127.0.0.1:5000`.

Health check: `http://127.0.0.1:5000/health`

### 4. Start the Streamlit frontend

Open a second terminal in the project root, activate the virtual environment, and run:

```powershell
python -m streamlit run .\frontend\app.py
```

Streamlit will display the local URL in the terminal, usually `http://localhost:8501`.

Keep the backend running while using the frontend.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Check API and model status |
| POST | `/predict` | Classify a survey response |

The prediction endpoint expects all 14 feature values in JSON format, using the same categorical encodings and preprocessing as the training data.

## Limitations

- Survey responses may contain reporting errors.
- Class imbalance affects model metrics.
- The 0.20 threshold changes the balance between false positives and false negatives.
- Results may not generalize to other populations or datasets.
- This model is not a clinically validated diagnostic or future-risk prediction tool.

## Future Improvements

- Validate feature encodings against the official survey codebook.
- Evaluate threshold selection on validation data separately from the final test set.
- Add model explainability and feature-importance analysis.
- Add automated API tests and input validation.
- Deploy the frontend and backend for public demonstration.

## Disclaimer

For educational and research purposes only. This project must not be used for diagnosis, treatment, or healthcare decisions.

## Author

**Kusum Thakur**

GitHub: [@Kusum2219](https://github.com/Kusum2219)
