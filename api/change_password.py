from crypto.hashing import generated_hash
from datetime import datetime
from database_decorators.db_decorator import database_wrapper
import sqlite3 
import os
from api.get_vaults import get_vaults

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(FILE_PATH, "..", "password_manager.db")


def change_master_password(
    cursor,
    username,
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

    # for each vault
    for vault in vaults:
        pass
        # decrypt the vault key using the old password
        # encrypt the vault key using the new password
        # 
    # comit the transaction so that the changes to the db are atomic
    # get all the vaul
    cursor.execute("COMMIT;")
    connection.commit()
    connection.close()
    return True
    
    
