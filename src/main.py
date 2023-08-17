from presentation_layer import Presentation
from utility import (
    get_user_option,
    get_user_name,
    get_user_email_with_validator,
    get_user_password,
    get_y_n_value,
    hash_user_password,
    three_times_login_checker,
    get_letter,
)
from db_layer import MongoDB
from sys import exit
from loggers.log_to_console import console_logger
from loggers.log_to_file import file_logger
from game_layer import Game


def register_service() -> None:
    Presentation.register_introduction()
    name = get_user_name()
    Presentation.seprarator_between_lines()
    while True:
        email = get_user_email_with_validator()
        db_responce = db.is_email_unused("users", email=email)
        if db_responce == False:
            file_logger.info(f"{email} is already in use!")
            Presentation.email_is_already_in_use()
            continue
        elif db_responce == None:
            console_logger.info(
                "We encountered unexpected error. Try latter! Exiting the program!"
            )
            file_logger.critical("There is issues with db, there should be log upper!")
            exit()
        else:
            break
    Presentation.seprarator_between_lines()
    password = get_user_password()
    Presentation.seprarator_between_lines()
    Presentation.show_users_registration_entries(
        name=name, email=email, password=password
    )
    Presentation.is_all_information_correct()
    all_values_correct = get_y_n_value()
    Presentation.seprarator_between_lines()
    if all_values_correct == "y":
        hashed_user_password = hash_user_password(password)
        result = db.crate_user(
            "users", name=name, email=email, password=hashed_user_password
        )
        if result != "":
            console_logger.info(f"You have successfully registered account!")
            login_service_after_registration(email)
        else:
            console_logger.info(
                "We have encountered some kind of troubles! We are redirecting you to registration form!"
            )
            register_service()
    else:
        register_service()


def login_service_after_registration(email: str) -> None:
    Presentation.seprarator_between_lines()
    Presentation.show_users_email(email=email)
    password_validation_result = three_times_login_checker(
        "0.0.0.0", "27017", "final_task", email=email
    )
    if password_validation_result is True:
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
    Presentation.login_introduction()
    Presentation.seprarator_between_lines()
    email = get_user_email_with_validator()
    Presentation.seprarator_between_lines()
    password_validation_result = three_times_login_checker(
        "0.0.0.0", "27017", "final_task", email=email
    )
    if password_validation_result is True:
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
    Presentation.seprarator_between_lines()
    Presentation.play_a_game(user_name=user_name)
    game = Game(user_id, db.get_random_word("words"))
    if game.get_word() == None:
        console_logger.info(
            "We have issued unexpected error! System is going to shut down!"
        )
        file_logger.warning("Connection to db is lost!")
        exit()
    Presentation.seprarator_between_lines()
    while:
        Presentation.seprarator_between_lines()
        game.accept_letter_for_game(get_letter())
        if game.get_game_status() == True:
            Presentation.congratule_player(user_name=user_name)
            word = game.get_word()
            lives_left = game.get_lives_count()
            incorect_guessed_letters = game.get_guesed_letters()
            letters_left = game.get_left_letters()

            db.add_game(
                "games",
                user_id=user_id,
                word=word,
                lives_left=lives_left,
                incorrect_guessed_letters=incorect_guessed_letters,
                letters_left=letters_left,
            )
            history(user_id=user_id, user_name=user_name)
            break
        elif game.get_lives_count> 0:



def history(user_id: str, user_name: str) -> None:
    pass


def app_run() -> None:
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
    db.create_collection("words")
    db.create_words_for_game("words")
    app_run()
    db.drop_collection("words")
