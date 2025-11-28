from fastapi import APIRouter, UploadFile, File
from ml.infer_wound import wound_model

router = APIRouter()

@router.post("/predict")
async def predict_wound(file: UploadFile = File(...)):
    img_bytes = await file.read()
    result = wound_model.predict(img_bytes)
    return {"status": "ok", "wound_prediction": result}
