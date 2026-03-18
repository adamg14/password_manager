import sqlite3
from crypto import create_hash_salt, verify_password


connection = sqlite3.connect("password_manager.db")
db_cursor = connection.cursor()


def select_all(cursor, db_table):
    cursor.execute(f'SELECT * FROM {db_table}')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def drop_table(cursor, db_table):
    try:
        cursor.execute(f'DROP TABLE IF EXISTS {db_table}')
    except:
        print("error occurred when dropping table")

def create_user(username, master_password):
    try:
        hashed_master_password = create_hash_salt(master_password)
        print(f"this should be the hashed password{hashed_master_password[1:-1]}")
        db_cursor.execute(f'INSERT INTO user (username, master_password) VALUES("{username}", "{hashed_master_password}")')
        connection.commit()
        return "User created successfully."
    except Exception as e:
        print(e)
        return "An error occurred when created the user."

def validate_user(
        username,
        password
):
    db_cursor.execute(f'''
                      SELECT *
                      FROM user
                      WHERE username = "{username}"
                      ''')
    query_result = db_cursor.fetchone()
    print(query_result)
    if query_result == []:
        return "user does not exist"
    else:
        stored_password = query_result[1]
        if stored_password == create_hash_salt(password):
            return True
        else:
            return False

    

create = create_user("adam1234", "password")
result = validate_user("adam1234", create_hash_salt("password"))
print(result)