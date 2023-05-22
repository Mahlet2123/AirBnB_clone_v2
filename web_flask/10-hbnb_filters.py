#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)

@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    display a HTML page like 6-index.html, which was done
    during the project 0x01. AirBnB clone - Web static
    """
    states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)

@app.teardown_appcontext
def teardown_db(exception):
    """
    close the database connection after
    the request has been processed.
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
