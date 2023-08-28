# pylint: skip-file
from typing import List, Optional

from db_layer import MongoClient
from loggers.log_to_console import console_logger


class Game:
    """To initialize class, need to provide user id and word."""

    def __init__(self, user_id: str, word: str) -> None:
        self.user_id = user_id
        self._word = word
        self.word_lenght_in_list = []
        self.lives_left = 10
        self.guesed_letters = []
        self.letters_left = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]
        self.guessing_word = []

    def get_word(self) -> Optional[str]:
        """Method returns private attribute"""
        return self._word

    def fill_guessing_word_with_special_char(self) -> None:
        """Method makes private attribute into the list filled with special char."""
        for number in range(len(self._word)):
            self.guessing_word.insert(number, "_")

    def take_life_away(self) -> None:
        """Method is used to take life away if letter wasn't correct"""
        self.lives_left -= 1

    def get_lifes_count(self) -> int:
        """Method returs lifes count"""
        return int(self.lives_left)

    def accept_letter_for_game(self, letter: str) -> None:
        """Method accepts a letter in capital, then goes throught the algorithm to set all attributes."""
        counter = 0
        if letter in self._word:
            try:
                self.letters_left.remove(letter.upper())
            except ValueError:
                console_logger.info(
                    "You have provided same letter that was used before. Please select one that was not used!"
                )
            except Exception as e:
                console_logger.info(f"we have encountered unexepected error! {e}")
            for letter_in_word in self._word:
                if letter == letter_in_word:
                    self.guessing_word.pop(counter)
                    self.guessing_word.insert(counter, letter)
                    counter += 1
                else:
                    counter += 1
        else:
            try:
                self.letters_left.remove(letter.upper())
                self.guesed_letters.append(letter)
            except ValueError:
                console_logger.info(
                    "You have provided same letter that was used before. Please select one that was not used!"
                )
            except Exception as e:
                console_logger.info(f"we have encountered unexepected error! {e}")
            else:
                self.take_life_away()

    def get_left_letters(self) -> List[str]:
        """Method returs list with all letters which is still unused."""
        return self.letters_left

    def get_incorrect_guesed_letters(self) -> List[str]:
        """Method returs a list of incorrect guessed letters"""
        return self.guesed_letters

    def get_game_status(self) -> bool:
        """Method returs bool value according to game state."""
        if self.lives_left > 0 and "_" not in self.guessing_word:
            return True
        else:
            return False

    def get_guessing_word(self) -> List[str]:
        """Method returs list of letters of guessing word."""
        return self.guessing_word


if __name__ == "__main__":
    pass
