from db_layer import MongoClient
from typing import Optional


class Game:
    def __init__(self, id: str, name: str, word: str) -> None:
        self.id = id
        self.name = name
        self._word = word
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

    def get_word(self) -> Optional[str]:
        return self._word

    def take_live_away(self) -> None:
        self.lives_left -= 1

    def get_lives_count(self) -> int:
        return self.lives_left
