#!/usr/bin/python3
"""this modules returns a number"""

from flask import Flask, render_template


def create_app():
    """this creates the app"""
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.route('/')
    def hello_world():
        """ Returns some text. """
        return 'Hello HBNB!'

    @app.route('/hbnb')
    def hello():
        """ Return other text. """
        return 'HBNB'

    @app.route('/c/<text>')
    def c_text(text):
        """ replace text with variable. """
        text = text.replace('_', ' ')
        return 'C {}'.format(text)
    return app


if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000)
