from fastapi import APIRouter, File, UploadFile, HTTPException
import requests
import os

router = APIRouter()

VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
API_URL = os.getenv("API_URL")

def upload_file(file):
    url = f"{API_URL}/files"
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    try: 
        files = {"file": (file.filename, file.file, file.content_type)}
        response = requests.post(url, headers=headers, files=files)
        response.raise_for_status()  
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error en la API de VirusTotal: {str(e)}")

def get_analysis_result(analysis_id: str):
    url = f"{API_URL}/analyses/{analysis_id}"
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error en la API de VirusTotal: {str(e)}")