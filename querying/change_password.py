from crypto.hashing import generated_hash
from datetime import datetime
from database_decorators.db_decorator import database_query_wrapper


@database_query_wrapper
def change_master_password(
    username,
    new_master_password
):
    new_password_hash = generated_hash(new_master_password)

    query = """
    UPDATE users
    SET master_password_hash=?
    WHERE username = ?"""


    return query, (new_password_hash, username)
    
    
