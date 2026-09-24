import sqlite3
import os

DB_PATH = "database.sqlite"

def init_database():
    """
    Initializes a test database simulating a production schema 
    where a recent migration added a NOT NULL tenant_id column.
    """
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(50) NOT NULL UNIQUE,
        email VARCHAR(100) NOT NULL,
        tenant_id VARCHAR(50) NOT NULL
    );
    """)

    conn.commit()
    conn.close()
    print(f"Initialized {DB_PATH} with users schema (including tenant_id).")

if __name__ == "__main__":
    init_database()
