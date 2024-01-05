
<h1 align="center">MemoMingle</h1>

[View the live project here.](https://memomingle.vercel.app/)

Welcome to MemoMingle, an intuitive and robust note-taking application designed to streamline the way individuals capture and organize their thoughts. This application serves as a personal and professional aid, allowing users to create, edit, and manage notes with ease. The sleek user interface, tailored for an optimal user experience, incorporates contemporary design principles to ensure that navigation and note management are both seamless and efficient.

Whether you're jotting down quick reminders or compiling detailed research notes, MemoMingle is your go-to solution for storing information efficiently. This document will guide you through every aspect of using MemoMingle, from initial setup to advanced features.

This submission represents Milestone Project 3 for the Code Institute's Diploma in Web Application Development program. My website comprises of a note-taking app and utilizes the HTML, CSS,  Javascript, and Python technologies I have acquired throughout the course.




<div align="center">
<a href="https://ibb.co/T1yzLCd"><img src="https://i.ibb.co/hc0pfqw/memomingle-copy.jpg" alt="memomingle-copy" border="0"></a>
</div>

## Repository

[Find the project repository here:](https://github.com/Moodyw03/moodloop-final)

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


## Repository

[Find the project repository here:](https://github.com/Moodyw03/moodloop-final)

























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
