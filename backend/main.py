from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.wounds import router as wound_router
from routes.vitals import router as vitals_router

app = FastAPI()

# ✅ FIX: Allow CORS for your HTML frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Allow ALL origins (HTML, local files, React, anything)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(wound_router, prefix="/wound")
app.include_router(vitals_router, prefix="/vitals")

@app.get("/")
def root():
    return {"message": "Backend is running!"}
