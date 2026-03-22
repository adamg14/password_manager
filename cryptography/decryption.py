from cryptography.fernet import Fernet


def decryption(key, encrypted_message):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message).decode()