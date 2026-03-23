from cryptography.encryption import encryption
from database_wrapper import database_function


@database_function
def create_user(
        cursor,
        username,
        master_password
):
    master_password_hash = hashing.generated_hash(master_password).decode()
    salt = kdf.create_salt().decode()

    cursor.execute(f"""
    INSERT INTO user (username, master_password_hash, salt, create_at, update_at) VALUES ({username}, {master_password_hash}, {salt}, {datetime.now()}, {datetime.now()})
                   """)
    return True





    
