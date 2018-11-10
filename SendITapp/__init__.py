"""Import relevant package."""
from flask import Flask
from instance.config import Config
from SendITapp.api.v1 import superv1_blueprint


def create_app(config_class=Config):
    """Create the app."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(superv1_blueprint)
    return app
