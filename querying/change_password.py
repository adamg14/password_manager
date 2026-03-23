from database_wrapper import database_function
from cryptography.hashing import generated_hash
from datetime import datetime


@database_function
def change_master_password(
    cursor,
    username,
    new_master_password
):
    generated_hash().decode()
    cursor.execute(
        f"""
        UPDATE username
        SET master_password_hash = {generated_hash(new_master_password).decode()}
        WHERE username = {username}""")
    cursor.execute(f"""
        UPDATE username
        SET updated_at = {datetime.now()}
        WHERE username = {username}
                   """)
