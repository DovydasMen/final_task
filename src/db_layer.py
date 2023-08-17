from pymongo import MongoClient
from pymongo.errors import (
    CollectionInvalid,
    PyMongoError,
    ConnectionFailure,
    WriteError,
)
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from loggers.log_to_console import console_logger
from loggers.log_to_file import file_logger
from random_word import RandomWords
from random import randint


# class DbConnection(ABC):
#     @abstractmethod
#     def create_collection() -> bool:
#         pass

#     @abstractmethod
#     def create_user() -> int:
#         pass

#     @abstractmethod
#     def check_login() -> bool:
#         pass
#
#     @abstractmethod
#     def is_email_unused()-> bool:
#         pass

#     @abstractmethod
#     def create_words_for_game() -> None:
#         pass

#     @abstractmethod
#     def drop_collection() -> str:
#         pass

#     @abstractmethod
#     def get_user() -> str:
#         pass

#     @abstractmethod
#     def get_user_all_games() -> List[Dict[str, Any]]:
#         pass

#     @abstractmethod
#     def get_user_unfinished_game() -> Dict[str, Any]:
#         pass


class Base:
    def __init__(self, host: str, port: str, database_name: str) -> None:
        self.host = host
        self.port = port
        self.database_name = database_name

    def create_collection(self, collection_name: str) -> bool:
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            db.create_collection(collection_name)
            file_logger.info(f"Collection {collection_name} was created!")
            client.close()
            return True
        except CollectionInvalid as e:
            file_logger.info(
                f"Collection is not created as expected! {str(e).capitalize()}!"
            )
            return False
        except PyMongoError as e:
            file_logger.info(f"We have faced unexpected error: {str(e).capitalize()}")
            return False

    def create_words_for_game(self, collection_name: str) -> None:
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            collection = db[collection_name]
            random_word = RandomWords()
            for entry in range(50):
                collection.insert_one(
                    {f"word": random_word.get_random_word(), "entry": str(entry)}
                )
        except WriteError as e:
            file_logger.info(
                f"We faced error while creating user! {str(e).capitalize()}"
            )
            return ""
        except ConnectionFailure as e:
            file_logger.info(f"Connection to db was lost! {str(e).capitalize()}")
            return ""
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return ""

    def drop_collection(self, collection_name: str) -> str:
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            db.drop_collection(f"{collection_name}")
            file_logger.info(f"Collection {collection_name} was droped/deleted!")
        except ConnectionFailure as e:
            file_logger.info(f"Connection to db was lost! {str(e).capitalize()}")
            return None
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return None

    def crate_user(
        self, collection_name: str, name: str, email: str, password: str
    ) -> str:
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            collection = db[collection_name]
            user_info = {
                "name": f"{name}",
                "email": f"{email}",
                "password": f"{password}",
            }
            result = collection.insert_one(user_info)
            file_logger.info(f"User with id - {result.inserted_id} was created.")
            return str(result.inserted_id)
        except WriteError as e:
            file_logger.info(
                f"We faced error while creating user! {str(e).capitalize()}"
            )
            return ""
        except ConnectionFailure as e:
            file_logger.info(f"Connection to db was lost! {str(e).capitalize()}")
            return ""
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return ""

    def is_email_unused(self, collection_name: str, email: str) -> Optional[bool]:
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            collection = db[collection_name]
            file_logger.info(f"There was query to our db for {email}!")
            query = {"email": {"$eq": email}}
            if collection.find_one(query) != None:
                return False
            return True
        except ConnectionFailure as e:
            file_logger.info(f"Connection to db was lost! {str(e).capitalize()}")
            return None
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return None

    def check_login(
        self, collection_name: str, email: str, password: str
    ) -> Optional[bool]:
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            collection = db[collection_name]
            file_logger.info(f"There was query to our db for {email}!")
            query = {"email": {"$eq": email}}
            result = collection.find_one(query)
            if result["email"] == email and result["password"] == password:
                return True
            return False
        except ConnectionFailure as e:
            file_logger.info(f"Connection to db was lost! {str(e).capitalize()}")
            return None
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return None

    def get_user(self, collection_name: str, email: str) -> Optional[Dict[str, Any]]:
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            collection = db[collection_name]
            file_logger.info(f"There was query to our db for {email}!")
            query = {"email": {"$eq": email}}
            result = collection.find_one(query)
            return result
        except ConnectionFailure as e:
            file_logger.info(f"Connection to db was lost! {str(e).capitalize()}")
            return None
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return None

    def get_random_word(self, collection_name: str) -> Optional[str]:
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            collection = db[collection_name]
            value = randint(0, 49)
            query = {"entry": {f"$eq": f"{value}"}}
            result = collection.find_one(query)
            return str(result["word"]).upper()
        except ConnectionFailure as e:
            file_logger.info(f"Connection to db was lost! {str(e).capitalize()}")
            return None
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return None

    def add_game(
        self,
        collection_name: str,
        user_id: str,
        game_number: str,
        word: str,
        lives_left: str,
        incorrect_guessed_letters: List[str],
        letters_left: List[str],
        guessed_letters: List[str],
        game_status: bool,
    ) -> Optional[str]:
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            collection = db[collection_name]
            game_info = {
                "user_id": f"{user_id}",
                "game_number": f"{game_number}",
                "guessing_word": f"{word}",
                "lives_left": f"{lives_left}",
                "incorrect_guessed_letters": f"{incorrect_guessed_letters}",
                "letter_left": f"{letters_left}",
                "guessed_letters": f"{guessed_letters}",
                "game_status": f"{game_status}",
            }
            result = collection.insert_one(game_info)
            file_logger.info(f"Game with id - {result.inserted_id} was created.")
            return str(result.inserted_id)
        except WriteError as e:
            file_logger.info(
                f"We faced error while creating Game! {str(e).capitalize()}"
            )
            return None
        except ConnectionFailure as e:
            file_logger.info(f"Connection to db was lost! {str(e).capitalize()}")
            return None
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return None

    def get_game_number(self, collection_name: str) -> int:
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            collection = db[collection_name]  

    def get_all_finished_games(self, collection_name: str, user_id: str) -> List[Dict]:
        pass

    def get_unfinished_game(self, collection_name: str, user_id: str) -> Dict:
        pass

    def delete_game(self, colllection_name: str, game_number) -> str:
        pass


class MongoDB(Base):
    def __init__(self, host: str, port: str, database_name: str) -> None:
        super().__init__(host, port, database_name)
        self.host = host
        self.port = port
        self.database_name = database_name


if __name__ == "__main__":
    db = MongoDB("0.0.0.0", "27017", "final_task")
    db.create_collection("words")
    db.create_words_for_game("words")
