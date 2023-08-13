from presentation_layer import Presentation
from utility import (
    get_user_option,
    get_user_name,
    get_user_email_with_validator,
    get_user_password,
    get_y_n_value,
    hash_user_password,
    three_times_login_checker,
)
from db_layer import MongoDB
from sys import exit
from loggers.log_to_console import console_logger
from loggers.log_to_file import file_logger


def register_service() -> None:
    Presentation.register_introduction()
    name = get_user_name()
    Presentation.seprarator_between_lines()
    while True:
        email = get_user_email_with_validator()
        if db.is_email_unused("users", email=email) == False:
            file_logger.info(f"{email} is already in use!")
            Presentation.email_is_already_in_use()
            continue
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
    validation_result = three_times_login_checker(
        "0.0.0.0", "27017", "final_task", email=email
    )
    if validation_result is True:
        game()
    else:
        file_logger.info(
            f"User provided bad pasword for three times. System shuts down!"
        )
        console_logger.info(
            "You have provided bad password three times, system shuts down!"
        )
        exit()


def login_service() -> None:
    print("login service")


def game() -> None:
    print("Hello from game!")


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
    app_run()
