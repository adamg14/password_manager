import base64
from cryptography.fernet import Fernet


# This will be used to decrypt the vault key, so that it can be used to decrypt passwords to display to the user
def decryption(key, encrypted_message):
    fernet_key = base64.urlsafe_b64encode(key)
    cipher = Fernet(fernet_key)
    return cipher.decrypt(encrypted_message).decode()