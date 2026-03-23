from datetime import datetime
import sqlite3
from cryptography import hashing
from cryptography import kdf
import uuid
from cryptography.crypto_keys import generate_aes_key
from cryptography.kdf import key_derivation_function
from cryptography.encryption import encryption
connection = sqlite3.connect('password_manager.db')
from database_wrapper import database_function


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
    return True


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


    
