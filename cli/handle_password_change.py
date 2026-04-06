import time
from api.update_master_password import update_master_password
from cli.user_interface import user_interface


def handle_password_change(username, master_password):
    old_password = str(input("Enter your current password: "))
    new_password = str(input("Enter your new password: "))

    result = update_master_password(username, old_password, new_password)

    if result:
        print("Password updated. All vault keys have been re-encrypted.")
        time.sleep(2)
        user_interface(username, new_password)
    else:
        print("Failed to update password. Check your current password and try again.")
        time.sleep(2)
        user_interface(username, master_password)