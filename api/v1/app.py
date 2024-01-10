#!/usr/bin/python3
"""
Flask API Setup
"""

from flask import Flask, jsonify, make_response, Blueprint
from models import storage
from flask_cors import CORS
from models.engine import *
from api.v1.views import app_views
from os import getenv


""" Flask instances """
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_close(error):
    """ Close file and delete database """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ function to handle error 404 """
    return jsonify({'error': "Not found"}), 404


if __name__ == '__main__':
    host = getenv("HBNB_API_HOST")
    if host is None:
        host = '0.0.0.0'
    port = getenv("HBNB_API_PORT")
    if port is None:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
