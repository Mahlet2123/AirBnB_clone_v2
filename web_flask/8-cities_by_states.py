#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)

@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """ for fetching data from the storage engine """
    states = list(storage.all(State).values())
    # states list contains all State objects stored in the database.
    return render_template("8-cities_by_states.html", states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """
    close the database connection after
    the request has been processed.
    """
    storage.close()

if __name__ == "__main__":
    storage.reload()
    app.run(host="0.0.0.0", port=5000)
