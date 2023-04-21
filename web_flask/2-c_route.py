#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Handles the root url"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Handles the root/hbnb url"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Handles the root/c/<text> url"""
    return f"C {escape(text).replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
