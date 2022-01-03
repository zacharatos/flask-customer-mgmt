from flask import Flask

from fcm.blueprints.webpage import webpage
from fcm.blueprints.customer import customer
from fcm.blueprints.product import product

from fcm.extensions import debug_toolbar
from fcm.extensions import csrf
from fcm.extensions import db
# from fcm.extensions import login_manager


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
    app.register_blueprint(customer)
    app.register_blueprint(product)

    # Load the extensions in the app
    extensions(app)

    return app


def extensions(app):
    """
    A function for registering extensions to our flask application
    """
    debug_toolbar.init_app(app)
    csrf.init_app(app)
    db.init_app(app)
    # login_manager.init_app(app)

    return None
