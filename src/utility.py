from loggers.log_to_console import console_logger
from loggers.log_to_file import file_logger


def get_user_option() -> int:
    while True:
        try:
            selection = int(input("Your selection: "))
            if selection <= 0 or selection > 3:
                console_logger.info("Please choose values from 1 to 3")
                continue
        except ValueError:
            print("Please write numbers!")
            file_logger.info(f"User written wrong value input {selection} !")
        except KeyboardInterrupt:
            print("Please type in integer value!")
            file_logger.info("User written wrong input!")
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
        except KeyboardInterrupt:
            print("Please type in your name!")
            file_logger.info("User tried to paste information!")
        except Exception as e:
            print("We have encountered unexpected error!", str(e), "Try again!")
            file_logger.info("User written wrong input!")
            continue
        else:
            break
    return user_name


def get_user_email_with_validator() -> str:
    while True:
        try:
            user_email = input("Email: ").rstrip().lstrip()
            if "@" not in user_email:
                # think about .com or etc validator!
                # THINK ABOUTI F USER PROVIDES ONLY @
                file_logger.info("User provided email without @!")
                print("You provided email without special char @")
                continue
        except KeyboardInterrupt:
            print("Please type in your email!")
            file_logger.info("User tried to paste information!")
        except Exception as e:
            print("We have encountered unexpected error!", str(e), "Try again!")
            file_logger.info("User written wrong input!")
            continue
        else:
            break
    return user_email


def get_user_password() -> str:
    while True:
        try:
            user_password = input("Password: ").rstrip().lstrip()
        except KeyboardInterrupt:
            print("Please type in your password!")
            file_logger.info("User tried to paste information!")
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
            elif y_n_value == "y" or y_n_value == "n":
                print("Please select Y letter or n letter!")
                file_logger.info(
                    f"User doesn't provided correct values! Value = {y_n_value}"
                )
                break
        except KeyboardInterrupt:
            print("Please type in your email!")
            file_logger.info("User tried to paste information!")
        except Exception as e:
            print("We have encountered unexpected error!", str(e), "Try again!")
            file_logger.info("User written wrong input!")
            continue
        else:
            break
    return y_n_value


if __name__ == "__main__":
    print(get_y_n_value())
