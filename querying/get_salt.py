from database_wrapper import database_function


@database_function
def get_salt(
    cursor,
    username
):
    cursor.execute(f"""
    SELECT salt FROM user WHERE username = {username}
                   """)
    return cursor.fetchone()