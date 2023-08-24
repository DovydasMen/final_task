# pylint: skip-file
from abc import ABC, abstractmethod
from random import randint
from typing import Any, Dict, List, Optional, Union

from pymongo import MongoClient
from pymongo.cursor import Cursor
from pymongo.errors import (
    CollectionInvalid,
    ConnectionFailure,
    OperationFailure,
    PyMongoError,
    WriteError,
)
from random_word import RandomWords

from loggers.log_to_console import console_logger
from loggers.log_to_file import file_logger


class DbConnection(ABC):
    @abstractmethod
    def create_collection() -> bool:
        pass

    @abstractmethod
    def create_user() -> Optional[str]:
        pass

    @abstractmethod
    def check_login() -> Optional[bool]:
        pass

    @abstractmethod
    def is_email_used() -> Optional[bool]:
        pass

    @abstractmethod
    def create_words_for_game() -> None:
        pass

    @abstractmethod
    def drop_collection() -> None:
        pass

    @abstractmethod
    def get_user() -> Optional[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_all_games() -> Cursor:
        pass


class Base(DbConnection):
    def __init__(self, host: str, port: str, database_name: str) -> None:
        self.host = host
        self.port = port
        self.database_name = database_name

    def create_collection(self, collection_name: str) -> bool:
        """Method is used to create collection to Db"""
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
        """Method is use to generate random entries(words) to db ussing random_word library"""
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
            return
        except ConnectionFailure as e:
            file_logger.info(f"Connection to db was lost! {str(e).capitalize()}")
            return
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return

    def drop_collection(self, collection_name: str) -> None:
        """Method is used to drop collection from Db."""
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            db.drop_collection(f"{collection_name}")
            file_logger.info(f"Collection {collection_name} was droped/deleted!")
        except ConnectionFailure as e:
            file_logger.info(f"Connection to db was lost! {str(e).capitalize()}")
            return
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return

    def create_user(
        self, collection_name: str, name: str, email: str, password: str
    ) -> Optional[str]:
        """Method is used to create user entry to db. Need to get collection name as string, name as string, email as string, password as string"""
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
            return
        except ConnectionFailure as e:
            file_logger.info(f"Connection to db was lost! {str(e).capitalize()}")
            return
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return

    def is_email_used(self, collection_name: str, email: str) -> Optional[bool]:
        """Method checks if email is unused. Query for user by email."""
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            collection = db[collection_name]
            file_logger.info(f"There was query to our db for {email}!")
            query = {"email": {"$eq": email}}
            if collection.find_one(query) != None:
                return True
            return False
        except ConnectionFailure as e:
            file_logger.info(f"Connection to db was lost! {str(e).capitalize()}")
            return
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return

    def check_login(
        self, collection_name: str, email: str, password: str
    ) -> Optional[Union[str, bool]]:
        """Method checks if provided credentials is same as in db"""
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            collection = db[collection_name]
            file_logger.info(f"There was query to our db for {email}!")
            query = {"email": {"$eq": email}}
            result = collection.find_one(query)
            if result == None:
                file_logger.info("We don't have such account in our system!")
                return ""
            else:
                if result["email"] == email and result["password"] == password:
                    return True
                else:
                    return False
        except ConnectionFailure as e:
            file_logger.info(f"Connection to db was lost! {str(e).capitalize()}")
            return
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return

    def get_user(self, collection_name: str, email: str) -> Optional[Dict[str, Any]]:
        """Method returns user."""
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
            return
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return

    def get_random_word(self, collection_name: str) -> Optional[str]:
        """Method returs random word as a string."""
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
            return
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return

    def add_game(
        self,
        collection_name: str,
        user_id: str,
        word: str,
        lifes_left: str,
        incorrect_guessed_letters: List[str],
        letters_left: List[str],
        game_status: bool,
    ) -> Optional[str]:
        """Method add game to db with it's options."""
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            collection = db[collection_name]
            game_info = {
                "user_id": f"{user_id}",
                "guessing_word": f"{word}",
                "lifes_left": f"{lifes_left}",
                "incorrect_guessed_letters": f"{incorrect_guessed_letters}",
                "letter_left": f"{letters_left}",
                "game_status": f"{game_status}",
            }
            result = collection.insert_one(game_info)
            file_logger.info(f"Game with id - {result.inserted_id} was created.")
            return str(result.inserted_id)
        except WriteError as e:
            file_logger.info(
                f"We faced error while creating Game! {str(e).capitalize()}"
            )
            return
        except ConnectionFailure as e:
            file_logger.info(f"Connection to db was lost! {str(e).capitalize()}")
            return
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return

    def get_all_games(self, collection_name: str, user_id: str) -> Optional[Cursor]:
        """Method returns all games as a MongoDb object Cursor."""
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            collection = db[collection_name]
            file_logger.info(
                f"There was query to our db for games according to user_id: {user_id}!"
            )
            pipeline = [{"$match": {"user_id": f"{user_id}"}}]
            result = collection.aggregate(pipeline)
            return result
        except ConnectionFailure as e:
            file_logger.info(f"Connection to db was lost! {str(e).capitalize()}")
            return
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return


class MongoDB(Base):
    def __init__(self, host: str, port: str, database_name: str) -> None:
        super().__init__(host, port, database_name)
        self.host = host
        self.port = port
        self.database_name = database_name

    def set_up_schema_validator(
        self, collection_name: str, validator_rule: Dict[str, Any]
    ) -> Optional[bool]:
        """Method is used to set up validator schemas."""
        try:
            client: MongoClient = MongoClient(f"mongodb://{self.host}:{self.port}")
            db = client[self.database_name]
            collection = db[collection_name]
            db.command("collMod", collection.name, **validator_rule)
            file_logger.info("Validator rule was set")
            return True
        except OperationFailure as e:
            file_logger.info(f" We have encountered operational issue {e}")
            return
        except Exception as e:
            file_logger.info(f"We have encountered unxepected error {e}")
            return


if __name__ == "__main__":
    pass
