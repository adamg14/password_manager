from cli.user_interface import user_interface

from api.create_vault import create_valut

import time


def handle_create_vault(
        username,
        master_password
):
    vault_name = str(input("Enter the name of the new vault: "))
    vault_creation = create_valut(
        username,
        master_password,
        vault_name  
    )

    if vault_creation:
        print(f"The new vault ({vault_name}) was created successfully.")
        time.sleep(5)
        user_interface(
            username,
            master_password
        )
    else:
        print("There was an error that occurred when creating the vault. Please try again later.")
        user_interface(
            username,
            master_password
        )