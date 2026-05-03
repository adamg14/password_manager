import sqlite3
from pathlib import Path

DB_PATH = Path.home() / ".password_manager" / "password_manager.db"

def fetch_one(function):
    def wrapper(*args, **kwargs):
        try:
            connection = sqlite3.connect(DB_PATH)
            cursor = connection.cursor()

            result = function(*args, **kwargs)
            query, params = result

            cursor.execute(query, params)

            db_result = cursor.fetchone()
            return db_result
        except Exception as e:
            print(f"Database error: {e}")
            return None
        finally:
            connection.close()
    return wrapper
