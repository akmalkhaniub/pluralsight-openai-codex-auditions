import datetime
import uuid

class UserRepository:
    """
    Persistence layer interface for User entities.
    Simulates database persistence with timestamping and unique UUIDs.
    """
    def __init__(self):
        # Simulated database storage table
        self._table = []

    async def save(self, email: str, username: str, password_hash: str, salt: str, created_from_ip: str) -> dict:
        record = {
            "id": str(uuid.uuid4()),
            "email": email,
            "username": username,
            "password_hash": password_hash,
            "salt": salt,
            "created_from_ip": created_from_ip,
            "created_at": datetime.datetime.utcnow().isoformat()
        }
        self._table.append(record)
        return record
