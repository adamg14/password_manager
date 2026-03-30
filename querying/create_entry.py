from crypto.encryption import encryption
from database_decorators import database_wrapper
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
    # retieve the salt assigned to the user
    salt = get_salt(username=username).decode()
    # once again derive the master key using the KDF
    derived_master_key = key_derivation_function(
        master_password,
        salt
    )

    # decrypt the vault key using the master key
    decrypted_key = decryption(
        derived_master_key,
        encrypted_key
    )

    # encrypt the new password with the new key
    encrypted_password = encryption(
        decrypted_key.encode(),
        password_input
    )

    # use the master key
    cursor.execute(f"""
    INSERT INTO entries (id, vault_name, type, encrypted_data, created_at, update_at) VALUES
                   """, (uuid.uuid5(),vault_name, password_type, encrypted_password, datetime.now(),
                         datetime.now()
                         )
                   )
    return True
# CREATE TABLE IF NOT EXISTS entries (
#     id TEXT NOT NULL PRIMARY KEY,
#     vault_id TEXT NOT NULL REFERENCES vaults(id),
#     type TEXT NOT NULL DEFAULT 'login',
#     encrypted_data TEXT NOT NULL,
#     created_at TIMESTAMP DEFAULT now()
#     updated_at TIMESTAMP DEFAULT now()
# )