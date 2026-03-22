import secrets


def generate_aes_key():
    return secrets.token_bytes(32)