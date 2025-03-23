from flask import Blueprint, request, session, redirect, url_for, render_template, flash
from models.user import User
from models.note import Note
from decorators import login_required, parent_required
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
from flask import current_app as app

parent = Blueprint("parent", __name__)

@parent.route("/dashboard")
@login_required
@parent_required
def dashboard():
    """Parent dashboard to manage child accounts"""
    parent_id = session["user_id"]
    
    # Get all children accounts
    children = User.get_children(parent_id)
    
    return render_template("parent/dashboard.html", children=children)

@parent.route("/add-child", methods=["GET", "POST"])
@login_required
@parent_required
def add_child():
    """Add a child account"""
    parent_id = session["user_id"]
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        
        # Validate input
        error = None
        
        if not username or not password:
            error = "Username and password are required."
        elif len(username) < 3:
            error = "Username must be at least 3 characters."
        elif len(password) < 4:
            error = "Password must be at least 4 characters."
        elif password != confirm_password:
            error = "Passwords do not match."
            
        if error is None:
            # Create child account
            child_id, create_error = User.create_child_account(parent_id, username, password)
            
            if child_id:
                flash("Child account created successfully!", "success")
                return redirect(url_for("parent.dashboard"))
            else:
                error = create_error or "Failed to create child account."
        
        flash(error, "error")
    
    return render_template("parent/add_child.html")

@parent.route("/child/<child_id>")
@login_required
@parent_required
def child_details(child_id):
    """View details of a child account"""
    parent_id = session["user_id"]
    
    # Verify parent relationship
    if not User.is_parent_of(parent_id, child_id):
        flash("You do not have permission to view this child's account.", "error")
        return redirect(url_for("parent.dashboard"))
    
    # Get child info
    child = User.find_by_id(child_id)
    
    # Get child's notes
    notes = Note.find_all(child_id)
    
    # Get child's achievements
    achievements = User.get_achievements(child_id)
    
    return render_template(
        "parent/child_details.html", 
        child=child, 
        notes=notes, 
        achievements=achievements
    )

@parent.route("/child/<child_id>/note/<note_id>")
@login_required
@parent_required
def view_note(child_id, note_id):
    """View a specific note from a child"""
    parent_id = session["user_id"]
    
    # Verify parent relationship
    if not User.is_parent_of(parent_id, child_id):
        flash("You do not have permission to view this child's notes.", "error")
        return redirect(url_for("parent.dashboard"))
    
    # Get the note
    note = Note.find_by_id(note_id)
    
    # Verify note exists and belongs to child
    if not note or note["user_id"] != child_id:
        flash("Note not found.", "error")
        return redirect(url_for("parent.child_details", child_id=child_id))
    
    return render_template("parent/view_note.html", note=note, child_id=child_id)

@parent.route("/child/<child_id>/time-limit", methods=["POST"])
@login_required
@parent_required
def set_time_limit(child_id):
    """Set usage time limits for a child account"""
    parent_id = session["user_id"]
    
    # Verify parent relationship
    if not User.is_parent_of(parent_id, child_id):
        flash("You do not have permission to modify this child's account.", "error")
        return redirect(url_for("parent.dashboard"))
    
    if request.method == "POST":
        daily_limit_minutes = request.form.get("daily_limit", type=int)
        
        if daily_limit_minutes is not None and daily_limit_minutes >= 0:
            # Update child's time limit in the database
            data = supabase.table('users') \
                .update({"daily_time_limit": daily_limit_minutes}) \
                .eq("id", child_id) \
                .execute()
            
            if data.data:
                flash("Time limit updated successfully!", "success")
            else:
                flash("Failed to update time limit.", "error")
        else:
            flash("Invalid time limit value.", "error")
    
    return redirect(url_for("parent.child_details", child_id=child_id))

@parent.route("/child/<child_id>/reset-password", methods=["POST"])
@login_required
@parent_required
def reset_child_password(child_id):
    """Reset a child's password"""
    parent_id = session["user_id"]
    
    # Verify parent relationship
    if not User.is_parent_of(parent_id, child_id):
        flash("You do not have permission to modify this child's account.", "error")
        return redirect(url_for("parent.dashboard"))
    
    if request.method == "POST":
        new_password = request.form.get("new_password")
        confirm_password = request.form.get("confirm_password")
        
        # Validate input
        error = None
        
        if not new_password:
            error = "New password is required."
        elif len(new_password) < 4:
            error = "Password must be at least 4 characters."
        elif new_password != confirm_password:
            error = "Passwords do not match."
            
        if error is None:
            # Update child's password
            result = User.update_password(child_id, new_password)
            
            if result:
                flash("Password reset successfully!", "success")
            else:
                error = "Failed to reset password."
        
        if error:
            flash(error, "error")
    
    return redirect(url_for("parent.child_details", child_id=child_id))

@parent.route("/flagged-content")
@login_required
@parent_required
def flagged_content():
    """View all flagged content from children's notes"""
    parent_id = session["user_id"]
    
    # Get all flagged notes from children
    flagged_notes = Note.get_flagged_notes(parent_id)
    
    return render_template("parent/flagged_content.html", notes=flagged_notes)

@parent.route("/child/<child_id>/delete", methods=["POST"])
@login_required
@parent_required
def delete_child_account(child_id):
    """Delete a child account"""
    parent_id = session["user_id"]
    
    # Verify parent relationship
    if not User.is_parent_of(parent_id, child_id):
        flash("You do not have permission to delete this child's account.", "error")
        return redirect(url_for("parent.dashboard"))
    
    # Delete the child account
    success, message = User.delete_user(child_id)
    
    if success:
        flash("Child account deleted successfully.", "success")
    else:
        flash(message, "error")
    
    return redirect(url_for("parent.dashboard")) 