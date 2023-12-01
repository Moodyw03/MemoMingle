from datetime import datetime
from bson import ObjectId
from flask import jsonify, request
from models.note import Note


def serialize(doc):
    doc["_id"] = str(doc["_id"])
    return doc


def create_note():
    data = request.json
    note = Note(data['title'], data['content'], data.get('tags', []))
    note_id = note.insert()
    return jsonify({'message': 'Note created successfully', 'id': str(note_id)}), 201


def get_notes():
    notes = Note.find_all()
    return jsonify([serialize(note) for note in notes])


def get_note(note_id):
    try:
        note = Note.find_by_id(note_id)
        if note:
            return jsonify(serialize(note))

        return jsonify({'message': 'Note not found'}), 404
    except:
        return jsonify({'message': 'Invalid note ID'}), 400


def update_note(note_id):
    data = request.json
    data['lastModified'] = datetime.now()
    try:
        print(data)
        if Note.find_by_id(note_id):
            Note.update(note_id, data)
            return jsonify({'message': 'Note updated successfully'})
        return jsonify({'message': 'Note not found'}), 404
    except:
        return jsonify({'message': 'Invalid note ID'}), 400


def delete_note(note_id):
    try:
        if Note.find_by_id(note_id):
            Note.delete(note_id)
            return jsonify({'message': 'Note deleted successfully'})
        return jsonify({'message': 'Note not found'}), 404
    except:
        return jsonify({'message': 'Invalid note ID'}), 400
