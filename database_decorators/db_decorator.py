import sqlite3
import os

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(FILE_PATH, "..", "password_manager.db")


def database_wrapper(function):
    def wrapper(*args, **kwargs):
        try:
            connection = sqlite3.connect(DB_PATH)
            cursor = connection.cursor()
            result = function(cursor, *args, **kwargs)
            connection.commit()
            return result
        except Exception as e:
            return e
        finally:
            connection.close()
    return wrapper

def database_query_wrapper(function):
    def wrapper(*args, **kwargs):
        try:
            print("function called")
            connection = sqlite3.connect(DB_PATH)
            cursor = connection.cursor()

            result = function(*args, **kwargs)
            print(result)
            query = result[0]
            params = result[2]

            cursor.execute(query, params)
            connection.commit()
            print("query committed")
            return True
        except Exception as e:
            return e
        finally:
            connection.close()
    
    return wrapper