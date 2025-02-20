#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes
"""

from models.state import State
from models import storage
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def display_states():
    """dislay states description"""
    states = storage.all('State')
    return render_template('9-states.html', states=states)


@app.route("/states/<id>")
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    states = storage.all('State')
    state = states.get(id)
    return render_template("9-states.html", states={id: state})


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
