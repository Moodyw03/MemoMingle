import os
from dotenv import load_dotenv
from flask import Flask, render_template

from controllers.auth_controller import auth
from controllers.note_controller import note

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(note, url_prefix="/notes")


@app.route("/")
def index():
    return render_template("index.html")
