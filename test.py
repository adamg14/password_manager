import sqlite3

connection = sqlite3.connect("./password_manager.db")
cursor = connection.cursor()
query = "SELECT * FROM tablename;"
cursor.execute(query)
result = cursor.fetchall()
print(result)
