from datetime import timedelta
from flask import (
    Flask, session, render_template, request, flash, redirect, url_for
)
import config
import logging

from views import index, load, generate
from src.models.user import User
from src.external.s3 import S3Client


application = Flask(__name__)

application.logger.handlers = []
application.logger.addHandler(logging.StreamHandler())

application.secret_key = config.AUTH_KEY
session_timeout = config.SESSION_TIMEOUT
application.permanent_session_lifetime = timedelta(minutes=session_timeout)
S3Client.initialize_bucket(config.BUCKET)
User.initialize_users()

modules = [index, load, generate]
for module in modules:
    application.register_blueprint(module.routes)


def authorize(username, password):
    if not User.is_valid_login(username, password):
        return False
    session.permanent = True
    session['username'] = username
    return True


def is_logged_in():
    if session.get('username'):
        return True
    return False


@application.before_request
def before_request():
    if not is_logged_in():
        if not authorize(
            request.form.get('username'),
            request.form.get('password')
        ):
            flash('Invalid login information', 'error')
            return render_template('login.html')


@application.route('/login', methods=['POST'])
def login():
    if authorize(
        request.form.get('username'),
        request.form.get('password')
    ):
        return redirect(url_for('index.index'))
    else:
        flash('Invalid login information', 'error')
        return render_template('login.html')


@application.route('/logout', methods=['GET'])
def logout():
    session.pop('username')
    return render_template('login.html')


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
