from cryptography.fernet import Fernet


# This will be used to decrypt the vault key, so that it can be used to decrypt passwords to display to the user
def decryption(key, encrypted_message):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message).decode()