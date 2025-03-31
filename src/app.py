from fastapi import FastAPI
from routers import VirusTotal

app = FastAPI()

app.include_router(VirusTotal.router)

@app.get("/")
def home():
    return {"message": "API de análisis de archivos con VirusTotal"}