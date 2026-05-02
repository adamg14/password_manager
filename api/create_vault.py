from database_decorators.db_decorator import database_wrapper
from crypto.crypto_keys import generate_aes_key
from .get_salt import get_salt
from crypto.kdf import key_derivation_function
from crypto.encryption import encryption
from datetime import datetime
import uuid


@database_wrapper
def create_valut(
    username,
    master_password,
    valut_name,
):
    
    # retrieve the salt dedicated to the user
    stored_salt = get_salt(username)[0]
    print(f"this should be the stored salt: {stored_salt}")

    # derive the master key using the KDF
    derrived_master_key = key_derivation_function(master_password, stored_salt.encode())[1]
    print(f"this should be the derived master password: {derrived_master_key}")
    # generate a brand new AES key for the vault
    vault_key = generate_aes_key()

    # encrypt the vault key for storage using the derived master key
    encrypted_vault_key = encryption(derrived_master_key, vault_key).decode()
    query = """
    INSERT INTO vault (vault_id, vault_name, username, encrypted_key, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)
                   """
    params = (str(uuid.uuid4()), valut_name, username, encrypted_vault_key, datetime.now(), datetime.now())
    return query, params

