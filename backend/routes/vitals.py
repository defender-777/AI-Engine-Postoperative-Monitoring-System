from fastapi import APIRouter, Request
from ml.anomaly_detector import check_vitals

router = APIRouter(prefix="/vitals")

@router.post("/check")
async def check_vitals_api(request: Request):
    """
    Accepts JSON body: { "hr": <num>, "temp": <num>, "spo2": <num> }
    Returns: {"status":"ok", "alerts": [...]}
    """
    data = await request.json()
    hr = data.get("hr")
    temp = data.get("temp")
    spo2 = data.get("spo2")

    # basic validation
    try:
        hr = float(hr)
        temp = float(temp)
        spo2 = float(spo2)
    except Exception:
        return {"status": "error", "message": "Invalid vitals input"}

    alerts = check_vitals(hr, temp, spo2)
    return {"status": "ok", "alerts": alerts}
