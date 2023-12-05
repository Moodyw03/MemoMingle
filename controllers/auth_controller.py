from flask import Blueprint, request, session, redirect, url_for, render_template
from models.user import User

auth = Blueprint('auth', __name__)


@auth.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    # if the user is already logged in, redirect to the notes page
    if 'user_id' in session:
        return redirect(url_for('note.get_notes'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.verify_password(username, password):
            user = User.find_by_username(username)
            session['user_id'] = str(user['_id'])
            return redirect(url_for('note.get_notes'))
        return render_template('sign-in.html', error='Invalid credentials')
    return render_template('sign-in.html')


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # if the user is already logged in, redirect to the notes page
    if 'user_id' in session:
        return redirect(url_for('note.get_notes'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.find_by_username(username):
            return render_template('auth/sign-up.html', error='Email already exists')
        user = User(username, password)
        user.insert()
        return redirect(url_for('auth.sign_in'))
    return render_template('sign-up.html')


@auth.route('/sign-out')
def sign_out():
    session.pop('user_id', None)
    return redirect(url_for('auth.sign_in'))
