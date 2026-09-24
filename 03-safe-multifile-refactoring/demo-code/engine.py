import time
from typing import List, Dict

class DataIngestionEngine:
    """
    Legacy synchronous data ingestion engine.
    Reads entire datasets into memory in a blocking manner.
    """
    def __init__(self, batch_size: int = 100):
        self.batch_size = batch_size

    def read_records(self, raw_data: List[str]) -> List[Dict[str, str]]:
        """
        Synchronously parses and transforms records, blocking the thread.
        """
        parsed = []
        for line in raw_data:
            # Simulate slight I/O processing delay
            time.sleep(0.01)
            parts = line.strip().split(",")
            if len(parts) >= 2:
                parsed.append({"id": parts[0], "value": parts[1]})
        return parsed
