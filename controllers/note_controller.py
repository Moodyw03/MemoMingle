from datetime import datetime
from flask import (
    Blueprint,
    request,
    session,
    redirect,
    url_for,
    render_template,
)


from models.note import Note
from decorators import login_required

note = Blueprint("note", __name__)


# Not needed anymore as Supabase already returns JSON-serializable data
# def serialize(doc):
#     doc["_id"] = str(doc["_id"])
#     return doc


# Notes
@note.route("/", methods=["GET"])
@login_required
def get_notes():
    user_id = session["user_id"]
    if not user_id:
        return redirect(url_for("auth.sign_in"))

    # Fetch message from query parameters
    success = request.args.get("success")
    error = request.args.get("error")
    notes = Note.find_all(user_id)

    current_date = datetime.now().date()
    return render_template(
        "notes.html",
        notes=notes,
        current_date=current_date,
        success=success,
        error=error,
    )


# New Note
@note.route("/new", methods=["POST"])
@login_required
def create_note():
    user_id = session["user_id"]
    if not user_id:
        return redirect(url_for("auth.sign_in"))

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        tags = [tag.strip() for tag in request.form["tags"].split(";")]
        note = Note(
            title=title,
            content=content,
            tags=tags,
            user_id=user_id,
        )
        note_id = note.insert()

        success = None
        error = None

        if note_id:
            success = "Note created successfully"
        else:
            error = "Failed to create note"
        return redirect(url_for("note.get_notes", success=success, error=error))


# DELETE /notes/<note_id>/delete
@note.route("/<string:note_id>/delete", methods=["POST"])
@login_required
def delete_note(note_id):
    user_id = session["user_id"]
    if not user_id:
        return redirect(url_for("auth.sign_in"))

    try:
        note = Note.find_by_id(note_id)
        if note and note["user_id"] == user_id:
            Note.delete(note_id)
            return redirect(
                url_for("note.get_notes", success="Note deleted successfully")
            )
        else:
            return redirect(url_for("note.get_notes", error="Note not found")), 404
    except Exception as e:
        return redirect(url_for("note.get_notes", error="Invalid note ID")), 400


# GET POST /notes/<note_id>/edit
@note.route("/<string:note_id>/edit", methods=["GET", "POST"])
@login_required
def edit_note(note_id):
    note = Note.find_by_id(note_id)

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        tags = [tag.strip() for tag in request.form["tags"].split(";")]

        # Create a dictionary for the new data
        new_data = {
            "title": title,
            "content": content,
            "tags": tags,
        }

        Note.update(note_id, new_data)  # Update the note in the DB
        return redirect(url_for("note.get_notes", success="Note edited successfully"))

    if note:
        # Prepare tags for display
        note["tags"] = "; ".join(note["tags"])

    return render_template("edit-note.html", note=note)


@note.route("/", methods=["POST"])
@login_required
def search_notes():
    user_id = session["user_id"]
    if not user_id:
        return redirect(url_for("auth.sign_in"))

    if request.method == "POST":
        search = request.form["search"]
        query = search.strip()

        notes = Note.search(query, user_id)
        current_date = datetime.now().date()
        return render_template(
            "notes.html", notes=notes, current_date=current_date, search=query
        )
