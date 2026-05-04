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
    # the salt is stored in the database as a
    # hexadecmial conversion of raw bytes
    stored_salt = get_salt(username)[0]


    # derive the master key using the KDF
    # the salt must be encoded into bytes before being passed into the
    # key derivation function method
    derrived_master_key = key_derivation_function(master_password, stored_salt.encode())[1]
    # generate a brand new AES key for the vault
    vault_key = generate_aes_key()

    # encrypt the vault key for storage using the derived master key
    # the encryption method takes the master key and encodes it inot base64 before being used as a key
    # the encrypted vault key must be encoded so that it can be stored in the database
    # raw bytes (vault key, master key)
    # encryption method encodes the key in base64
    # fernet key encryption (with b64 key) and raw bytes message
    # produces a cipher of b64 which can be encoded as a string then stored in the database
    encrypted_vault_key = encryption(derrived_master_key, vault_key).decode()
    query = """
    INSERT INTO vault (vault_id, vault_name, username, encrypted_key, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)
                   """
    params = (str(uuid.uuid4()), valut_name, username, encrypted_vault_key, datetime.now(), datetime.now())
    return query, params

