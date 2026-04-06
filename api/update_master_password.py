from database_decorators.db_decorator import database_wrapper
from crypto.kdf import key_derivation_function
from crypto.decryption import decryption
from crypto.encryption import encryption
from crypto.hashing import generated_hash
from datetime import datetime


@database_wrapper
def update_master_password(cursor, username, old_password, new_password):
    # fetch the user's salt from the same transaction
    cursor.execute("SELECT salt FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    if not row:
        return False
    salt = row[0]

    # derive master keys for both old and new passwords
    old_master_key = key_derivation_function(old_password, salt.encode())[1]
    new_master_key = key_derivation_function(new_password, salt.encode())[1]

    # fetch all vaults belonging to this user
    cursor.execute(
        "SELECT vault_name, encrypted_key FROM vaults WHERE username = ?",
        (username,)
    )
    vaults = cursor.fetchall()

    # re-encrypt each vault key: decrypt with old master key, re-encrypt with new
    for vault_name, encrypted_vault_key in vaults:
        vault_key = decryption(old_master_key, encrypted_vault_key.encode())
        new_encrypted_vault_key = encryption(new_master_key, vault_key.encode()).decode()
        cursor.execute(
            "UPDATE vaults SET encrypted_key = ?, update_at = ? WHERE vault_name = ? AND username = ?",
            (new_encrypted_vault_key, datetime.now(), vault_name, username)
        )

    # update the stored password hash
    cursor.execute(
        "UPDATE users SET master_password_hash = ?, updated_at = ? WHERE username = ?",
        (generated_hash(new_password), datetime.now(), username)
    )

    return cursor.rowcount > 0
