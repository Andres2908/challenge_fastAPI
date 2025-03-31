from fastapi import APIRouter, UploadFile, File
from ..services import VirusTotal as virusTotal_service

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    result = virusTotal_service.upload_file(file)
    return {"message": "Archivo enviado a VirusTotal", "data": result}


@router.get("/upload")
async def get_analysis(analysis_id: str):
    result = virusTotal_service.get_analysis_result(analysis_id)
    return {"message": "Resultado del análisis", "data": result}