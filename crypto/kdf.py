# Key Derivation Function: (Input: Plain Text Password) -> (Ouptut: Encryption Key)
# PBKDF5
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes 


def key_derivation_function(
        master_password,
        salt
):
    """
    input:
        plaintext master password: str
    output:
        salt: bytes,
        key: bytes (AES265 key) """
    salt = salt.decode()
    key = PBKDF2(master_password, salt, 32, count=1000000, hmac_hash_module=SHA512)
    return salt, key


def create_salt():
    return get_random_bytes(16).hex()



