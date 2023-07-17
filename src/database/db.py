from pymongo import MongoClient
from ..config import DATABASE_URL, DATABASE_NAME, USERS, CODES
from .schemas import User, Code

class DB:
    def __init__(self):
        self.__client = MongoClient(DATABASE_URL)
        self.__db = self.__client.get_database(DATABASE_NAME)
        self._users = self.__db.get_collection(USERS)
        self._codes = self.__db.get_collection(CODES)

    def get_all_info(self):
        return [list(self._users.find()), list(self._codes.find())]
    
    def find_user(self, **filter):
        data = self._users.find_one(filter)
        return User(**data) if data else None
    
    def find_code(self, **filter):
        data = self._codes.find_one(filter)
        return Code(**data) if data else None

    def add_user(self, user: User):
        self._users.insert_one(user.dict())

    def add_code(self, code: Code):
        self._codes.insert_one(code.dict())

    def update_user(self, user: User):
        self._users.update_one({"user_id": user.tg_user.id}, {"$set": user})

    def update_code(self, code: Code):
        self._codes.update_one({"user_id": code.user_id}, {"$set": code})

    def update_users(self, users):
        self._users.delete_many({})
        self._users.insert_many(users)

    def update_codes(self, codes):
        self._codes.delete_many({})
        self._codes.insert_many(codes)    