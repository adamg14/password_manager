import sqlite3
from pathlib import Path
import traceback


DB_PATH = Path.home() / ".password_manager" / "password_manager.db"
connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()
cursor.execute("SELECT * FROM entries;")
result = cursor.fetchone()
print(result)

# this is the entries object 
# (
# 'b942d393-b115-4e4d-b1d4-1dd4bb4fc026',
# 'Google',
# 'authentication',
# 'Z0FBQUFBQnA5ODRFSVZkMWN5RzdUOVpyajIzQkxVTDVNQjFSMi1Md1ZfdzFjYWhadTRiTVZBaXl2MGpzblVzM09NOGZZbjlMOUVmQXVZWHo3alEzWVVWZW5McFMxUWpnTkE9PQ==',
# '2026-05-03 23:36:52.706873', 
# '2026-05-03 23:36:52.706882'
# )
