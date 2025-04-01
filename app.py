from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import VirusTotal

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

app.include_router(VirusTotal.router, prefix="/virustotal")

@app.get("/")
def home():
    return {"message": "API de análisis de archivos con VirusTotal"}