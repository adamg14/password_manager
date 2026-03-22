from datetime import datetime
import sqlite3
from cryptography import hashing
from cryptography import kdf
connection = sqlite3.connect('password_manager.db')

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


@database_function
def create_user(
        cursor,
        username,
        master_password
):
    master_password_hash = hashing.generated_hash(master_password).decode()
    salt = kdf.create_salt().decode()

    cursor.execute(f"""
    INSERT INTO user (username, master_password_hash, salt, create_at, update_at) VALUES ({username}, {master_password_hash}, {salt}, {datetime.now()}, {datetime.now()})
                   """)



    

#     CREATE TABLE IF NOT EXISTS users (
#     username TEXT NOT NULL PRIMARY KEY,
#     master_password_hash  TEXT NOT NULL
#     salt TEXT NOT NULL
#     created_at DATE TIME NOT NULL
#     updated_at DATE TIME NOT NULL
# )
    