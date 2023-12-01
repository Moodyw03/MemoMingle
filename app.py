import os
from dotenv import load_dotenv
from flask import Flask, render_template

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
    # return index.html from the templates folder
    return render_template("index.html")
