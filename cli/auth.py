from api.create_user import create_user
from api.validate_user import validate_user


def login():
    print("********************LOGIN********************")
    username_input = str(input("Enter username: "))
    master_password_input = str(input("Enter master password: "))
    return username_input, master_password_input


def handle_login():
    username, password = login()
    login_result = validate_user(username, password)

    if login_result:
        print("You have successfully logged in. Please continue.")
        from cli.user_interface import user_interface
        user_interface(username, password)
    elif login_result == False:
        print("Incorrect username or password. Please try again.")
        handle_login()
    else:
        print("This user does not exist. Please register for an account.")
        create_account()


def create_account():
    print("********************CREATE ACCOUNT********************")
    username_input = str(input("Enter username: "))
    master_password_input = str(input("Enter password: "))

    if len(username_input) < 3 or len(master_password_input) < 3:
        print("INVALID USERNAME OR PASSWORD")
    else:
        creation_result = create_user(
            username=username_input,
            master_password=master_password_input
        )
        if creation_result:
            print("Creation successful. You are now able to login")
            handle_login()
        else:
            print("An error occurred when creating an account, please try again later.")
            from cli.home import home
            home()
