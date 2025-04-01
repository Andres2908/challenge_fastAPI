import pytest
from unittest.mock import patch, MagicMock
from src.services.VirusTotal import upload_file
from fastapi import UploadFile
from io import BytesIO

@pytest.fixture
def mock_file():
    return UploadFile(filename="test.txt", file=BytesIO(b"contenido de prueba"))

def test_upload_file(mock_file):
    mock_response = MagicMock()
    mock_response.json.return_value = {"data": {"id": "123456"}}
    mock_response.status_code = 200

    with patch("requests.post", return_value=mock_response): 
        response = upload_file(mock_file)

    assert response == {"data": {"id": "123456"}} 
