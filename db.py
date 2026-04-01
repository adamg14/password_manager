import sqlite3

connection = sqlite3.connect("password_manager.db")
cursor = connection.cursor()
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS entries (
#         id TEXT NOT NULL PRIMARY KEY,
#         vault_id TEXT NOT NULL REFERENCES vaults(id),
#         type TEXT NOT NULL DEFAULT 'login',
#         encrypted_data TEXT NOT NULL,
#         created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#         updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
#     )
# """)
cursor.execute("""
INSERT INTO entries (id, vault_id, type, encrypted_data) VALUES(?, ?, ?, ?)""", (1, ))
print(cursor.fetchall())
connection.commit()