#!/usr/bin/python3
"""this module i added the c display"""


from flask import Flask, render_template

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
    return f"c {modified_text}"

@app.route('/python/<text>')
def python_diplay(text):
    """this display c and text"""
    if text is not None:
        modified_text = text.replace('_', ' ')
        return f"Python {modified_text}"
    else: 
        text = "is cool"
        return f"Python {text}"
@app.route('/number/<n>')
def display_number(n):
    try:
        n_int = int(n)
        return f"{n_int} is a number"
    except ValueError:
        return f"{n} is not a valid number"

@app.route('/number_template/<n>')
def html_display(n):
    """display html"""
    try:
        n_int = int(n)
        if isinstance(n_int, int):
            return render_template('5-number.html', n=n_int)
    except ValueError:
        return f"{n} is not a valid number"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
