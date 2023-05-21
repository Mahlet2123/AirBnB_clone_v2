#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def state_list():
    """ display a HTML page with the list of all State objects
    present in DBStorage sorted by name (A->Z) """
    states = list(storage.all(State).values())
    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def remove_session(exception):
    """ a Flask teardown function.
    It is executed after each request to the Flask application. """
    storage.close()

if __name__ == "__main__":
    #storage.reload()
    app.run(host="0.0.0.0", port=5000)
