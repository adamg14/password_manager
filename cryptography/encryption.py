from cryptography.fernet import Fernet


def encryption(key, message):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message