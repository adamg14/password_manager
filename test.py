import sqlite3

print("hello world")

connection = sqlite3.connect("password_manager.db")
cursor = connection.cursor()
cursor.execute("select * from users")
print(cursor.fetchall())
connection.commit()