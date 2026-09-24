import hashlib
import os
from models.user import UserRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    async def create_user(self, email: str, username: str, password: str, origin_ip: str) -> dict:
        """
        Coordinates password hashing, business validation, 
        and persistence via the UserRepository.
        """
        # Generate salt & compute hash
        salt = os.urandom(16).hex()
        password_hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

        user_record = await self.repo.save(
            email=email,
            username=username,
            password_hash=password_hash,
            salt=salt,
            created_from_ip=origin_ip
        )
        return {
            "id": user_record["id"],
            "email": user_record["email"],
            "username": user_record["username"],
            "created_at": user_record["created_at"]
        }
