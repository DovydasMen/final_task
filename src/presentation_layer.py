from typing import List, Optional


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
        print("For account creation we need to recieve fallowing information: ")
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

    @staticmethod
    def login_introduction() -> None:
        print("For log into system please provide fallowing information: ")

    @staticmethod
    def game_introduction() -> None:
        print("This is a Hangman!")
        print("***************************************************************")
        print(
            "Following options:\n1.Play a game\n2.Look all ended game history!\n3.Exit"
        )

    @staticmethod
    def play_a_game(user_name: str) -> None:
        print(f"{user_name} we are loading your game, it could take some time!")

    @staticmethod
    def congratule_player(user_name: str) -> None:
        print(f"{user_name} You have won the game!")

    @staticmethod
    def show_unused_letters(letters: List[str]) -> None:
        print("Here is all letters that are left:")
        Presentation.seprarator_between_lines()
        for letter in letters:
            print(letter, end=" ")

    @staticmethod
    def show_wrong_typed_letters(letters: List[str]) -> None:
        print("Here is all wrong letters that you typed in:")
        Presentation.seprarator_between_lines()
        for letter in letters:
            print(letter, end=" ")

    @staticmethod
    def hangman_visualization(lives_left: int) -> None:
        if lives_left == 9:
            print("{{{}}}")
        elif lives_left == 8:
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print(" {{{}}}")
        elif lives_left == 7:
            print("   __________")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print(" {{{}}}")
        elif lives_left == 6:
            print("   __________")
            print("   |         |")
            print("   |         |")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print(" {{{}}}")
        elif lives_left == 5:
            print("   __________")
            print("   |         |")
            print("   |         |")
            print("   |         O ")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print(" {{{}}}")
        elif lives_left == 4:
            print("   __________")
            print("   |         |")
            print("   |         |")
            print("   |         O ")
            print("   |         |")
            print("   |         |")
            print("   |   ")
            print(" {{{}}}")
        elif lives_left == 3:
            print("   __________")
            print("   |         |")
            print("   |         |")
            print("   |         O ")
            print("   |        (|")
            print("   |         |")
            print("   |   ")
            print(" {{{}}}")
        elif lives_left == 2:
            print("   __________")
            print("   |         |")
            print("   |         |")
            print("   |         O ")
            print("   |        (|)")
            print("   |         |")
            print("   |   ")
            print(" {{{}}}")
        elif lives_left == 1:
            print("   __________")
            print("   |         |")
            print("   |         |")
            print("   |         O ")
            print("   |        (|)")
            print("   |         |")
            print("   |        (")
            print(" {{{}}}")
        elif lives_left == 0:
            print("   __________")
            print("   |         |")
            print("   |         |")
            print("   |         O ")
            print("   |        (|)")
            print("   |         |")
            print("   |        ( )")
            print(" {{{}}}")


if __name__ == "__main__":
    Presentation.hangman_visualization(0)
