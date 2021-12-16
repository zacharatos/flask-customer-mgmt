from flask import Flask
from fcm.blueprints.webpage import webpage


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

    return app
