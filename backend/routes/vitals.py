from fastapi import APIRouter
from ml.anomaly_detector import check_vitals

router = APIRouter()

@router.post("/vitals/check")
async def vitals_check(data: dict):
    alerts = check_vitals(data["hr"], data["temp"], data["spo2"])
    return {"alerts": alerts}
