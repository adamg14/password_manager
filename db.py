import sqlite3
from crypto import create_hash_salt


def database_connection():
    connection = sqlite3.connect("password_manager.db")
    cursor = connection.cursor()
    print(cursor)
    return cursor


db_cursor = database_connection()


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
        return "User created successfully."
    except Exception as e:
        print(e)
        return "An error occurred when created the user."
