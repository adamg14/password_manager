from datetime import datetime
import sqlite3
from cryptography import hashing
from cryptography import kdf
import uuid
from cryptography.crypto_keys import generate_aes_key
from cryptography.kdf import key_derivation_function
from cryptography.encryption import encryption
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
    return wrapper


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
def get_salt(
    cursor,
    username
):
    cursor.execute(f"""
    SELECT salt FROM user WHERE username = {username}
                   """)
    return cursor.fetchone()


@database_function
def create_valut(
    cursor,
    username,
    master_password,
    valut_name,
    type
):
    # create a vault key
    vault_key = generate_aes_key()

    # encrypt the vault key using the master password
    stored_salt = get_salt(username)
    derrived_master_key = key_derivation_function(master_password, stored_salt)[1]

    # generating an AES key for the vault
    vault_key = generate_aes_key().decode()
    # encrypting the vault key for storage, the vault key is encrypted using the derrived master key
    encrypted_vault_key = encryption(derrived_master_key, vault_key).decode

    cursor.execute(f"""
    INSERT INTO vault (vault_id, vault_name, type, username, encrypted_key) VALUES ({uuid.uuid5()}, {valut_name}, {type}, {username}, {encrypted_vault_key})
                   """)


@database_function
def get_user(
    cursor,
    username
    ):
    cursor.execute(f"""SELECT * FROM user WHERE username = {username}""")
    return cursor.fetchone()


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


    
