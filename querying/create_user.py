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


@database_function
def get_user(
    cursor,
    username
    ):
    cursor.execute(f"""SELECT * FROM user WHERE username = {username}""")
    row = cursor.fetchone()
    return row


@database_function
def validate_user(
    cursor,
    username,
    master_password
):
    user = get_user(cursor, username)
    input_hash = hashing.generated_hash(master_password).decode()

    if input_hash == user[1]:
        return True
    else:
        return False


    
