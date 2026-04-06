from api.get_vaults import get_vaults
from cli.user_interface import user_interface

import time


def handle_view_vaults(username, master_password):
    vaults_response = get_vaults(username)

    if len(vaults_response) == 0:
        print("You currently do not have any vaults.")
        time.sleep(2)
    else:
        counter = 1
        for vault in vaults_response:
            print(f"{counter}. {vault[0]}")
            counter += 1

    user_interface(username, master_password)
