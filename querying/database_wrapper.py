def database_function(function):
    def wrapper(*args, **kwargs):
        connection = sqlite3.connect("../password_manager.db")
        cursor = connection.cursor()
        try:
            result = function(cursor, *args, **kwargs)
            connection.commit()
            return result
        finally:
            connection.close()
    return wrapper