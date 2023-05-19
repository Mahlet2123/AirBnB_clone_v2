#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
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
    return "C {}".format(escape(text).replace("_", " "))


@app.route("/python", strict_slashes=False, defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Handles the root/python/(<text>) url"""
    return "Python {}".format(escape(text).replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Handles the root/number/n url"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Handles the root/number_template/n url"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """Handles the root/number_odd_or_even/n url"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
