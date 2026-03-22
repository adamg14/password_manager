import secrets

# one-time generation of the vault key for encrypting passwords 
def generate_aes_key():
    return secrets.token_bytes(32)