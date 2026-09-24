from typing import List, Dict
from engine import DataIngestionEngine

class IngestionController:
    """
    API Controller that coordinates the ingestion workflow.
    Directly depends on DataIngestionEngine's synchronous interface.
    """
    def __init__(self):
        self.engine = DataIngestionEngine()

    def process_upload(self, raw_lines: List[str]) -> Dict[str, any]:
        """
        Synchronous handler processing an upload batch.
        """
        records = self.engine.read_records(raw_lines)
        total_items = len(records)
        return {
            "status": "completed",
            "processed_count": total_items,
            "sample": records[:3] if records else []
        }
