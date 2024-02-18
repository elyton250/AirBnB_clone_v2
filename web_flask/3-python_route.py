#!/usr/bin/python3
"""this module i added the c display"""


from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return "Hello HBNB!"


@app.route('/hbnb')
def hello_hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c_diplay(text):
    """this display c and text"""
    modified_text = text.replace('_', ' ')
    return f"C {modified_text}"


@app.route('/python/<text>')
def python_diplay(text):
    """this display c and text"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
