from crypto.encryption import encryption
from decorators.db_decorator import database_wrapper
from crypto.kdf import create_salt
from crypto.hashing import generated_hash
from datetime import datetime


@database_wrapper
def create_user(
        cursor,
        username,
        master_password
):
    master_password_hash = generated_hash(master_password).decode()
    salt = create_salt().decode()

    cursor.execute(f"""
    INSERT INTO user (username, master_password_hash, salt, create_at, update_at) VALUES ({username}, {master_password_hash}, {salt}, {datetime.now()}, {datetime.now()})
                   """)
    return True





    
