from flask import Blueprint, request, session, redirect, url_for, render_template, flash
from models.user import User
from decorators import login_required
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
from flask import current_app as app

auth = Blueprint("auth", __name__)


@auth.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    # if the user is already logged in, redirect to the appropriate page
    if "user_id" in session:
        if session.get("is_parent"):
            return redirect(url_for("parent.dashboard"))
        return redirect(url_for("note.get_notes"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        is_shared_device = request.form.get("shared_device") == "on"
        
        error = None

        if not username or not password:
            error = "Username and password are required."
        else:
            user = User.find_by_username(username)
            if user is None:
                error = "Incorrect username or password."
            elif not check_password_hash(user["password"], password):
                error = "Incorrect username or password."

        if error is None:
            session.clear()
            session.permanent = True
            
            # Set different timeouts based on device type
            if is_shared_device:
                # 10 minutes for shared devices
                app.permanent_session_lifetime = timedelta(minutes=10)
            else:
                # 2 hours for personal devices
                app.permanent_session_lifetime = timedelta(hours=2)
            
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            session["is_parent"] = user.get("is_parent", False)
            session["last_activity"] = datetime.now().timestamp()
            
            # Update user login streak
            User.update_streak(user["id"])
            
            # Redirect to appropriate page based on account type
            if session["is_parent"]:
                return redirect(url_for("parent.dashboard"))
            else:
                return redirect(url_for("note.get_notes"))

        flash(error)

    return render_template("sign-in.html")


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    # if the user is already logged in, redirect to the notes page
    if "user_id" in session:
        if session.get("is_parent"):
            return redirect(url_for("parent.dashboard"))
        return redirect(url_for("note.get_notes"))

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        is_parent = request.form.get("is_parent") == "on"

        # Check if username or password is less than 4 characters
        if len(username) < 4 or len(password) < 4:
            return render_template(
                "sign-up.html",
                error="Username and password must be at least 4 characters long",
            )

        if User.find_by_username(username):
            return render_template("sign-up.html", error="Username already exists")

        user = User(username, password, is_parent=is_parent)
        user.insert()
        return render_template("sign-in.html", success="Account created successfully")

    return render_template("sign-up.html")


@auth.route("/sign-out")
def sign_out():
    session.pop("user_id", None)
    return redirect(url_for("auth.sign_in"))


@auth.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    user_id = session["user_id"]
    user = User.find_by_id(user_id)
    
    # Get user achievements
    achievements = User.get_achievements(user_id)
    
    if request.method == "POST":
        current_password = request.form["current_password"]
        new_password = request.form["new_password"]
        confirm_new_password = request.form["confirm_new_password"]
        
        # Validate current password
        if not check_password_hash(user["password"], current_password):
            return render_template("profile.html", user=user, achievements=achievements, error="Current password is incorrect")
        
        # Check if new password matches confirmation
        if new_password != confirm_new_password:
            return render_template("profile.html", user=user, achievements=achievements, error="New passwords do not match")
        
        # Check if new password meets requirements
        if len(new_password) < 4:
            return render_template("profile.html", user=user, achievements=achievements, error="Password must be at least 4 characters long")
        
        # Update the password
        User.update_password(user_id, new_password)
        
        return render_template("profile.html", user=user, achievements=achievements, success="Password updated successfully")
    
    return render_template("profile.html", user=user, achievements=achievements)


@auth.route("/delete-account", methods=["GET", "POST"])
@login_required
def delete_account():
    """Delete the user's own account"""
    user_id = session["user_id"]
    user = User.find_by_id(user_id)
    
    if request.method == "POST":
        # Check if user is confirming deletion with their password
        password = request.form.get("password")
        
        if not password or not check_password_hash(user["password"], password):
            flash("Incorrect password. Account not deleted.", "error")
            return render_template("delete-account.html")
        
        # If this is a parent account, check for child accounts
        if user.get("is_parent", False):
            children = User.get_children(user_id)
            if children:
                flash("You cannot delete your account while you have child accounts. Please delete child accounts first.", "error")
                return render_template("delete-account.html")
        
        # Delete the account
        success, message = User.delete_user(user_id)
        
        if success:
            # Clear the session
            session.clear()
            flash("Your account has been successfully deleted.", "success")
            return redirect(url_for("auth.sign_in"))
        else:
            flash(message, "error")
            return render_template("delete-account.html")
    
    return render_template("delete-account.html")
