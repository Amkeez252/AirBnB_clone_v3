#!/usr/bin/python3

"""
Created for app.py
@author; Auwal Abdulmalik 

"""
from os import getenv
from flask import Flask, jsonify, Blueprint
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})





@app.teardown_appcontext
def close_db_sesion(error):
    """ this for slash routing"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """handler for 404 errors that returns a JSON-formatted
    404 status code response.
    """
    return ({'error': 'Not found'}), 404


if __name__ == "__main__":
    HBNB_API_HOST = getenv('HBNB_API_HOST')
    HBNB_API_PORT = getenv('HBNB_API_PORT')
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT,
            threaded=True, debug=True)
