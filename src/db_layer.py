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
            # think of quering information from collection
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
            # not hashed !
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

    def is_email_unused(self, collection_name: str, email: str) -> bool:
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
            return False
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return False

    def check_login(self, collection_name: str, email: str, password: str) -> bool:
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
            return False
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return False

    def get_user(self, collection_name: str, email: str) -> Dict[str, Any]:
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
            return {}
        except PyMongoError as e:
            file_logger.info(f"We occured unxepected error. {str(e).capitalize()}")
            return {}


class MongoDB(Base):
    def __init__(self, host: str, port: str, database_name: str) -> None:
        super().__init__(host, port, database_name)
        self.host = host
        self.port = port
        self.database_name = database_name


if __name__ == "__main__":
    db = MongoDB("0.0.0.0", "27017", "final_task")
    # db.create_collection("words")
    # db.create_words_for_game("words")
    # db.crate_user("users", "d", "d@d.lt", "123")
    # print(db.check_login("users", "d@d.lt", "12"))
    print(db.get_user("users", "d@d.lt"))
    print(type(db.get_user("users", "d@d.lt")))
