from decorators.db_decorator import database_wrapper


@database_wrapper
def get_salt(
    cursor,
    username
):
    cursor.execute(f"""
    SELECT salt FROM user WHERE username = {username}
                   """)
    return cursor.fetchone()