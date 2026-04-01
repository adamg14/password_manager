import sqlite3
import time
from querying.create_user import create_user
from querying.validate_user import validate_user
from querying.change_password import change_master_password
from querying.create_vault import create_valut
from querying.get_vaults import get_vaults
from querying.retrieve_vault import retrieve_vault
from querying.create_entry import create_entry

BANNER = """
 ___       _                    _       ____                                         _   __  __
/ _ \   __| | __ _ _ __ ___   ( )___  |  _ \ __ _ ___ _____      _____  _ __ __| | |  \/  | __ _ _ __   __ _  __ _  ___ _ __
| |_| | / _` |/ _` | '_ ` _ \ |// __| | |_) / _` / __/ __\\ \\ /\\ / / _ \| '__/ _` | | |\/| |/ _` | '_ \\ / _` |/ _` |/ _ \\ '__|
|  _  || (_| | (_| | | | | | |   \\__ \\ |  __/ (_| \\__ \\__ \\\\ V  V / (_) | | | (_| | | |  | | (_| | | | | (_| | (_| |  __/ |
|_| |_| \\__,_|\\__,_|_| |_| |_|   |___/ |_|   \\__,_|___/___/ \\_/\\_/ \\___/|_|  \\__,_| |_|  |_|\\__,_|_| |_|\\__,_|\\__, |\\___|_|
                                                                                                                   |___/"""

connection = sqlite3.connect("password_manager.db")
cursor = connection.cursor()


def get_number(prompt, valid_selection):
    while True:
        try:
            number = int(input(prompt))
            if number in valid_selection:
                return number
            else:
                raise ValueError
        except ValueError:
            print("Invalid selection. ")


def home():
    print(BANNER)
    print("zero-knowledge. AES encrypted.")
    for key, (label, label_function) in menu_options.items():
        print(f"{key}. {label}")

    print("Select ctrl + c to exit")
    choice = str(input("select an option: "))
    action = menu_options.get(choice, None)
    if action:
        label, label_function = action
        if label_function:
            label_function()
    else:
        print("invalid select. please try again.")



def create_account():
    print("********************CREATE ACCOUNT********************")
    username_input = str(input("Enter username: "))
    master_password_input = str(input("Enter password: "))

    if len(username_input) < 3 or len(master_password_input) < 3:
        print("INVALID USERNAME OR PASSWORD")
    else:
        creation_result = create_user(
            username=username_input,
            master_password=     master_password_input
        )
        if creation_result:
            print("Creation successful. You are now able to login")
            handle_login()
        else:
            print("An error occured when creating an account, please try again later.")
            home()


def handle_login():
    username, password = login()
    login_result = validate_user(
        username,
        password
    )

    if login_result:
        return username, password
    elif login_result is False:
        print("Incorrect credentials")
        return None
    else:
        print("You have not registered")
        time.sleep(2)
        create_account()


def login():
    print("********************LOGIN********************")
    username_input = str(input("ENTER USERNAME: "))
    master_password_input = str(input("ENTER MASTER PASSWORD: "))
    return username_input, master_password_input

    
def handle_change_password(username, new_password):
    if change_master_password(
        username,
        new_password
    ):
        print("Your password has been changed.")
        time.sleep(5)
        user_interface(
            username,
            new_password
        )


def user_interface(username, master_password):
    print("********************SELECT AN OPTION***************")
    print("1. Change password")
    print("2. Create vault")
    print("3. View vaults")
    print("4. Select a vault")
    print("5. Logout")
        
    user_input = get_number("Please enter your selection: ", [1, 2, 3, 4])
    
    if user_input == 1:
        new_password = str(input("Enter your new password: "))
        handle_change_password(username, new_password)
        
        if password_change_result:
            print("Your password has been changed.")
            time.sleep(5)
            user_interface(
                username,
                user_input_2
            )
        else:
            print("An error occured. Please try again")
            time.sleep(5)
            user_interface(
                username,
                master_password
            )
    
    if user_input == 2:
        vault_name_input = str(input("Enter a name for your vault (e.g. GMail): "))

        vault_creation = create_valut(
            username,
            master_password,
            vault_name_input,
        )

        if vault_creation == True:
            print("Your vault has been created successfully.")
        else:
            print("An error occured during the creation of the vault. Please try again.")
    
    if user_input == 3:
        vaults_response = get_vaults(
            username
        )
        if len(vaults_response) == 0:
            print("You currently do not have any vaults.")
            time.sleep(2)
            user_interface(username, master_password)
        else:
            counter = 1
            for vault in vaults_response:
                print(f"{counter}. {vault[0]}")
                counter += 1
    if user_input == 4:
        vaults_response = get_vaults(
            username
        )
        vault_input = str(input("Enter the name of the vault you want to access: "))
        vault_details = retrieve_vault(
            username,
            vault_input
        )

        


def vault_interface(
        username,
        master_password,
        vault_details
):
    counter = 1
    for vault in vault_details:
        print(f"{counter}. {vault[0]}")
        counter += 1
    user_input = int(input("Select a vault: "))

    if (user_input > counter) or not isinstance(user_input, int) or (user_input <= 0):
        print("Invalid selection. Please try again")
        vault_interface(
            username,
            master_password,
            vault_details
        )
    else:
        print(f"You have selected the {vault}.")
        print("**********OPTIONS*****")
        print("1. Create a new password")
        user_input_2 = int(input("select an option: "))
        if user_input_2 == 1:
            password_type_input =  str(input("Enter the type of password (e.g. login): "))
            password_user_input = str(input("Enter the password: "))
            entry_creation_result = create_entry(
                username=username,
                master_password=master_password,
                vault_name=vault_details[0],
                encrypted_key=vault_details[2],
                password_type=password_type_input,
                password_input=password_user_input
            )

            if entry_creation_result:
                print("Entry created successfully.")
            else:
                print("An error occurred when trying to create the entry. Please try again later.")
        # option to view passwords stored in vault
        # options to delete passwords in vault
        # option to edit password in vaults

    
menu_options = {
    "1": ("Login", handle_login),
    "2": ("Create Account", create_account)

}

if __name__ == '__main__':
    while True:
        home()
