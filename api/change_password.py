from crypto.hashing import generated_hash
from crypto.decryption import decryption
from crypto.encryption import encryption
from crypto.kdf import key_derivation_function

from database_decorators.db_decorator import database_wrapper

from api.get_vaults import get_vaults
from api.get_user import get_user
from datetime import datetime
import sqlite3 
import os

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(FILE_PATH, "..", "password_manager.db")


def change_master_password(
    cursor,
    username,
    current_password,
    new_master_password
):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    # being the transaction so the update of the password and the consequent changes are ATOMIC in line with ACID principles
    cursor.execute("BEGIN TRANSACTION;")   
    new_password_hash = generated_hash(new_master_password)

    query = """
    UPDATE users
    SET master_password_hash = ?,
    updated_at = ?
    WHERE username = ?"""
    params = (new_password_hash, datetime.now(), username)

    cursor.execute(query, params)

    # retieve all the vaults that belongs to the user 
    vaults = get_vaults(
        username
    )

    user_salt = get_user(username)[2]

    # for each vault
    for vault in vaults:
        old_encrypted_key = vault[2]
        # decrypt the vault key using the old password

        # encrypt the vault key using the new password
        # to do this must derive the master password key with the new master_password_key

        # get the salt for the user
        new_master_key = key_derivation_function(
            new_master_password,
            user_salt.encode()
        )

        new_encryped_key = encryption(new_master_key.encode(), user_salt).decode()

        query = """UPDATE vault SET encrypted_key = ? WHERE id = ?"""
        params = (new_encryped_key, vault[0])

    # comit the transaction so that the changes to the db are atomic
    # get all the vaul
    cursor.execute("COMMIT;")
    connection.commit()
    connection.close()
    return True
    
    
