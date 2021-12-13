from flask import Flask
from fcm.blueprints.webpage import webpage


def create_app():
    """
    The Factory Function for initialazing and creating a Flask App.
    """
    app = Flask(__name__, instance_relative_config=True)

    # Load Configuration files
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    # Register the blueprints to the main app
    app.register_blueprint(webpage)

    return app
