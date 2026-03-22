import secrets

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