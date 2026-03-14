def login():
    print("********************PASSWORD MANAGER********************")
    print("********************SELECT AN OPTION********************")
    print("1. LOGIN")
    print("2. CREATE AN ACCOUNT")
    print("3. EXIT)
    user_login_input = int(input("ENTER OPTION HERE"))

    if user_login_input == 1:
        login()
    elif user_login_input == 2:
        create_account()
    elif user_login_input == 3:
        exit()
    else:
        print("INVALID OPTION SELECTED. PLEASE TRY AGAIN")



def create_account():
    print("********************CREATE ACCOUNT********************")
    username_input = str(input("ENTER USERNAME: "))
    master_password_input = str(input("ENTER MASTER PASSWORD "))

    if len(username_input) < 3 or len(mater_password_input)) < 3:
        print("INVALID USERNAME OR PASSWORD")

def login():
    print("********************LOGIN********************")
    username_input = str(input("ENTER USERNAME: "))
    master_password_input = str(input("ENTER MASTER PASSWORD: "))


if __name__ == '__main__':
    login()
