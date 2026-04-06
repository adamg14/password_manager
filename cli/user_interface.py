from cli.utils import get_number
from cli.handle_password_change import handle_password_change
from cli.handle_create_vault import handle_create_vault
from cli.handle_view_vaults import handle_view_vaults
from cli.handle_select_vault import handle_select_vault
from cli.home import home


def user_interface(username, master_password):
    print("********************SELECT AN OPTION***************")
    print("1. Change password")
    print("2. Create vault")
    print("3. View vaults")
    print("4. Select a vault")
    print("5. Logout")
    user_input = get_number("Please enter your selection: ", [1, 2, 3, 4, 5])

    if user_input == 1:
        handle_password_change(username, master_password)

    elif user_input == 2:
        handle_create_vault(username, master_password)

    elif user_input == 3:
        handle_view_vaults(username, master_password)

    elif user_input == 4:
        handle_select_vault(username, master_password)

    elif user_input == 5:
        del username
        del master_password
        home()
