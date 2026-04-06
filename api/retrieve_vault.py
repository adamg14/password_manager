from database_decorators.db_fetchone import fetch_one


@fetch_one
def retrieve_vault(
    username,
    vault_name
):
    query = f"""SELECT * FROM vaults WHERE username = ? and vault_name = ?"""
    return query, (username, vault_name)