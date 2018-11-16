"""Import relevant package."""
from flask import Flask, make_response, jsonify
from instance.config import Config
from SendITapp.api.v1 import superv1_blueprint
from SendITapp.api.v2 import superv2_blueprint


def page_not_found(e):
    return make_response(jsonify(
        {"Message": "The URL you have entered is not on this server"}), 404)


def create_app(config_class=Config):
    """Create the app."""
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(superv1_blueprint)
    app.register_blueprint(superv2_blueprint)
    app.register_error_handler(404, page_not_found)
    return app
