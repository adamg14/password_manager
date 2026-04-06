from cli.vault import create_valut
from user_interface import user_interface


def handle_view_vaults(
        username,
        master_password
):
    vault_name_input = str(input("Enter a name for your vault (e.g. GMail): "))
    
    vault_creation = create_valut(username, master_password, vault_name_input)

    if vault_creation:
        print("Your vault has been created successfully.")
        user_interface(
            username,
            master_password
        )
    else:
        print("An error occurred during the creation of the vault. Please try again.")
        user_interface(
            username,
            master_password
        )