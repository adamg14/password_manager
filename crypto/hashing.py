from Crypto.Hash import SHA512


def generated_hash(master_password):
    """
    input:
        plaintext master password: str
    output:
        SHA512 hash digest: bytes
    """
    encoded_master_password = master_password.encode('utf-8')
    hashed_password = SHA512.new(data=encoded_master_password).hexdigest()
    return hashed_password


