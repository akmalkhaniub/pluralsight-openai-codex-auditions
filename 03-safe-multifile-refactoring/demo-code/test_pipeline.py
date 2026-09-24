import pytest
from controller import IngestionController

def test_ingestion_controller_success():
    """
    Verifies that the ingestion pipeline processes lines correctly.
    """
    raw_lines = [
        "USR001,Alpha",
        "USR002,Beta",
        "USR003,Gamma"
    ]
    controller = IngestionController()
    result = controller.process_upload(raw_lines)
    
    assert result["status"] == "completed"
    assert result["processed_count"] == 3
    assert result["sample"][0]["id"] == "USR001"
