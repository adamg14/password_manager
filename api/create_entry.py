from database_decorators.db_decorator import database_wrapper
from .get_salt import get_salt
from crypto.decryption import decryption
from crypto.encryption import encryption
from crypto.kdf import key_derivation_function
import uuid
from datetime import datetime
import base64
from cryptography.fernet import Fernet


@database_wrapper
def create_entry(
    username,
    master_password,
    vault_name,
    encrypted_key,
    password_type,
    password_input
):
    # retrieve the salt assigned to the user
    salt = get_salt(username=username)[0]
    print(f"this is the salt {salt}")
    # derive the master key using the KDF
    derived_master_key = key_derivation_function(master_password, salt)[1]

    # decrypt the encrypted vault key (which is stored in the database)
    # using the master key (derived by the function above)
    fernet_key = base64.urlsafe_b64encode(derived_master_key)
    cipher = Fernet(fernet_key)

    # the raw 
    decrypted_key = cipher.decrypt(encrypted_key.encode())
    
    # encrypt the new password with the vault key
    encrypted_password = encryption(decrypted_key, password_input.encode())

    # right now the password in encrypted in raw bytes, 
    # meaning it cannot be decoded into utf-8
    # raw bytes -> base64 -> utf-8
    encoded_password = base64.b64encode(encrypted_password).decode("utf-8")
    query = """
    INSERT INTO entries (id, vault_id, type, encrypted_data, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)
                   """
    
    params = (str(uuid.uuid4()), vault_name, password_type, encoded_password, datetime.now(), datetime.now())
    return query, params
