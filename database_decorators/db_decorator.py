import sqlite3
from pathlib import Path
import traceback


DB_PATH = Path.home() / ".password_manager" / "password_manager.db"


def transaction_decorator(function):
    def wrapper(*args, **kwargs):
        try:
            connection = sqlite3.connect(DB_PATH)
            cursor = connection.cursor()

            # function returns a list of queries it needs to be atomic
            cursor.execute("BEGIN TRANSACTION;")
            # function runs the queries within the transactions
            result = function(*args, **kwargs)
            for query, params in result.items():
                cursor.execute(query, params)
            connection.commit()
            return True
        except Exception as e:
            print(f"Database error: {e}")
            # rollback any changes to the database if connection is interrupted
            # this ensures atomicity
            connection.rollback()
            return None
        finally:
            connection.close()
    return wrapper
        
        
def database_wrapper(function):
    def wrapper(*args, **kwargs):
        try:
            connection = sqlite3.connect(DB_PATH)
            cursor = connection.cursor()
            query, params  = function(*args, **kwargs)
            cursor.execute(query, params)
            connection.commit()
            return True
        except Exception as e:
            print(f"Database error: {e}")
            traceback.print_exc()
            return None
        finally:
            connection.close()
    return wrapper


def database_query_wrapper(function):
    def wrapper(*args, **kwargs):
        try:
            connection = sqlite3.connect(DB_PATH)
            cursor = connection.cursor()

            result = function(*args, **kwargs)
            query = result[0]
            params = result[1]

            cursor.execute(query, params)
            connection.commit()
            return True
        except Exception as e:
            print(f"Database error: {e}")
            return None
        finally:
            connection.close()

    return wrapper
