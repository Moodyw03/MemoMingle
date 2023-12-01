# Note Taking App

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
