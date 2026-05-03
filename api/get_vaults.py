from database_decorators.db_fetchall import fetch_all


@fetch_all
def get_vaults(
    username
):
    query = f"""SELECT * FROM vault WHERE username = ?"""
    return query, (username, )