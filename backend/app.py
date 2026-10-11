
from pathlib import Path
import pickle

import pandas as pd
from catboost import CatBoostClassifier
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"

MODEL_PATH = MODEL_DIR / "heart_disease_catboost_14_features.cbm"
THRESHOLD_PATH = MODEL_DIR / "best_threshold_14.pkl"
FEATURES_PATH = MODEL_DIR / "feature_names_14.pkl"

with open(THRESHOLD_PATH, "rb") as file:
    THRESHOLD = pickle.load(file)

with open(FEATURES_PATH, "rb") as file:
    FEATURES = pickle.load(file)

model = CatBoostClassifier()
model.load_model(str(MODEL_PATH))


@app.get("/health")
def health():
    return jsonify({
        "status": "healthy",
        "model_loaded": True,
        "feature_count": len(FEATURES),
        "feature_names": FEATURES,
        "threshold": THRESHOLD
    })


@app.post("/predict")
def predict():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Send a valid JSON object."}), 400

    missing = [feature for feature in FEATURES if feature not in data]
    if missing:
        return jsonify({
            "error": "Missing required features.",
            "missing_features": missing
        }), 400

    # Validate and preserve categorical values as strings.
    row = {}
    for feature in FEATURES:
        value = data[feature]

        if value is None or isinstance(value, (dict, list, bool)):
            return jsonify({
                "error": f"Invalid value for {feature}."
            }), 400

        row[feature] = str(value)

    input_df = pd.DataFrame([row], columns=FEATURES)

    try:
        probability = float(model.predict_proba(input_df)[0][1])
    except Exception:
        app.logger.exception("Prediction failed")
        return jsonify({
            "error": "Could not process the supplied feature values."
        }), 400

    prediction = "Yes" if probability >= THRESHOLD else "No"

    return jsonify({
        "prediction": prediction,
        "model_score_percent": round(probability * 100, 2),
        "threshold_percent": round(THRESHOLD * 100, 2),
        "disclaimer": (
            "Educational model output only; not a medical diagnosis "
            "or a validated estimate of clinical risk."
        )
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
