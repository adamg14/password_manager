from .get_salt import get_salt
from crypto.kdf import key_derivation_function
from crypto.decryption import decryption
import base64
from cryptography.fernet import Fernet


def decrypt_entry(username, master_password, encrypted_key, encrypted_data):
    try:
        # get the salt from the users table in the database
        salt = get_salt(username=username)[0]

        # derive the master key
        derived_master_key = key_derivation_function(master_password, salt.encode())[1]

        # decrypt the vault key using the master key
        fernet_key = base64.urlsafe_b64encode(derived_master_key)
        cipher = Fernet(fernet_key)
        # this variable now holds the true vaule of the vault ket
        decrypted_vault_key = cipher.decrypt(encrypted_key.encode()) 

        # decode the encrypted data which is stored in the database as base64 encoding
        # then decode this base64 encoding into bytes
        encrypted_bytes = base64.b64decode(encrypted_data.encode("utf-8"))

        # decrypt the encrypted bytes using the decrypted vault key
        plaintext_password = decryption(decrypted_vault_key, encrypted_bytes)

        return plaintext_password

    except Exception as e:
        print(f"Error decrypting entry: {e}")
        return None