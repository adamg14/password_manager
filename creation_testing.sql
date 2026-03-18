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