from database_decorators.db_decorator import database_wrapper
from crypto.crypto_keys import generate_aes_key
from .get_salt import get_salt
from crypto.kdf import key_derivation_function
from crypto.encryption import encryption
from datetime import datetime

@database_wrapper
def create_valut(
    cursor,
    username,
    master_password,
    valut_name,
):
    
    # retrieve the salt dedicated to the user
    stored_salt = get_salt(username)[0]

    # derive the master key using the KDF
    derrived_master_key = key_derivation_function(master_password, stored_salt.encode())[1]

    # generate a brand new AES key for the vault
    vault_key = generate_aes_key()

    # encrypt the vault key for storage using the derived master key
    encrypted_vault_key = encryption(derrived_master_key, vault_key).decode()
    cursor.execute(f"""
    INSERT INTO vaults (vault_name, username, encrypted_key, created_at, update_at) VALUES (?, ?, ?, ?, ?)
                   """, (valut_name, username, encrypted_vault_key, datetime.now(), datetime.now()))
    return True