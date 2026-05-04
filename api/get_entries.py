# need a fetchall wrapper function
# decoded_password = base64.b64decode(encrypted_password.encode("utf-8"))
# decrypted = decryption(key, decoded_password)
from database_decorators.db_fetchall import fetch_all


@fetch_all
def get_entries(vault_id):
    query = """
    SELECT *
    FROM entries
    WHERE vault_id = ?"""
    params = (vault_id,)

    return query, params
