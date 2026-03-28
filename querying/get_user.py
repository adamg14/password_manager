from database_decorators.db_fetchone import fetch_one


@fetch_one
def get_user(
    username
):
    query = f"""SELECT * FROM users WHERE username = ?"""
    return query, (username,)

