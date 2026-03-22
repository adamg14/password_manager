# Key Derivation Function: (Input: Plain Text Password) -> (Ouptut: Encryption Key)
# PBKDF5
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes 

def key_derivation_function(
        master_password
):
    """
    input:
        plaintext master password: str
    output:
        salt: bytes,
        key: bytes (AES265 key) """
    salt = get_random_bytes(16)
    key = PBKDF2(master_password, salt, 32, count=1000000, hmac_hash_module=SHA512)
    return salt, key

def generated_hash(mater_password):
    """
    input:
        plaintext master password: str
    output:
        SHA512 hash digest: bytes
    """
    encoded_master_password = mater_password.encode()
    hashed_password = SHA512.new(data=encoded_master_password).digest()
    return hashed_password

