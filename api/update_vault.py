from database_decorators.db_decorator import database_wrapper

@database_wrapper
def update_vault(
        username,
        vault_id,
        new_encryped_key
):
    query = """
    UPDATE vaults 
    SET encrypted_key = ?
    WHERE username = ?
    AND vault_id = ?"""

    params = (
        new_encryped_key,
        username,
        vault_id
    )

    return query, params
    