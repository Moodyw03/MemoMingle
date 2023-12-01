import os
import datetime

from dotenv import load_dotenv
from flask import Flask, request, jsonify
from bson import ObjectId
from controllers.note_controller import (
    create_note,
    get_notes,
    get_note,
    update_note,
    delete_note,
)


from config.db import db

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


# CRUD Routes for Notes
app.route("/api/notes", methods=["POST"])(create_note)
app.route("/api/notes", methods=["GET"])(get_notes)
app.route("/api/notes/<string:note_id>", methods=["GET"])(get_note)
app.route("/api/notes/<string:note_id>", methods=["PUT"])(update_note)
app.route("/api/notes/<string:note_id>", methods=["DELETE"])(delete_note)


@app.route("/")
# Get all notes from the database
def index():
    return jsonify({"message": "Welcome to the Notes API"})
