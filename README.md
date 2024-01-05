
<h1 align="center">MemoMingle</h1>

[View the live project here.](https://memomingle.vercel.app/)

Welcome to MemoMingle, an intuitive and robust note-taking application designed to streamline the way individuals capture and organize their thoughts. This application serves as a personal and professional aid, allowing users to create, edit, and manage notes with ease. The sleek user interface, tailored for an optimal user experience, incorporates contemporary design principles to ensure that navigation and note management are both seamless and efficient.

Whether you're jotting down quick reminders or compiling detailed research notes, MemoMingle is your go-to solution for storing information efficiently. This document will guide you through every aspect of using MemoMingle, from initial setup to advanced features.

This submission represents Milestone Project 3 for the Code Institute's Diploma in Web Application Development program. My website comprises of a note-taking app and utilizes the HTML, CSS,  Javascript, and Python technologies I have acquired throughout the course.




<div align="center">
<a href="https://ibb.co/T1yzLCd"><img src="https://i.ibb.co/hc0pfqw/memomingle-copy.jpg" alt="memomingle-copy" border="0"></a>
</div>

## Repository

[Find the project repository here:](https://github.com/Moodyw03/MemoMingle)

## User Interface
MemoMingle's user interface (UI) is crafted with a focus on simplicity and ease of use, ensuring that users can navigate the app intuitively. The UI employs a warm, pastel colour palette that creates a welcoming and calming environment, aimed at enhancing user concentration and reducing visual strain during note management tasks.

Key design elements include:

Minimalistic Layout: The clean interface avoids clutter, directing user focus to the task at hand.
Intuitive Controls: Commonly used actions are prominently placed and easily accessible, promoting a fluid user experience.

Consistent Visual Elements: The use of familiar icons and consistent colour coding helps users quickly associate functions with symbols.

Responsive Design: The UI adjusts seamlessly across various devices, ensuring functionality and aesthetics are maintained on screens of all sizes.
The choice of colours and layout is informed by psychological principles that associate certain hues with memory and cognitive function, which is essential for a note-taking application. This thoughtful design approach aims to make the note-taking process as effortless and pleasant as possible for the user.

<div align="center"><a href="https://ibb.co/FY9j5t5"><img src="https://i.ibb.co/vdbK383/memomingle-colors-copy.jpg" alt="memomingle-colors-copy" border="0"></a>
</div>


## Code Overview

### App Structure

config/: Contains configuration files, like db.py for database connections.
controllers/: Holds the auth_controller.py and note_controller.py for handling authentication and note operations respectively.
models/: Includes user.py and note.py defining the data models.
static/: Stores static files like CSS, JS, and images for the front end.
templates/: Contains HTML templates for rendering views.
app.py: The main entry point of the Flask application.
.env: Stores environment variables (not to be uploaded to version control).
Database Schema:

Users Collection: Stores username and hashed passwords.
Notes Collection: Stores notes with fields for title, content, tags, creation, and last modified timestamps.

API Endpoints:
Authentication (/auth/sign-in, /auth/sign-up, /auth/sign-out): For user login, registration, and logout.
Note Management (/notes/, /notes/new, /notes/<id>/delete, /notes/<id>/edit): For listing, creating, deleting, and editing notes.


<div align="center"><a href="https://ibb.co/vvSkVMb"><img src="https://i.ibb.co/yBrqdxD/flowchart.jpg" alt="flowchart" border="0"></a></div>

## Functionality
<div align="center"><a href="https://ibb.co/DMP8830"><img src="https://i.ibb.co/X5f33mc/crud1.jpg" alt="crud1" border="0"></a></div>

### Authentication

Sign-Up: Users register by providing a username and password. The password is hashed for security and stored in the Users collection.

Sign-In: Users log in using their credentials. The system validates the input against the stored hashed password. Upon success, a session is initiated.

Sign-Out: Users sign out to end their session, clearing their session data and preventing further access to their notes without re-authentication.

### Notes Management

Creating Notes: Users can create notes by entering a title and content, along with optional tags.
Updating Notes: Existing notes can be updated. Users can modify the title, content, and tags of their notes.
Deleting Notes: Users can delete any of their notes. This action is irreversible.
Searching Notes: Users can search through their notes using keywords. The search can match note titles, content, and tags.

### Error Handling

User Feedback: Clear messages are displayed to users upon errors, like invalid login attempts or issues in note operations.
Validation Errors: Input validation errors, such as short usernames or passwords, prompt the user to correct their input.


### Security

In MemoMingle, security is a top priority, and several measures are implemented to protect user data:

Password Hashing: We use Werkzeug's security features to hash passwords before storing them in the database. This means that actual passwords are never stored, only their secure hashes.
Session Management: Flask-Session is utilized for secure session management. User sessions are encrypted and managed server-side, mitigating the risks associated with client-side sessions.
Environment Variables: Sensitive information, such as database URI and secret keys, are stored in environment variables, not in the codebase, to prevent exposure.
Secure Transport Layer: The application is configured to enforce HTTPS to ensure that data transmitted between the client and server is encrypted.
Input Validation: All user inputs are validated and sanitized to protect against SQL injection and XSS attacks.
These technologies and strategies form a robust security posture for MemoMingle, ensuring user data integrity and confidentiality.








































Create a virtual environment named 'venv' for dependency isolation.
`python3 -m venv env`

Activate the created virtual environment.
`source env/bin/activate`

Install Flask, a lightweight web application framework.
`pip install flask`

Generate a file with all installed packages and their versions.
`pip freeze > requirements.txt`

Check the installed Flask and Python versions.
`python -m flask --version`

Set the environment variable to specify the Flask application entry point.
`export FLASK_APP=app`

Set the Flask environment to development for debugging and auto-reload.
`export FLASK_ENV=development`

Enable debug mode for more detailed error logs and interactive debugging.
`export FLASK_DEBUG=1`

Run the Flask web application on a local development server.
`flask run`

Combined
`export FLASK_APP=app; export FLASK_ENV=development; export FLASK_DEBUG=1; flask run`
