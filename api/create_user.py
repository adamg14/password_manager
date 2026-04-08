from crypto.encryption import encryption
from database_decorators.db_decorator import database_wrapper
from crypto.kdf import create_salt
from crypto.hashing import generated_hash
from datetime import datetime


@database_wrapper
def create_user(
        cursor,
        username,
        master_password
):
        master_password_hash = generated_hash(master_password)
        salt = create_salt()

        query = """
        INSERT INTO users (username, master_password_hash, salt, created_at, updated_at) VALUES (?, ?, ?, ?, ?)
                        """
        
        params = (username, master_password_hash, salt, datetime.now(), datetime.now())
        
        return query, params





    
