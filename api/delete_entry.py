import sqlite3
from pathlib import Path
from datetime import datetime
from database_decorators.db_decorator import transaction_decorator
DB_PATH = Path.home() / ".password_manager" / "password_manager.db"


@transaction_decorator
def delete_entry(vault_id, entry_type):
    # first delete the entry from the entry table
    queries = {}
    query_one = """
    DELETE FROM ENTRIES
    WHERE vault_id = ?
    AND type = ?
    """
    params1  = (vault_id, entry_type)

    query_two = """
    UPDATE vault
    SET updated_at = ?
    WHERE vault_id = ?"""
    params2 = (datetime.now(), vault_id)

    queries[query_one] = params1
    queries[query_two] = params2

    return queries
    # next we need to update the vault 
    # in order to update the vault 
