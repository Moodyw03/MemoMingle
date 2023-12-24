import os
from dotenv import load_dotenv
from flask import Flask, render_template

from markupsafe import escape, Markup
from jinja2 import pass_eval_context

from controllers.auth_controller import auth
from controllers.note_controller import note

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@pass_eval_context
def nl2br(eval_ctx, value):
    result = escape(value).replace("\n", Markup("<br>\n"))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result


app.jinja_env.filters["nl2br"] = nl2br


app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(note, url_prefix="/notes")


@app.route("/")
def index():
    return render_template("index.html")
