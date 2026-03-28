from .get_user import get_user
from crypto.hashing import generated_hash

import sqlite3

connection = sqlite3.connect("../password_manager.db")
cursor = connection.cursor()


def validate_user(
    username,
    master_password
):
    user = get_user(username)
    if user:
        stored_master_password = user[1]
        if stored_master_password == generated_hash(master_password=master_password):
            return  True
        else:
            return False
    else:
        return "user does not exist. please try again."


