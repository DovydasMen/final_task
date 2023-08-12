from presentation_layer import Presentation
from utility import (
    get_user_option,
    get_user_name,
    get_user_email_with_validator,
    get_user_password,
)
from db_layer import MongoDB
from sys import exit


def register_service() -> None:
    Presentation.register_introduction()
    name = get_user_name()
    Presentation.seprarator_between_lines()
    while True:
        email = get_user_email_with_validator()
        if db.is_email_unused("users", email=email) == False:
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


def login_service_after_registration(email: str) -> None:
    pass


def login_service() -> None:
    print("login service")


def game() -> None:
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
    app_run()
