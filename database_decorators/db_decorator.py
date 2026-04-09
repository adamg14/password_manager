import sqlite3
import os

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(FILE_PATH, "..", "password_manager.db")


def transaction_decorator(function):
    def wrapper(*args, **kwargs):
        try:
            connection = sqlite3.connect(DB_PATH)
            cursor = connection.cursor()

            # function returns a list of queries it needs to be atomic
            cursor.execute("BEGIN TRANSACTION;")
            # function runs the queries within the transactions
            result = function(cursor, *args, **kwargs)
            cursor.execute("COMMIT;")
            connection.commit()
            return result
        except Exception as e:
            print(f"Database error: {e}")
            return None
        
        
def database_wrapper(function):
    def wrapper(*args, **kwargs):
        try:
            connection = sqlite3.connect(DB_PATH)
            cursor = connection.cursor()
            result = function(cursor, *args, **kwargs)
            connection.commit()
            return result
        except Exception as e:
            print(f"Database error: {e}")
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
