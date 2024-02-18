#!/usr/bin/python3
"""this modules returns even or odds"""
from flask import Flask, render_template


def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.route('/')
    def hello_world():
        """Return some text."""
        return 'Hello HBNB!'

    @app.route('/hbnb')
    def hello():
        """Return other text."""
        return 'HBNB'

    @app.route('/c/<text>')
    def c_text(text):
        """Replace text with variable."""
        text = text.replace('_', ' ')
        return 'C {}'.format(text)

    @app.route('/python/')
    @app.route('/python/<text>')
    def python_text(text='is cool'):
        """Replace more text with another variable."""
        text = text.replace('_', ' ')
        return 'Python {}'.format(text)

    @app.route('/number/<int:n>')
    def number_text(n):
        """Replace with int only if given int."""
        n = str(n)
        return '{} is a number'.format(n)

    @app.route('/number_template/<int:n>')
    def html_num(n):
        """Display HTML if n is int."""
        n = str(n)
        return render_template('5-number.html', n=n)

    @app.route('/number_odd_or_even/<int:n>')
    def html_display_even_odd(n):
        """Display according to odd and even."""
        try:
            if n % 2 == 0:
                return render_template(
                    '6-number_odd_or_even.html', n=n, result='even')
            else:
                return render_template(
                    '6-number_odd_or_even.html', n=n, result='odd')
        except ValueError:
            return f"{n} is not a valid number"

    return app


if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000)
