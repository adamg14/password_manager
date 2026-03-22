from cryptography.fernet import Fernet


# This function will be used to encrypt the vault key using the master password key
def encryption(key, message):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message