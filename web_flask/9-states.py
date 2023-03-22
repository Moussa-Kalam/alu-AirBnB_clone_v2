#!/usr/bin/python3

"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_of_states():
    """loads states and cities"""
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template("9-states.html",
                           states=storage.all('State').values(),
                           state_id=state_id)


@app.teardown_appcontext
def teardown_db(self):
    """closes the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
