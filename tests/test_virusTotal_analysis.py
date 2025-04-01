import pytest
from unittest.mock import patch, MagicMock
from src.services.VirusTotal import get_analysis_result

def test_get_analysis_result():
    analysis_id = "123456"

    mock_response = MagicMock()
    mock_response.json.return_value = {"data": {"attributes": {"status": "completed"}}}
    mock_response.status_code = 200

    with patch("requests.get", return_value=mock_response):
        response = get_analysis_result(analysis_id)
    assert response == {"data": {"attributes": {"status": "completed"}}}