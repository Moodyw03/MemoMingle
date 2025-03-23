from flask import session, redirect, url_for
from functools import wraps
from models.user import User


def login_required(f):
    """
    Decorator to verify if user is logged in
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("auth.sign_in"))
        return f(*args, **kwargs)
    return decorated_function

def parent_required(f):
    """
    Decorator to verify if user is a parent account
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("auth.sign_in"))
            
        user_id = session["user_id"]
        user = User.find_by_id(user_id)
        
        # Check if user exists and is a parent
        if not user or not user.get("is_parent", False):
            # Redirect to notes page if the user is not a parent
            return redirect(url_for("note.get_notes"))
            
        return f(*args, **kwargs)
    return decorated_function
