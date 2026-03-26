import sqlite3
import os

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(FILE_PATH, "..", "password_manager.db")


def database_wrapper(function):
    def wrapper(*args, **kwargs):
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        try:
            result = function(cursor, *args, **kwargs)
            connection.commit()
            return result
        finally:
            connection.close()
    return wrapper