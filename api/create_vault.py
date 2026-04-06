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
    
    # encrypt the vault key using the master password
    # retieved the salt dedicated to the user
    stored_salt = get_salt(username)[0]
    print(f"this should be the stored salt {stored_salt}")

    # pass the salt and the master password to derive the key stored to the derivation key function to get the master key
    derrived_master_key = key_derivation_function(master_password, stored_salt.encode())[1]
    print(f"this should be the derived master key: {derrived_master_key}")

    # generating a brand new AES key for the vault
    vault_key = generate_aes_key()

    print(f"THIS SHOULD BE THE VAULT KEY: {vault_key}")

    # encrypting the vault key for storage, the vault key is encrypted using the derrived master key
    encrypted_vault_key = encryption(derrived_master_key, vault_key).decode()

    print(f"THIS SHOULD BE THE ENCRYPTED VAULT KEY{encrypted_vault_key}")
    cursor.execute(f"""
    INSERT INTO vaults (vault_name, username, encrypted_key, created_at, update_at) VALUES (?, ?, ?, ?, ?)
                   """, (valut_name, username, encrypted_vault_key, datetime.now(), datetime.now()))
    return True