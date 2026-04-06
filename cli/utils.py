def get_number(prompt, valid_selection):
    while True:
        try:
            number = int(input(prompt))
            if number in valid_selection:
                return number
            else:
                raise ValueError
        except ValueError:
            print("Invalid selection.")
