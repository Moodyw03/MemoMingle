from datetime import datetime
from config.db import db
from bson import ObjectId


class Note:
    def __init__(self, title, content, tags=None):
        self.title = title
        self.content = content
        self.dateCreated = datetime.now()
        self.lastModified = self.dateCreated
        self.tags = tags if tags else []

    def insert(self):
        result = db.notes.insert_one({
            'title': self.title,
            'content': self.content,
            'dateCreated': self.dateCreated,
            'lastModified': self.lastModified,
            'tags': self.tags
        })
        return result.inserted_id

    @staticmethod
    def find_all():
        return db.notes.find()

    @staticmethod
    def find_by_id(note_id):
        return db.notes.find_one({'_id': ObjectId(note_id)})

    @staticmethod
    def update(note_id, new_data):
        db.notes.update_one({'_id': ObjectId(note_id)}, {'$set': new_data})

    @staticmethod
    def delete(note_id):
        db.notes.delete_one({'_id': ObjectId(note_id)})
