#!/usr/bin/env python3
""" Entry point for the application. """

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """ Locale selector. """
    if request.args.get('locale') in Config.LANGUAGES:
        return request.args.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> dict:
    """
    If the login_as query parameter is present,
    return the user with the corresponding id, otherwise
    return None
    :return: A dictionary of the user.
    """
    login_as = request.args.get('login_as', False)
    if login_as:
        user = users[int(login_as)]
        if user:
            return user
    return None


class Config():
    """ The `Config` class is a class that contains a list of languages"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.before_request
def before_request():
    """
    > If the user is logged in, get the user object from
    the database and store it in the global
    variable `g.user`
    """

    if get_user():
        g.user = get_user()


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    The function `index()` returns the rendered template `index.html`
    :return: The index.html file is being returned.
    """

    return render_template('5-index.html')


if __name__ == "__main__":
    """ This is a common Python idiom to check if the file
    is being run as a script or imported as a module."""
    app.run(host='0.0.0.0', port=5000, debug=True)
