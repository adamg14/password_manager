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

    # derive the master key using the KDF
    derrived_master_key = key_derivation_function(master_password, salt.encode())[1]

    
    # decrypt the encrypted vault key (which is stored in the database)
    # using the master key (derived by the function above)
    # the decryption function return a decoded string
    fernet_key = base64.urlsafe_b64encode(derrived_master_key)
    cipher = Fernet(fernet_key)
    decrypted_key = cipher.decrypt(encrypted_key.encode())
    print(f"decrypted_key length: {len(decrypted_key)}, value: {decrypted_key.hex()}")
    
    # encrypt the new password with the vault key
    # the encryption function will encode the raw bytes of the encrypted key to base 64
    encrypted_password = encryption(decrypted_key, password_input.encode())
    print(f"THIS SHOULD BE THE ENCRYPTED PASSWORD (DECODED SO THAT IT IS A STRING): {encrypted_password.decode()}")
    # right now the password in encrypted in raw bytes, 
    # meaning it cannot be decoded into utf-8
    # raw bytes -> base64 -> utf-8
    decoded_password = base64.b64encode(encrypted_password).decode("utf-8")
    print(f"this should be the decoded encrypted password in utf-8: {decoded_password}")
    query = """
    INSERT INTO entries (id, vault_id, type, encrypted_data, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)
                   """
    
    params = (str(uuid.uuid4()), vault_name, password_type, decoded_password, datetime.now(), datetime.now())
    return query, params
