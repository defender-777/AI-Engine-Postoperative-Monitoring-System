from fastapi import APIRouter, UploadFile, File, Form
from ml.infer_wound import wound_model
from ml.anomaly_detector import check_vitals
from ml.risk_engine import compute_full_risk

router = APIRouter(prefix="/risk")

@router.post("/evaluate")
async def full_risk(
    file: UploadFile = File(...),
    hr: float = Form(...),
    temp: float = Form(...),
    spo2: float = Form(...)
):
    """
    Expects a multipart/form-data POST with:
      - file (image)
      - hr, temp, spo2 as form fields
    Returns a JSON with risk_score and details.
    """
    img_bytes = await file.read()

    # Wound prediction
    wound_pred = wound_model.predict(img_bytes)

    # Vitals anomaly detection
    vitals_alerts = check_vitals(hr, temp, spo2)

    # Compute combined risk (returns dict with risk_score, risk_level, reasons, explanation)
    full_risk = compute_full_risk(wound_pred, vitals_alerts)

    # Return unified response
    response = {
        "status": "ok",
        "wound_prediction": wound_pred,
        "vitals_alerts": vitals_alerts,
        # full_risk already contains "risk_score" numeric key
        **full_risk
    }
    return response
