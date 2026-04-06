import sqlite3
import os

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(FILE_PATH, "..", "password_manager.db")


def fetch_one(function):
    def wrapper(*args, **kwargs):
        try:
            connection = sqlite3.connect(DB_PATH)
            cursor = connection.cursor()

            result = function(*args, **kwargs)
            query = result[0]
            params = result[1]

            cursor.execute(query, params)

            db_result = cursor.fetchone()
            return db_result
        except Exception as e:
            print(f"Database error: {e}")
            return None
        finally:
            connection.close()
    return wrapper
