from database_decorators.db_fetchone import fetch_one


@fetch_one
def retrieve_vault(
    username,
    vault_name
):
    query = f"""SELECT * FROM vault WHERE username = ? and vault_name = ?"""
    return query, (username, vault_name)

@fetch_one
def retrieve_vault_id(
    vault_id
):
    query = f"""SELECT * FROM vault WHERE vault_id = ?"""
    return query, (vault_id)