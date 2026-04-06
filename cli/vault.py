import time

from api.change_password import change_master_password
from api.create_vault import create_valut
from api.get_vaults import get_vaults
from api.retrieve_vault import retrieve_vault
from api.create_entry import create_entry
from cli.utils import get_number


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
        password_change_result = change_master_password(username, new_password)

        if password_change_result:
            print("Your password has been changed.")
            time.sleep(5)
            user_interface(username, new_password)
        else:
            print("An error occurred. Please try again")
            time.sleep(5)
            user_interface(username, master_password)

    if user_input == 2:
        vault_name_input = str(input("Enter a name for your vault (e.g. GMail): "))
        vault_creation = create_valut(username, master_password, vault_name_input)

        if vault_creation:
            print("Your vault has been created successfully.")
        else:
            print("An error occurred during the creation of the vault. Please try again.")

    if user_input == 3:
        vaults_response = get_vaults(username)

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
        vaults_response = get_vaults(username)
        vault_input = str(input("Enter the name of the vault you want to access: "))
        vault_details = retrieve_vault(username, vault_input)


def vault_interface(username, master_password, vault_details):
    counter = 1
    for vault in vault_details:
        print(f"{counter}. {vault[0]}")
        counter += 1
    user_input = int(input("Select a vault: "))

    if (user_input > counter) or not isinstance(user_input, int) or (user_input <= 0):
        print("Invalid selection. Please try again")
        vault_interface(username, master_password, vault_details)
    else:
        print(f"You have selected the {vault}.")
        print("**********OPTIONS*****")
        print("1. Create a new password")
        user_input_2 = int(input("select an option: "))
        if user_input_2 == 1:
            password_type_input = str(input("Enter the type of password (e.g. login): "))
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
