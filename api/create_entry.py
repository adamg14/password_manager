from database_decorators.db_decorator import database_wrapper
from .get_salt import get_salt
from crypto.decryption import decryption
from crypto.encryption import encryption
from crypto.kdf import key_derivation_function
import uuid
from datetime import datetime

@database_wrapper
def create_entry(
    cursor,
    username,
    master_password,
    vault_name,
    encrypted_key,
    password_type,
    password_input
):
    # retrieve the salt assigned to the user
    salt = get_salt(username=username)[0]

    # derive the master key using the KDF
    derived_master_key = key_derivation_function(master_password, salt.encode())[1]

    # decrypt the vault key using the master key
    decrypted_key = decryption(derived_master_key, encrypted_key.encode())

    # encrypt the new password with the vault key
    encrypted_password = encryption(decrypted_key.encode(), password_input.encode())

    query = """
    INSERT INTO entries (id, vault_id, type, encrypted_data, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)
                   """
    
    params = (str(uuid.uuid4()), vault_name, password_type, encrypted_password, datetime.now(), datetime.now())
    return query, params
