from crypto.hashing import generated_hash
from datetime import datetime
from database_decorators.db_decorator import database_wrapper


@database_wrapper
def change_master_password(
    cursor,
    username,
    new_master_password
):
    new_password_hash = generated_hash(new_master_password)

    query = """
UPDATE users
SET master_password_hash = ?,
updated_at = ?
WHERE username = ?"""

    cursor.execute(query, (new_password_hash, datetime.now(), username))


    return cursor.rowcount > 0
    
    
