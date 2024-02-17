#!/usr/bin/python3
"""this routes to the other path"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """thsi displays hello"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hello_hbnb():
    """this rerouts to hbnb"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
