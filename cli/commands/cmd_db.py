import click

from sqlalchemy_utils import database_exists

from fcm.app import create_app
from fcm.extensions import db

# Create app context for the database connection
app = create_app()
db.app = app


@click.command()
@click.option('--drop-db/--no-drop-db', default=False,
              help='Drop the databse if exists?')
def cli(drop_db):
    """
    A click function for initializing the databse if it
    does not already exists.
    """
    if drop_db:
        print("Dropping old database. . .")
        db.drop_all()

    db.create_all()

    return None
