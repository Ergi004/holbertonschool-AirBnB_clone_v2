#!/usr/bin/python3
"""
Module to initiate a flask
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Index route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    hbnb route
    """
    return "HBNB"

if __name__ == '__main__':
    app.run(debug=False)
