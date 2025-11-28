from fastapi import FastAPI
from routes.wounds import router as wound_router
from routes.vitals import router as vitals_router
from routes.risk import router as risk_router

app = FastAPI()

app.include_router(wound_router)
app.include_router(vitals_router)
app.include_router(risk_router)
