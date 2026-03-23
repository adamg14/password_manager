from database_wrapper import database_function


@database_function
def get_user(
    cursor,
    username
    ):
    cursor.execute(f"""SELECT * FROM user WHERE username = {username}""")
    return cursor.fetchone()

