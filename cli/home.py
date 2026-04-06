from cli.auth import handle_login, create_account

BANNER = """
 ___       _                    _       ____                                         _   __  __
/ _ \   __| | __ _ _ __ ___   ( )___  |  _ \ __ _ ___ _____      _____  _ __ __| | |  \/  | __ _ _ __   __ _  __ _  ___ _ __
| |_| | / _` |/ _` | '_ ` _ \ |// __| | |_) / _` / __/ __\\ \\ /\\ / / _ \| '__/ _` | | |\/| |/ _` | '_ \\ / _` |/ _` |/ _ \\ '__|
|  _  || (_| | (_| | | | | | |   \\__ \\ |  __/ (_| \\__ \\__ \\\\ V  V / (_) | | | (_| | | |  | | (_| | | | | (_| | (_| |  __/ |
|_| |_| \\__,_|\\__,_|_| |_| |_|   |___/ |_|   \\__,_|___/___/ \\_/\\_/ \\___/|_|  \\__,_| |_|  |_|\\__,_|_| |_|\\__,_|\\__, |\\___|_|
                                                                                                                   |___/"""

menu_options = {
    "1": ("Login", handle_login),
    "2": ("Create Account", create_account),
}


def home():
    print(BANNER)
    print("zero-knowledge. AES encrypted.")
    for key, (label, _) in menu_options.items():
        print(f"{key}. {label}")

    print("Select ctrl + c to exit")
    choice = str(input("select an option: "))
    action = menu_options.get(choice, None)
    if action:
        label, label_function = action
        label_function()
    else:
        print("invalid select. please try again.")
