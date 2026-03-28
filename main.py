import sqlite3
from querying.create_user import create_user
from querying.validate_user import validate_user

BANNER = """
 ___       _                    _       ____                                         _   __  __
/ _ \   __| | __ _ _ __ ___   ( )___  |  _ \ __ _ ___ _____      _____  _ __ __| | |  \/  | __ _ _ __   __ _  __ _  ___ _ __
| |_| | / _` |/ _` | '_ ` _ \ |// __| | |_) / _` / __/ __\\ \\ /\\ / / _ \| '__/ _` | | |\/| |/ _` | '_ \\ / _` |/ _` |/ _ \\ '__|
|  _  || (_| | (_| | | | | | |   \\__ \\ |  __/ (_| \\__ \\__ \\\\ V  V / (_) | | | (_| | | |  | | (_| | | | | (_| | (_| |  __/ |
|_| |_| \\__,_|\\__,_|_| |_| |_|   |___/ |_|   \\__,_|___/___/ \\_/\\_/ \\___/|_|  \\__,_| |_|  |_|\\__,_|_| |_|\\__,_|\\__, |\\___|_|
                                                                                                                   |___/"""

connection = sqlite3.connect("password_manager.db")
cursor = connection.cursor()

def home():
    print(BANNER)
    print("zero-knowledge. AES encrypted.")
    print("")
    print("1. Login")
    print("2. create an account")
    print("Select ctrl + c to exit")
    user_login_input = int(input("select and option "))
    if user_login_input == 1:
        login()
    elif user_login_input == 2:
        create_account()
    elif user_login_input == 3:
        exit()
    else:
        print("INVALID OPTION SELECTED. PLEASE TRY AGAIN.")
        home()



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
            login()
        else:
            print("An error occured when creating an account, please try again later.")
            home()


def login():
    print("********************LOGIN********************")
    username_input = str(input("ENTER USERNAME: "))
    master_password_input = str(input("ENTER MASTER PASSWORD: "))
    login_result = validate_user(
        username_input,
        master_password_input
    )
    if login_result == True:
        print("You have successfully logined in. Please continue.")
        user_interface(username_input, master_password_input)
    elif login_result == False:
        print("Incorrect username or password. Please Try again.")
        login()
    else:
        print("This user does not exist. Please register for an account.")
        create_account()

    



def user_interface(username, master_password):
    print("********************SELECT AN OPTION***************")
    print("1. Change password")
    print("2. Create vault")
    print("3. View vaults")
    print("4. Logout")
    user_input = int(input("Please enter your select: "))
    

if __name__ == '__main__':  
    # home()
    login()
