from database_decorators.db_fetchone import fetch_one


@fetch_one
def get_salt(
    username
):
    query = f"""SELECT salt FROM users WHERE username = ?"""
    return query, (username,)


