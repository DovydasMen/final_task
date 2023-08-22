# pylint: skip-file
from loggers.log_to_console import console_logger
from loggers.log_to_file import file_logger
from db_layer import MongoDB
from typing import Optional

import re


def get_user_option() -> int:
    while True:
        try:
            selection = int(input("Your selection: "))
            if selection <= 0 or selection > 3:
                console_logger.info("Please choose values from 1 to 3")
                continue
        except ValueError:
            print("Please write numbers!")
            file_logger.info(f"User written wrong value input!")
        except Exception as e:
            print("We have encountered unexpected error!", str(e), "Try again!")
            file_logger.info("User written wrong input!")
            continue
        else:
            break
    return selection


def get_user_name() -> str:
    while True:
        try:
            user_name = input("Name: ").rstrip().lstrip()
        except Exception as e:
            print("We have encountered unexpected error!", str(e), "Try again!")
            file_logger.info("User written wrong input!")
            continue
        else:
            break
    return user_name


def get_user_email() -> str:
    while True:
        try:
            user_email = input("Email: ").rstrip().lstrip()
        except Exception as e:
            print("We have encountered unexpected error!", str(e), "Try again!")
            file_logger.info("User written wrong input!")
            continue
        else:
            break
    return user_email


def is_email_valid(user_email: str) -> bool:
    regex = re.compile(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    )
    if re.fullmatch(regex, user_email):
        return True
    return False


def get_user_password() -> str:
    while True:
        try:
            user_password = input("Password: ").rstrip().lstrip()
        except Exception as e:
            print("We have encountered unexpected error!", str(e), "Try again!")
            file_logger.info("User written wrong input!")
            continue
        else:
            break
    return user_password


def hash_user_password(password: str) -> str:
    hashed_password = password + "whysoserious?"
    return hashed_password


def get_y_n_value():
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
                print("Please select Y letter or n letter!")
                file_logger.info(
                    f"User doesn't provided correct values! Value = {y_n_value}"
                )
                continue
        except Exception as e:
            print("We have encountered unexpected error!", str(e), "Try again!")
            file_logger.info("User written wrong input!")
            continue
    return y_n_value


def three_times_login_checker(
    host: str, port: str, database_name: str, email: str
) -> Optional[bool]:
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
    while True:
        try:
            # is alpha!
            letter = input("Please type letter: ").rstrip().lstrip().upper()
            if len(letter) > 1:
                print("You have entered more than 1 symbol!")
                file_logger.info("There was provided more then one symbol!")
                continue
            elif letter.isalpha():
                break
            else:
                print("Please select only letters!")
                file_logger.info(
                    f"User doesn't provided correct values! Value = {letter}"
                )
                continue
        except Exception as e:
            print("We have encountered unexpected error!", str(e), "Try again!")
            file_logger.info("User written wrong input!")
            continue
    return letter


if __name__ == "__main__":
    # db = MongoDB("0.0.0.0", "27017", "final_task")
    print(is_email_valid("dejau@regexo.lt"))
