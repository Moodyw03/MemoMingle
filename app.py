import os
from dotenv import load_dotenv
from flask import Flask, render_template, session
from datetime import timedelta
from flask_cors import CORS

from markupsafe import escape, Markup
from jinja2 import pass_eval_context

from controllers.auth_controller import auth
from controllers.note_controller import note
from controllers.parent_controller import parent
from config.supabase import supabase

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
CORS(app)  # Initialize CORS

# Session configuration for auto-logout
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)  # Default timeout: 30 minutes

# Security headers middleware
@app.after_request
def add_security_headers(response):
    # Content Security Policy
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' unpkg.com; style-src 'self' fonts.googleapis.com; font-src 'self' fonts.googleapis.com fonts.gstatic.com; img-src 'self' i.ibb.co unpkg.com data:; connect-src 'self'"
    # Prevent MIME type sniffing
    response.headers['X-Content-Type-Options'] = 'nosniff'
    # XSS Protection
    response.headers['X-XSS-Protection'] = '1; mode=block'
    # Prevent clickjacking
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    # Strict Transport Security
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    # Referrer Policy
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response


@pass_eval_context
def nl2br(eval_ctx, value):
    result = escape(value).replace("\n", Markup("<br>\n"))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result


app.jinja_env.filters["nl2br"] = nl2br


app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(note, url_prefix="/notes")
app.register_blueprint(parent, url_prefix="/parent")


@app.route("/")
def index():
    return render_template("index.html")

# This is needed for Vercel deployment
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
