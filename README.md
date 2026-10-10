# Heart Disease Prediction Using Machine Learning

A machine learning project that predicts the likelihood of heart disease based on clinical and health-related attributes. The project includes data preprocessing, exploratory data analysis, model comparison, evaluation, and an interactive Streamlit application.

## Overview

Heart disease is a major global health concern. This project explores how machine learning classification algorithms can identify patterns in clinical data and estimate the likelihood of heart disease.

The goal is to build and evaluate predictive models while understanding their strengths and limitations.

## Features

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature analysis and visualization
- Machine learning model training and comparison
- Evaluation using accuracy, precision, recall, F1-score, and confusion matrix
- Interactive prediction interface using Streamlit
- Saved trained model for inference

## Tech Stack

- **Language:** Python
- **Environment:** Google Colab
- **Data Analysis:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Visualization:** Matplotlib
- **Web Application:** Streamlit
- **Model Persistence:** Pickle

## Dataset

The project uses a cleaned, UCI-derived heart disease dataset.

- **Records:** 302
- **Input features:** 13
- **Target:** Binary classification
- **Class distribution:** 164 positive and 138 negative samples

### Features Used

| Feature | Description |
|---|---|
| `age` | Age of the individual |
| `sex` | Sex category encoded in the dataset |
| `cp` | Chest pain type |
| `trestbps` | Resting blood pressure |
| `chol` | Serum cholesterol |
| `fbs` | Fasting blood sugar indicator |
| `restecg` | Resting electrocardiographic results |
| `thalach` | Maximum heart rate achieved |
| `exang` | Exercise-induced angina indicator |
| `oldpeak` | ST depression induced by exercise |
| `slope` | Slope of the peak exercise ST segment |
| `ca` | Number of major vessels |
| `thal` | Thalassemia-related category |
| `target` | Target class |

The exact feature encoding and target labels depend on the dataset version used.

## Machine Learning Models

The following classification algorithms were evaluated:

- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest

### Model Evaluation Results

Results from the current 80:20 train-test split:

| Model | Test Accuracy | Heart Disease Recall |
|---|---:|---:|
| Logistic Regression | 80.33% | 84.85% |
| SVM | 77.05% | 81.82% |
| Random Forest | 75.41% | 78.79% |

Cross-validation accuracy:

| Model | Cross-Validation Accuracy |
|---|---:|
| Logistic Regression | 83.79% |
| SVM | 85.04% |
| Random Forest | 84.63% |

Logistic Regression achieved the highest test accuracy among these models, while SVM achieved the highest average cross-validation accuracy. Model selection should consider multiple evaluation metrics rather than accuracy alone.

## Project Structure

```text
heart-disease-prediction/
├── app.py
├── heart_disease_prediction.ipynb
├── heart_disease_model.pkl
├── requirements.txt
├── heart.csv
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Kusum2219/heart-disease-prediction.git
cd heart-disease-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser. Enter the required clinical features to explore a model prediction.

**Note:** The repository must contain the listed files, and `requirements.txt` must include all dependencies used by the application.

## Evaluation Metrics

- **Accuracy:** Overall proportion of correct predictions.
- **Precision:** Proportion of positive predictions that are correct.
- **Recall:** Proportion of actual positive cases identified by the model.
- **F1-score:** Harmonic mean of precision and recall.
- **Confusion Matrix:** Breakdown of true and false predictions.
- **Cross-validation:** Assessment of model performance across multiple data splits.

## Limitations

- The dataset is relatively small and may not represent the broader population.
- Model performance can vary depending on the train-test split and dataset preprocessing.
- Predictions may be affected by data quality, feature encoding, and class distribution.
- The model is intended for educational and research purposes only.

## Future Improvements

- Evaluate additional classification algorithms, including gradient boosting.
- Improve model interpretability using feature importance and explainability techniques.
- Perform external validation on independent datasets.
- Add automated testing and model performance monitoring.
- Deploy the application using Streamlit Community Cloud.

## Disclaimer

This project is for educational and research purposes only. It is not a medical diagnostic tool and must not be used as a substitute for professional medical advice, diagnosis, or treatment.

## Author

**Kusum Thakur**

- GitHub: [@Kusum2219](https://github.com/Kusum2219)

---

If you find this project useful, consider giving the repository a star.
