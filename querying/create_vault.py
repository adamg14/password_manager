from database_wrapper import database_function
from cryptography.crypto_keys import generate_aes_key
from get_salt import get_salt
from cryptography.kdf import key_derivation_function
from cryptography.encryption import encryption
import uuid


@database_function
def create_valut(
    cursor,
    username,
    master_password,
    valut_name,
    type
):
    # create a vault key
    vault_key = generate_aes_key()

    # encrypt the vault key using the master password
    stored_salt = get_salt(username)
    derrived_master_key = key_derivation_function(master_password, stored_salt)[1]

    # generating an AES key for the vault
    vault_key = generate_aes_key().decode()
    # encrypting the vault key for storage, the vault key is encrypted using the derrived master key
    encrypted_vault_key = encryption(derrived_master_key, vault_key).decode

    cursor.execute(f"""
    INSERT INTO vault (vault_id, vault_name, type, username, encrypted_key) VALUES ({uuid.uuid5()}, {valut_name}, {type}, {username}, {encrypted_vault_key})
                   """)