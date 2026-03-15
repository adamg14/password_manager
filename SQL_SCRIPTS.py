from main import database_connection

db_cursor = database_connection()

# creating the main user table, storing the 
db_cursor.execute('''
          CREATE TABLE IF NOT EXISTS user (
          username TEXT PRIMARY KEY NOT NULL,
          master_password TEXT NOT NULL
          )
          ''')
db_cursor.execute('''DROP TABLE IF EXISTS password''')
db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS password(
        username TEXT NOT NULL,
        entity TEXT NOT NULL,
        password TEXT NOT NULL,
        FOREIGN KEY (username) REFERENCES user(username))
                  ''')
db_cursor.execute('''INSERT INTO user(username, master_password) VALUES ('adam', 'password123')''')
db_cursor.execute('''INSERT INTO password(username, entity, password) VALUES ('adam', 'Facebook', 'password1')''')

def select_all(cursor, db_table):
    cursor.execute(f'SELECT * FROM {db_table}')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# print("User table created successfully")
# print("test user added to db successfully ")
# select_all(db_cursor, 'user')
# select_all(db_cursor,db_table='password')
select_all(db_cursor, db_table='password')
