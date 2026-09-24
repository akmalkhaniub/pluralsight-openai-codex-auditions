import sqlite3
from dataclasses import dataclass

@dataclass
class User:
    username: str
    email: str

def create_user(user: User):
    """
    Inserts a user record into the SQLite database.
    BUG: The code has not been updated for the new schema migration 
    requiring tenant_id, causing an IntegrityError at runtime.
    """
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()

    try:
        # Failing query: Missing tenant_id column!
        cursor.execute(
            "INSERT INTO users (username, email) VALUES (?, ?)",
            (user.username, user.email)
        )
        conn.commit()
        user_id = cursor.lastrowid
        print(f"User created successfully with ID: {user_id}")
        return user_id
    finally:
        conn.close()

if __name__ == "__main__":
    test_user = User(username="alex_dev", email="alex@company.internal")
    create_user(test_user)
