import sqlite3

connection = sqlite3.connect("password_manager.db")
cursor = connection.cursor()
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     username TEXT NOT NULL PRIMARY KEY,
#     master_password_hash  TEXT NOT NULL,
#     salt TEXT NOT NULL,
#     created_at DATE TIME NOT NULL,
#     updated_at DATE TIME NOT NULL
# )
# """)


cursor.execute("SELECT * FROM vaults")
print(cursor.fetchall())