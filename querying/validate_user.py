from database_wrapper import database 


@database_function
def validate_user(
    cursor,
    username,
    master_password
):
    user = get_user(cursor, username)
    input_hash = hashing.generated_hash(master_password).decode()

    if input_hash == user[1]:
        return True
    else:
        return False