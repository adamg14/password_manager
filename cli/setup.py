
import os
from pathlib import Path

DB_PATH = Path.home() / ".password_manager" / "password_manager.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

def set_up():
    try:
        import sqlite3
    except ImportError:
        print("Error: sqlite3 is not available in your Python installation")
        return -1
    try:

        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT NOT NULL PRIMARY KEY,
                master_password_hash  TEXT NOT NULL,
                salt TEXT NOT NULL,
                created_at DATE TIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at DATE TIME NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vault(
                vault_id TEXT NOT NULL PRIMARY KEY,
                vault_name TEXT NOT NULL,
                username TEXT NOT NULL,
                encrypted_key TEXT NOT NULL,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS entries (
                id TEXT NOT NULL PRIMARY KEY,
                vault_id TEXT NOT NULL REFERENCES vault(vault_id),
                type TEXT NOT NULL DEFAULT 'login',
                encrypted_data TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS access_granted (
                id TEXT NOT NULL PRIMARY KEY,
                vault_id TEXT NOT NULL REFERENCES vault(vault_id),
                vault_name TEXT NOT NULL,
                username TEXT NOT NULL,
                access_give TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );""")
        connection.commit()
        print("set up completed successfully.")
        return 1
    except Exception as e:
        print(f"Set up error occurred: {e}")
        # if any interruptions occur during the creation of the set up
        # rollback all the changes
        if connection:
            connection.rollback()
        return -1
    finally:
        connection.close()







