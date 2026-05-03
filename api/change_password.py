from crypto.hashing import generated_hash
from crypto.decryption import decryption
from crypto.encryption import encryption
from crypto.kdf import key_derivation_function

from database_decorators.db_decorator import transaction_decorator

from api.get_vaults import get_vaults
from api.get_user import get_user
from datetime import datetime

from pathlib import Path

DB_PATH = Path.home() / ".password_manager" / "password_manager.db"


# this functionality my have more than one execution query therefore it needs to be wrapper within a transaction
@transaction_decorator
def change_master_password(
    username,
    current_password,
    new_master_password
):
    # dictionary holding a hashmap between the query and the parameters
    result = {}
    new_password_hash = generated_hash(new_master_password)

    query = """
    UPDATE users
    SET master_password_hash = ?,
    updated_at = ?
    WHERE username = ?"""
    params = (new_password_hash, datetime.now(), username)
    result[query] = params

    # retieve all the vaults that belongs to the user
    # as if the password changes, the vault should be re-encrypted
    vaults = get_vaults(
        username
    )
    if len(vaults) == 0:
        # the user currently has no vaults
        # therefore this functionality only needs a single query
        return result
    else:
        # the user has a vault - which may contain passwords
        # therefore there are additional queries needing to be added to the results
        # object to be executed for this functionality
        user_salt = get_user(username)[2]

    
    

    return result
    # there are multiple execution statements for this statement
    # therefore they need to be ran as an atomic transaction
    # so if at any point of executiong the required queries in this function
    # there are interruptions, all the changes must be rolledback