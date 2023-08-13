from db_layer import MongoClient


class Game:
    def __init__(self, id: str, name: str, word: str) -> None:
        self.id = id
        self.name = name
        self._word = word
