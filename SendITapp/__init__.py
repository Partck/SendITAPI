"""Import relevant package."""
import os
from flask import Flask, make_response, jsonify
from instance.config import Config
from SendITapp.api.v1 import superv1_blueprint
from SendITapp.api.v2 import superv2_blueprint
from SendITapp.db_config import DbConfig
from flask_jwt_extended import JWTManager


def page_not_found(e):
    return make_response(jsonify(
        {"Message": "The URL you have entered is not on this server"}), 404)


def create_app(config_class=Config):
    """Create the app."""
    app = Flask(__name__)
    db = DbConfig()
    db.init_db()
    db.create_tables()
    app.config.from_object(config_class)
    app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET_KEY') or "candy"
    jwt = JWTManager(app)
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.register_blueprint(superv1_blueprint)
    app.register_blueprint(superv2_blueprint)
    app.register_error_handler(404, page_not_found)
    return app