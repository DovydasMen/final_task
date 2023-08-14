from db_layer import MongoClient
from typing import Optional, List
from loggers.log_to_console import console_logger


class Game:
    def __init__(self, id: str, name: str, word: str) -> None:
        self.id = id
        self.name = name
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
        return self._word

    def set_list_of_random_word(self) -> None:
        for number in range(len(self._word)):
            self.word_lenght_in_list.insert(number, "_")

    def set_list_lenght_for_guessing(self) -> None:
        for number in range(len(self._word)):
            self.guessing_word.insert(number, "_")

    def take_live_away(self) -> None:
        self.lives_left -= 1

    def get_lives_count(self) -> int:
        return self.lives_left

    def accept_letter_for_game(self, letter: str) -> None:
        counter = 0
        if letter in self._word:
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
                self.take_live_away()

    def get_left_letters(self) -> List[str]:
        return self.letters_left

    def get_game_status(self) -> bool:
        if self.lives_left > 0 and "_" not in self.guessing_word:
            return True
        else:
            return False


if __name__ == "__main__":
    game = Game("123", "Dovydas", "aaaabbbbcccc")
    game.set_list_of_random_word()
    game.set_list_lenght_for_guessing()
    game.accept_letter_for_game("d")
    print(game.get_lives_count())
    game.accept_letter_for_game("d")
    print(game.get_lives_count())
    game.accept_letter_for_game("d")
    game.accept_letter_for_game("e")
    game.accept_letter_for_game("i")
    game.accept_letter_for_game("z")
    game.accept_letter_for_game("x")
    game.accept_letter_for_game("j")
    game.accept_letter_for_game("k")
    game.accept_letter_for_game("o")
    game.accept_letter_for_game("q")

    game.accept_letter_for_game("b")
    game.accept_letter_for_game("c")
    print(game.guessing_word)
    print(game.get_lives_count())
    print(game.get_game_status())
