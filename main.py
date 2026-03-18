from db import create_user


def home():
    print("********************PASSWORD MANAGER********************")
    print("********************SELECT AN OPTION********************")
    print("1. LOGIN")
    print("2. CREATE AN ACCOUNT")
    print("3. EXIT")
    user_login_input = int(input("ENTER YOUR OPTION HERE: "))

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
    username_input = str(input("ENTER USERNAME: "))
    master_password_input = str(input("ENTER MASTER PASSWORD: "))

    if len(username_input) < 3 or len(master_password_input) < 3:
        print("INVALID USERNAME OR PASSWORD")
    else:
        creation_result = create_user(
            username_input,
            master_password_input
        )
        if creation_result == "User created successfully.":
            login()
        else:
            print("AN ERROR OCCURRED WHEN CREATING A USER. PLEASE TRY AGAIN LATER.")
            create_account()



def login():
    print("********************LOGIN********************")
    username_input = str(input("ENTER USERNAME: "))
    master_password_input = str(input("ENTER MASTER PASSWORD: "))


def user_interface():
    print("********************HOME PAGE********************")
    print("********************SELECT AN OPTION***************")
    print("1. Create new passord")
    print("2. Get a current password")
    print("3. Delete a password")
    print("4. Logout")
    user_input = int(input("Please enter your select: "))
    

if __name__ == '__main__':  
    home()
