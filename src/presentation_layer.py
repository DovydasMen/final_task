from typing import Any, Dict, List
from loggers.log_to_console import console_logger


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
        console_logger.info(
            "Please provide diffrent email! This one is already in use!"
        )

    @staticmethod
    def is_all_information_correct() -> None:
        print("Is information that have you provided correct? Y/n")

    @staticmethod
    def show_user_email(email: str) -> None:
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
        print("\n")
        for letter in letters:
            print(letter, end=" ")
        print("\n")

    @staticmethod
    def show_wrong_typed_letters(letters: List[str]) -> None:
        if letters == [] and len(letters) == 0:
            print("You have still guessed all letters correctly!")
        else:
            print("Here is all wrong letters that you typed in:")
            Presentation.seprarator_between_lines()
            print("\n")
            for letter in letters:
                print(letter, end=" ")
            print("\n")

    @staticmethod
    def hangman_visualization(lifes_left: int) -> None:
        if lifes_left == 10:
            print("You have all lifes left. So there is no structure of hangman!")
        elif lifes_left == 9:
            print("{{{}}}")
        elif lifes_left == 8:
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print(" {{{}}}")
        elif lifes_left == 7:
            print("   __________")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print(" {{{}}}")
        elif lifes_left == 6:
            print("   __________")
            print("   |         |")
            print("   |         |")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print(" {{{}}}")
        elif lifes_left == 5:
            print("   __________")
            print("   |         |")
            print("   |         |")
            print("   |         O ")
            print("   |   ")
            print("   |   ")
            print("   |   ")
            print(" {{{}}}")
        elif lifes_left == 4:
            print("   __________")
            print("   |         |")
            print("   |         |")
            print("   |         O ")
            print("   |         |")
            print("   |         |")
            print("   |   ")
            print(" {{{}}}")
        elif lifes_left == 3:
            print("   __________")
            print("   |         |")
            print("   |         |")
            print("   |         O ")
            print("   |        (|")
            print("   |         |")
            print("   |   ")
            print(" {{{}}}")
        elif lifes_left == 2:
            print("   __________")
            print("   |         |")
            print("   |         |")
            print("   |         O ")
            print("   |        (|)")
            print("   |         |")
            print("   |   ")
            print(" {{{}}}")
        elif lifes_left == 1:
            print("   __________")
            print("   |         |")
            print("   |         |")
            print("   |         O ")
            print("   |        (|)")
            print("   |         |")
            print("   |        (")
            print(" {{{}}}")
        elif lifes_left == 0:
            print("   __________")
            print("   |         |")
            print("   |         |")
            print("   |         O ")
            print("   |        (|)")
            print("   |         |")
            print("   |        ( )")
            print(" {{{}}}")

    @staticmethod
    def show_lifes_left(lifes: int) -> None:
        if lifes == 1:
            print(f"You have {lifes} life left.")
        else:
            print(f"You still have {lifes} lifes left.")

    @staticmethod
    def show_message_for_lose(user_name: str) -> None:
        print(f"Sorry {user_name}! You ran out of lifes! That means it's lost! ")

    @staticmethod
    def show_guessing_word(word_in_list: List[str]) -> None:
        print("This is your guessing word:")
        print("\n")
        for letter in word_in_list:
            print(letter, end=" ")
        print("\n")

    @staticmethod
    def history_greet(user_name: str) -> None:
        print(f"{user_name.title()}, this is yours all games history:")

    @staticmethod
    def history_representation(games: List[Dict[str, Any]]) -> None:
        for game_information in games:
            if game_information["game_status"] == "True":
                print("You have won this game!")
            else:
                print("You lost this game!")
            print(f"Your game word was {game_information['guessing_word']}.")
            print(f"There was {game_information['lifes_left']} lifes left!")
            print(
                f"This is incorrect letters that you gave used - {game_information['incorrect_guessed_letters']}."
            )
            print(f"These letters was selected {game_information['letter_left']}.")
            Presentation.seprarator_between_lines()
