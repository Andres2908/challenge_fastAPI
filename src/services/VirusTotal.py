from fastapi import APIRouter, HTTPException
import os
from dotenv import load_dotenv
import requests

load_dotenv()
router = APIRouter()

VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
API_URL = os.getenv("API_URL")

def make_request(method, url, headers, files=None):
    try:
        if method == "POST":
            response = requests.post(url, headers=headers, files=files)
        elif method == "GET":
            response = requests.get(url, headers=headers)

        response.raise_for_status()  
        return response.json()
    
    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=502, detail="Error de conexión con la API de VirusTotal")

    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="Tiempo de espera agotado al conectar con VirusTotal")

    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code
        raise HTTPException(status_code=status_code, detail=f"Error en la API de VirusTotal: {e}")

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error en la API de VirusTotal: {str(e)}")


def upload_file(file):
    url = f"{API_URL}/files"
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    files = {"file": (file.filename, file.file, file.content_type)}
    return make_request("POST", url, headers, files)

def get_analysis_result(analysis_id: str):
    url = f"{API_URL}/analyses/{analysis_id}"
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    return make_request("GET", url, headers)
