#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes
"""

from models.state import State
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/cities_by_states')
def city_list():
    """this function is for a city"""
    states = storage.all('State')
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
