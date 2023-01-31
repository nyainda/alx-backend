#!/usr/bin/env python3

""" Entry point for the application. """

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Locale selector. """
    if request.args.get('locale') in Config.LANGUAGES:
        return request.args.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])


class Config():
    """ The `Config` class is a class that contains a list of languages"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    The function `index()` returns the rendered template `index.html`
    :return: The index.html file is being returned.
    """

    return render_template('4-index.html')


if __name__ == "__main__":
    """ This is a common Python idiom to check if the file
    is being run as a script or imported as a module."""
    app.run(host='0.0.0.0', port=5000, debug=True)
