from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers
from routes.wounds import router as wound_router
from routes.vitals import router as vitals_router
from routes.risk import router as risk_router

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers (each router defines its own prefix)
app.include_router(wound_router)
app.include_router(vitals_router)
app.include_router(risk_router)

@app.get("/")
def root():
    return {"message": "Backend is running!"}
