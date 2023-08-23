# pylint: skip-file
from presentation_layer import Presentation
from utility import (
    get_user_option,
    get_user_name,
    get_user_email,
    get_user_password,
    get_y_n_value,
    hash_user_password,
    three_times_login_checker,
    get_letter,
    is_email_valid,
)
from db_layer import MongoDB
from sys import exit
from loggers.log_to_console import console_logger
from loggers.log_to_file import file_logger
from game_layer import Game
from json_schemas import (
    user_validation_rules,
    games_validation_rules,
    word_validation_rules,
)


def register_service() -> None:
    """This function registers account with provided name, email, password. It could exit from app ar redirect to login services."""
    Presentation.register_introduction()
    name = get_user_name()
    Presentation.seprarator_between_lines()
    while True:
        email = get_user_email()
        if is_email_valid(email):
            db_response = db.is_email_used("users", email=email)
            if db_response:
                file_logger.info(f"{email} is already in use!")
                Presentation.email_is_already_in_use()
                continue
            elif db_response == None:
                console_logger.info(
                    "We encountered unexpected error. Try latter! Exiting the program!"
                )
                file_logger.critical(
                    "There is issues with db, there should be log upper!"
                )
                exit()
            else:
                break
        else:
            file_logger.info("User have provided bad email.")
            console_logger.info(f"Please provide valid email!")
            continue
    Presentation.seprarator_between_lines()
    password = get_user_password()
    Presentation.seprarator_between_lines()
    Presentation.show_users_registration_entries(
        name=name, email=email, password=password
    )
    Presentation.is_all_information_correct()
    is_values_correct = get_y_n_value()
    Presentation.seprarator_between_lines()
    if is_values_correct == "y":
        hashed_user_password = hash_user_password(password)
        result = db.create_user(
            "users", name=name, email=email, password=hashed_user_password
        )
        if result != None:
            console_logger.info(f"You have successfully registered account!")
            file_logger.info(f" User {result} created.")
            login_service_after_registration(email)
        else:
            file_logger.warning("Connection to db was lost!")
            console_logger.info(
                "We have encountered some kind of troubles! We are redirecting you to main menu!"
            )
            app_run()
    else:
        register_service()


def login_service_after_registration(email: str) -> None:
    """Funcion check if password is correct and redirects to game service or exit's"""
    Presentation.seprarator_between_lines()
    Presentation.show_user_email(email=email)
    password_validation_result = three_times_login_checker(
        "0.0.0.0", "27017", "final_task", email=email
    )
    if password_validation_result:
        game_service(email)
    else:
        file_logger.info(
            f"User provided bad pasword for three times. System shuts down!"
        )
        console_logger.info(
            "You have provided bad password three times, system shuts down!"
        )
        exit()


def login_service() -> None:
    """Funcions checks if email is valid and validates password. If everything is good, redirect to game service else exits system"""
    Presentation.login_introduction()
    Presentation.seprarator_between_lines()
    while True:
        email = get_user_email()
        if is_email_valid(email):
            break
        else:
            file_logger.info("User have provided bad email.")
            console_logger.info(f"Please provide valid email!")
            continue
    Presentation.seprarator_between_lines()
    password_validation_result = three_times_login_checker(
        "0.0.0.0", "27017", "final_task", email=email
    )
    if password_validation_result:
        game_service(email)
    else:
        file_logger.info(
            f"User provided bad pasword for three times. System shuts down!"
        )
        console_logger.info(
            "You have provided bad password three times, system shuts down!"
        )
        exit()


def game_service(email: str) -> None:
    "Funcions get user, checks if it is and redirect to history or game, according to user preferences."
    account_info = db.get_user("users", email=email)
    if account_info == None:
        console_logger.info(
            "We have issued unexpected error! System is going to shut down!"
        )
        file_logger.warning("Connection to db is lost!")
        exit()
    Presentation.seprarator_between_lines()
    Presentation.game_introduction()
    option = get_user_option()
    if option == 1:
        game(str(account_info["_id"]), str(account_info["name"]))
    elif option == 2:
        history(str(account_info["_id"]), str(account_info["name"]))
    else:
        exit()


def game(user_id: str, user_name: str) -> None:
    "Funcion runs whole pressentation part and request to game object. After the game makes CRUD operation and redirect to game history."
    Presentation.seprarator_between_lines()
    Presentation.play_a_game(user_name=user_name)
    db.create_collection("words")
    if db.set_up_schema_validator("words", word_validation_rules) is None:
        console_logger.info(
            "We have issued unexpected error! System is going to shut down!"
        )
        file_logger.warning("Connection to db is lost!")
        exit()
    db.create_words_for_game("words")
    game = Game(user_id, db.get_random_word("words"))
    game.fill_guessing_word_with_special_char()
    if game.get_word() == None:
        console_logger.info(
            "We have issued unexpected error! System is going to shut down!"
        )
        file_logger.warning("Connection to db is lost!")
        exit()
    Presentation.show_guessing_word(game.get_guessing_word())
    while True:
        Presentation.seprarator_between_lines()
        game.accept_letter_for_game(get_letter())
        if game.get_game_status() == True:
            Presentation.congratule_player(user_name=user_name)
            word = game.get_word()
            lifes_left = game.get_lifes_count()
            incorect_guessed_letters = game.get_incorrect_guesed_letters()
            letters_left = game.get_left_letters()
            db.add_game(
                "games",
                user_id=user_id,
                word=word,
                lifes_left=lifes_left,
                incorrect_guessed_letters=incorect_guessed_letters,
                letters_left=letters_left,
                game_status=True,
            )
            db.drop_collection("words")
            history(user_id=user_id, user_name=user_name)
            break
        elif game.get_lifes_count() > 0:
            Presentation.seprarator_between_lines()
            Presentation.show_guessing_word(game.get_guessing_word())
            Presentation.seprarator_between_lines()
            lifes_left = game.get_lifes_count()
            Presentation.show_lifes_left(lifes_left)
            Presentation.seprarator_between_lines()
            Presentation.hangman_visualization(lifes_left)
            Presentation.seprarator_between_lines()
            Presentation.show_wrong_typed_letters(game.get_incorrect_guesed_letters())
            Presentation.seprarator_between_lines()
            Presentation.show_unused_letters(game.get_left_letters())
            continue
        else:
            if game.get_lifes_count() == 0:
                Presentation.seprarator_between_lines()
                lifes_left = game.get_lifes_count()
                Presentation.hangman_visualization(lifes_left)
                Presentation.seprarator_between_lines()
                Presentation.show_message_for_lose(user_name)
                word = game.get_word()
                incorect_guessed_letters = game.get_incorrect_guesed_letters()
                letters_left = game.get_left_letters()
                db.add_game(
                    "games",
                    user_id=user_id,
                    word=word,
                    lifes_left=lifes_left,
                    incorrect_guessed_letters=incorect_guessed_letters,
                    letters_left=letters_left,
                    game_status=False,
                )
                db.drop_collection("words")
                history(user_id=user_id, user_name=user_name)
                break


def history(user_id: str, user_name: str) -> None:
    """Funcion shows all game history."""
    Presentation.history_greet(user_name)
    all_games = db.get_all_games("games", user_id)
    Presentation.seprarator_between_lines()
    if all_games != None:
        Presentation.history_representation(all_games)
    else:
        console_logger.info(
            "We have issued unexpected error! System is going to shut down!"
        )
        file_logger.warning("Connection to db is lost!")
        exit()


def app_run() -> None:
    """Method redirects to login or registration services or simply exits app."""
    Presentation.welcome()
    Presentation.register_login_options()
    option = get_user_option()
    if option == 1:
        register_service()
    elif option == 2:
        login_service()
    else:
        exit()


if __name__ == "__main__":
    db = MongoDB("0.0.0.0", "27017", "final_task")
    db.create_collection("users")
    if db.set_up_schema_validator("users", user_validation_rules) is None:
        file_logger.warning(
            "We have encountered error with error which occured in setting up validation schema."
        )
    db.create_collection("games")
    if db.set_up_schema_validator("games", games_validation_rules) is None:
        file_logger.warning(
            "We have encountered error with error which occured in setting up validation schema."
        )

    app_run()
