import numpy as np
import joblib
import pandas as pd

MODEL_PATH = "ml/models/vitals_anomaly_model.pkl"
iso = joblib.load(MODEL_PATH)

def check_vitals(hr, temp, spo2):
    df = pd.DataFrame([{"hr": hr, "temp": temp, "spo2": spo2}])
    ml_result = iso.predict(df)[0]

    alerts = []

    if ml_result == -1:
        alerts.append("Unusual Vitals Pattern (AI)")

    if temp > 38.5:
        alerts.append("High Fever")
    if hr > 110:
        alerts.append("High Heart Rate")
    if spo2 < 94:
        alerts.append("Low Oxygen Level (Hypoxia)")

    return alerts
