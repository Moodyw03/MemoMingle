from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId

from config.db import db


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def insert(self):
        result = db.users.insert_one({
            'username': self.username,
            'password': self.password
        })
        return result.inserted_id

    @staticmethod
    def find_by_username(username):
        return db.users.find_one({'username': username})

    @staticmethod
    def find_by_id(user_id):
        return db.users.find_one({'_id': ObjectId(user_id)})

    @staticmethod
    def verify_password(email, password):
        user = User.find_by_username(email)
        if user:
            return check_password_hash(user['password'], password)
        return False
