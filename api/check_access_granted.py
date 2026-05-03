from database_decorators.db_fetchall import fetch_all


@fetch_all
def check_access_granted(
    username
):
    query = """
    SELECT *
    FROM access_granted
    WHERE username = ?
    """

    params = (username,)

    return query, params