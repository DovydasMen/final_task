# pylint: skip-file
import re
from typing import Optional, Union

from db_layer import MongoDB
from loggers.log_to_console import console_logger
from loggers.log_to_file import file_logger


def get_user_option() -> int:
    """Funcion returns values only from 1 to 3, other options is not valid."""
    while True:
        try:
            selection = int(input("Your selection: "))
            if selection <= 0 or selection > 3:
                console_logger.info("Please choose values from 1 to 3")
                continue
        except ValueError:
            console_logger.info("Please write numbers!")
            file_logger.info(f"User written wrong value input!")
        except Exception as e:
            console_logger.info(
                "We have encountered unexpected error!", str(e), "Try again!"
            )
            file_logger.info("User written wrong input!")
            continue
        else:
            break
    return selection


def get_user_name() -> str:
    """Function returs user name as a string."""
    while True:
        try:
            user_name = input("Name: ").rstrip().lstrip()
        except Exception as e:
            console_logger.info(
                "We have encountered unexpected error!", str(e), "Try again!"
            )
            file_logger.info("User written wrong input!")
            continue
        else:
            break
    return user_name


def get_user_email() -> str:
    """Function returs email as a string"""
    while True:
        try:
            user_email = input("Email: ").rstrip().lstrip()
        except Exception as e:
            console_logger.info(
                "We have encountered unexpected error!", str(e), "Try again!"
            )
            file_logger.info("User written wrong input!")
            continue
        else:
            break
    return user_email


def is_email_valid(user_email: str) -> bool:
    """Function returs bool value, for email validation there is used regex expresion."""
    regex = re.compile(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    )
    if re.fullmatch(regex, user_email):
        return True
    return False


def get_user_password() -> str:
    """Function returs users password as a string."""
    while True:
        try:
            user_password = input("Password: ").rstrip().lstrip()
        except Exception as e:
            console_logger.info(
                "We have encountered unexpected error!", str(e), "Try again!"
            )
            file_logger.info("User written wrong input!")
            continue
        else:
            break
    return user_password


def hash_user_password(password: str) -> str:
    """Function hashes password."""
    hashed_password = password + "whysoserious?"
    return hashed_password


def get_y_n_value() -> str:
    """Funcion returs only y or n as a string value."""
    while True:
        try:
            y_n_value = input("Your selection: ").rstrip().lstrip().lower()
            if len(y_n_value) > 1:
                print("You have entered more than 1 symbol!")
                file_logger.info("There was provided more then one symbol!")
                continue
            elif "y" in y_n_value:
                break
            elif "n" in y_n_value:
                break
            else:
                console_logger.info("Please select Y letter or N letter!")
                file_logger.info(
                    f"User doesn't provided correct values! Value = {y_n_value}"
                )
                continue
        except Exception as e:
            console_logger.info(
                "We have encountered unexpected error!", str(e), "Try again!"
            )
            file_logger.info("User written wrong input!")
            continue
    return y_n_value


def three_times_login_checker(
    host: str, port: str, database_name: str, email: str
) -> Optional[Union[str, bool]]:
    """Function chechks if password and provided email is correct withing the values in db."""
    db = MongoDB(host=host, port=port, database_name=database_name)
    max_tries = 3
    tries = 0
    while tries < max_tries:
        password = get_user_password()
        hashed_pasword = hash_user_password(password=password)
        db_response = db.check_login("users", email=email, password=hashed_pasword)
        if db_response == False:
            tries += 1
            console_logger.info("You have provided bad password!")
            continue
        elif db_response == "":
            file_logger.info("We don't have such account in our system!")
            return ""
        elif db_response == None:
            console_logger.info(
                "We encountered unexpected error. Try latter! Exiting the program!"
            )
            file_logger.critical("There is issues with db, there should be log upper!")
            exit()
        else:
            break
    return db_response


def get_letter() -> str:
    """Functions returs letters as a string. Letter is going to be upper cased."""
    while True:
        try:
            letter = input("Please type letter: ").rstrip().lstrip().upper()
            if len(letter) > 1:
                console_logger.info("You have entered more than 1 symbol!")
                file_logger.info("There was provided more then one symbol!")
                continue
            elif letter.isalpha():
                break
            else:
                console_logger.info("Please select only letters!")
                file_logger.info(
                    f"User doesn't provided correct values! Value = {letter}"
                )
                continue
        except Exception as e:
            console_logger.info(
                "We have encountered unexpected error!", str(e), "Try again!"
            )
            file_logger.info("User written wrong input!")
            continue
    return letter


if __name__ == "__main__":
    # db = MongoDB("0.0.0.0", "27017", "final_task")
    print(is_email_valid("dejau@regexo.lt"))
