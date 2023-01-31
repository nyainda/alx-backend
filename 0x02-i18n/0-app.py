#!/usr/bin/env python3

""" Entry point for the application. """

from os import getenv
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Locale selector. """
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())


class Config(object):
    """ The `Config` class is a class that contains a list of languages"""
    LANGUAGES = ['en', 'fr']


@app.route('/')
def index():
    """
    The function `index()` returns the rendered template `index.html`
    :return: The index.html file is being returned.
    """

    return render_template('0-index.html')


if __name__ == "__main__":
    """ This is a common Python idiom to check if the file
    is being run as a script or imported as a module."""
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
