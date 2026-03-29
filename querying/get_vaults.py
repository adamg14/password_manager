


@database_function
def get_vaults(
    cursor,
    username
):
    cursor.execute("""
    SELECT * FROM values WHERE username = {username}
                   """)
    
    return cursor.fetchall()