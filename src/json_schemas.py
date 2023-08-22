user_validation_rules = {
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name", "email", "password"],
            "properties": {
                "name": {"bsonType": "string", "description": "Name must be a string."},
                "email": {
                    "bsonType": "string",
                    "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
                    "description": "Email must be a valid email address.",
                },
                "password": {
                    "bsonType": "string",
                    "description": "Password must be a string.",
                },
            },
        }
    }
}

word_validation_rules = {
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["word"],
            "properties": {
                "word": {"bsonType": "string", "description": "Word must be a string."}
            },
        }
    }
}

games_validation_rules = {
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": [
                "user_id",
                "guessing_word",
                "lifes_left",
                "incorrect_guessed_letters",
                "letter_left",
                "game_status",
            ],
            "properties": {
                "user_id": {
                    "bsonType": "string",
                    "description": "User id must be a string.",
                },
                "guessing_word": {
                    "bsonType": "string",
                    "description": "Word must be a string.",
                },
                "lifes_left": {
                    "bsonType": "string",
                    "description": "Word must be a string.",
                },
                "incorrect_guessed_letters": {
                    "bsonType": "string",
                    "description": "There comes string of letters in list.",
                },
                "letter_left": {
                    "bsonType": "string",
                    "description": "There comes string of letters in list.",
                },
                "game_status": {
                    "bsonType": "string",
                    "description": "Game status must be a string.",
                },
            },
        }
    }
}
