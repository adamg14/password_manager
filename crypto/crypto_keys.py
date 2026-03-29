from Crypto.Random import get_random_bytes

# one-time generation of the vault key for encrypting passwords 
def generate_aes_key():
    return get_random_bytes(16)

