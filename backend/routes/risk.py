from fastapi import APIRouter, UploadFile, File
from ml.infer_wound import wound_model
from ml.anomaly_detector import check_vitals
from ml.risk_engine import compute_full_risk

router = APIRouter()

@router.post("/risk/evaluate")
async def full_risk(
    file: UploadFile = File(...),
    hr: float = 0,
    temp: float = 0,
    spo2: float = 0
):
    img_bytes = await file.read()
    
    wound_pred = wound_model.predict(img_bytes)
    vitals_alerts = check_vitals(hr, temp, spo2)
    risk = compute_full_risk(wound_pred, vitals_alerts)

    return {
        "wound_prediction": wound_pred,
        "vitals_alerts": vitals_alerts,
        "risk": risk
    }
