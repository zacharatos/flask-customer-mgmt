from flask import Flask

from fcm.blueprints.webpage import webpage
from fcm.extensions import debug_toolbar


def create_app(settings_override=None):
    """
    The Factory Function for initialazing and creating a Flask App.
    """
    app = Flask(__name__, instance_relative_config=True)

    # Load Configuration files
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    # Check if this file is used by tests and
    # update the configuration files appropriately.
    if settings_override:
        app.config.update(settings_override)

    # Register the blueprints to the main app
    app.register_blueprint(webpage)

    # Load the extensions in the app
    extensions(app)

    return app


def extensions(app):
    """
    A function for registering extensions to our flask application
    """
    debug_toolbar.init_app(app)

    return None
