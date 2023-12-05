from datetime import datetime
from bson import ObjectId

from config.db import db


class Note:
    def __init__(self, title, content, tags=None, user_id=None):
        self.title = title
        self.content = content
        self.dateCreated = datetime.now()  # Set on object creation
        self.tags = tags if tags else []
        self.user_id = user_id

    def insert(self):
        # Set 'lastModified' to the current time on insert
        result = db.notes.insert_one(
            {
                "title": self.title,
                "content": self.content,
                "dateCreated": self.dateCreated,
                "lastModified": datetime.now(),
                "tags": self.tags,
                "user_id": self.user_id,
            }
        )
        return result.inserted_id

    @staticmethod
    def find_all(user_id=None):
        return db.notes.find({"user_id": user_id}).sort("lastModified", -1)

    @staticmethod
    def find_by_id(note_id):
        return db.notes.find_one({"_id": ObjectId(note_id)})

    @staticmethod
    def update(note_id, new_data):
        new_data["lastModified"] = datetime.now()
        db.notes.update_one({"_id": ObjectId(note_id)}, {"$set": new_data})

    @staticmethod
    def delete(note_id):
        db.notes.delete_one({"_id": ObjectId(note_id)})

    @staticmethod
    def search(query, user_id=None):
        return db.notes.find(
            {
                "$and": [
                    {
                        "$or": [
                            {"title": {"$regex": query, "$options": "i"}},
                            {"content": {"$regex": query, "$options": "i"}},
                            {"tags": {"$regex": query, "$options": "i"}},
                            {"dateCreated": {"$regex": query, "$options": "i"}},
                            {"lastModified": {"$regex": query, "$options": "i"}},
                        ]
                    },
                    {"user_id": user_id},
                ]
            }
        ).sort("lastModified", -1)
