from fastapi import FastAPI
from src.routers import VirusTotal

app = FastAPI()

app.include_router(VirusTotal.router, prefix="/virustotal")

@app.get("/")
def home():
    return {"message": "API de análisis de archivos con VirusTotal"}