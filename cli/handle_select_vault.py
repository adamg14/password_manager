from cli.user_interface import user_interface
from cli.utils import get_number

from api.get_vaults import get_vaults
from api.retrieve_vault import retrieve_vault

import time


def handle_select_vault(
          username,
          master_password
):

    vaults_response = get_vaults(username)

    if len(vaults_response) == 0:
        print("You currently do not have any vaults.")
        time.sleep(2)
        user_interface(username, master_password)
    else:
        counter = 1
        for vault in vaults_response:
            print(f"Vault {counter}: {vault[0]}")
        
        user_selection = get_number("Please select a vault", [i for i in range(1, counter)])

        selected_vault = retrieve_vault(username, vaults_response[user_selection - 1][0])

        if selected_vault:
            return selected_vault
        else:
            print("An error has occrred when trying to retrieve the vault. Please try again later.")
            


