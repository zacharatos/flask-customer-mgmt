import pytest
from fcm.app import create_app


# Create a wrapper for receiving the whole app
@pytest.fixture(scope='session')
def app():
    """
    This is the function which executed only once in the tests
    for the whole flask application and creates an example app to run our
    tests on it.
    """
    params = {
        'DEBUG': False,
        'TESTING': True,
    }

    _app = create_app(settings_override=params)

    # Create an application for running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app
    ctx.pop()


@pytest.fixture(scope='function')
def client(app):
    """
    The function for running the test in the application.
    It runs in every test.
    """
    yield app.test_client()
