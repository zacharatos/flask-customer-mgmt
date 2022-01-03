from datetime import timedelta

DEBUG = True

# Flask related settings
SERVER_NAME = 'localhost:8000'
SECRET_KEY = 'thisisonlyfordev'

# SQLAlchemy related settings
SQLALCHEMY_DATABASE_URI = 'postgresql://fcm:simplepass@0.0.0.0:5432/fcm'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Seed user in database
SEED_ADMIN_EMAIL = 'dev@local.host'
SEED_ADMIN_PASSWORD = 'simplepass'
REMEMBER_COOKIE_DURATION = timedelta(days=30)
