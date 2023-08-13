class Presentation:
    @staticmethod
    def welcome() -> None:
        print("***************************************************************")
        print("Welcome to Hangman!")
        print("***************************************************************")

    @staticmethod
    def register_login_options() -> None:
        print("In Order to start a game you should choose option from bellow:")
        print("***************************************************************")
        print("1.Register user\n2.Login\n3.Exit")
        print("***************************************************************")

    @staticmethod
    def register_introduction() -> None:
        print("For account creation we need to reciev fallowing information: ")
        print("***************************************************************")

    @staticmethod
    def seprarator_between_lines() -> None:
        print("***************************************************************")

    @staticmethod
    def show_users_registration_entries(name: str, email: str, password: str) -> None:
        print("You have provided following information:")
        print("***************************************************************")
        print(f"Yours name: {name}")
        print("***************************************************************")
        print(f"Yours email: {email}")
        print("***************************************************************")
        print(f"Yours password: {password}")
        print("***************************************************************")

    @staticmethod
    def email_is_already_in_use() -> None:
        print("Please provide diffrent email! This one is already in use!")

    @staticmethod
    def is_all_information_correct() -> None:
        print("Is information that have you provided correct? Y/n")

    @staticmethod
    def show_users_email(email: str) -> None:
        print(f"Your email - {email}")
