from crypto.hashing import generated_hash
from crypto.decryption import decryption
from crypto.encryption import encryption
from crypto.kdf import key_derivation_function

from database_decorators.db_decorator import transaction_decorator

from api.get_vaults import get_vaults
from api.get_user import get_user
from datetime import datetime
import sqlite3 
import os

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(FILE_PATH, "..", "password_manager.db")


# this functionality my have more than one execution query therefore it needs to be wrapper within a transaction
@transaction_decorator
def change_master_password(
    username,
    current_password,
    new_master_password
):
    # dictionary holding a hashmap between the query and the parameters
    result = {}
    new_password_hash = generated_hash(new_master_password)

    query = """
    UPDATE users
    SET master_password_hash = ?,
    updated_at = ?
    WHERE username = ?"""
    params = (new_password_hash, datetime.now(), username)
    result[query] = params

    # retieve all the vaults that belongs to the user
    # as if the password changes, the vault should be re-encrypted
    vaults = get_vaults(
        username
    )
    print(f"THIS SHOULD BE THE RESPONSE OF GET_VAULTS - SHOULD BE EMPTY: {vaults}")
    user_salt = get_user(username)[2]

    # for each vault
    for vault in vaults:
        old_encrypted_key = vault[2]
        # decrypt the vault key using the old password
        
        # get the salt for the user
        new_master_key = key_derivation_function(
            new_master_password,
            user_salt.encode()
        )

        password_hash = {}
        for entry in vault:
            password_hash[entry[0]] = decryption(
                old_encrypted_key.encode(),
                entry[3].decode()
            )
        
        # update all the entries associated with that vault
        for vault_id, decrypted_password in password_hash:
            # encrypt the entry with the new vault password
            new_encryped_entry = encryption(
                new_master_key,
                decrypted_password.encode()
            )
            query = """UPDATE entries
            SET encryped_data = ?
            WHERE id = ?"""
            params = (new_encryped_entry.decode(), vault_id)
            result[query] = params
        # encrypt the vault key using the new password
        # to do this must derive the master password key with the new master_password_key


        new_encryped_key = encryption(new_master_key.encode(), user_salt).decode()

        query = """UPDATE vault SET encrypted_key = ? WHERE id = ?"""
        params = (new_encryped_key, vault[0])
        result[query] = params
    

    return result
    # there are multiple execution statements for this statement
    # therefore they need to be ran as an atomic transaction
    # so if at any point of executiong the required queries in this function
    # there are interruptions, all the changes must be rolledback