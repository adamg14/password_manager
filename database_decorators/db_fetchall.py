import sqlite3
from pathlib import Path

DB_PATH = Path.home() / ".password_manager" / "password_manager.db"

def fetch_all(function):
    def wrapper(*args, **kwargs):
        try:
            connection = sqlite3.connect(DB_PATH)
            cursor = connection.cursor()

            result = function(*args, **kwargs)
            query = result[0]
            params = result[1]

            cursor.execute(query, params)

            db_result = cursor.fetchall()

            return db_result
        except Exception as e:
            print(f"Database error: {e}")
            return []
        finally:
            connection.close()
        
    return wrapper
