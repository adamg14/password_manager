from datbase_wrapper.database_wrapper import database_function 
from get_user import get_user
from crypto.hashing import generated_hash

@database_function
def validate_user(
    cursor,
    username,
    master_password
):
    user = get_user(cursor, username)
    input_hash = generated_hash(master_password).decode()

    if input_hash == user[1]:
        return True
    else:
        return False