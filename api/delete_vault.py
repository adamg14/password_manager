from database_decorators.db_decorator import transaction_decorator


@transaction_decorator
def delete_vault(
        vault_id
):
    queries = {}

    query1 = """
    DELETE FROM vault
    WHERE vault_id = ?"""
    params1 = (vault_id, )

    query2 = """
    DELETE FROM entries
    WHERE vault_id = ?"""
    params2 = (vault_id,)

    queries[query1] = params1
    queries[query2] = params2

    # delete the record from the vault table
    # delete all the corresponding entries records 
    # in the entries table
    return queries