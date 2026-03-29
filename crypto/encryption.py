from cryptography.fernet import Fernet
import base64

# This function will be used to encrypt the vault key using the master password key
def encryption(key, message):
    try:
        fernet_key = base64.urlsafe_b64encode(key)
        cipher = Fernet(fernet_key)
        encrypted_message = cipher.encrypt(message)
        return encrypted_message
    except Exception as e:
        print("an error has occurred during encryption")
        print(e)
