# This file needs a further refactoring 
def vault_interface(username, master_password, vault_details):
    counter = 1
    for vault in vault_details:
        print(f"{counter}. {vault[0]}")
        counter += 1
    user_input = int(input("Select a vault: "))

    if user_input < 1 or user_input >= counter:
        print("Invalid selection. Please try again")
        vault_interface(username, master_password, vault_details)
    else:
        selected_vault = vault_details[user_input - 1]
        print(f"You have selected the {selected_vault[0]}.")
        print("**********OPTIONS*****")
        print("1. Create a new password")
        user_input_2 = int(input("select an option: "))
        if user_input_2 == 1:
            password_type_input = str(input("Enter the type of password (e.g. login): "))
            password_user_input = str(input("Enter the password: "))
            entry_creation_result = create_entry(
                username=username,
                master_password=master_password,
                vault_name=selected_vault[0],
                encrypted_key=selected_vault[2],
                password_type=password_type_input,
                password_input=password_user_input
            )

            if entry_creation_result:
                print("Entry created successfully.")
            else:
                print("An error occurred when trying to create the entry. Please try again later.")