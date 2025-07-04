"""
Test configuration and fixtures for the Flask application.
"""
import pytest
import tempfile
import os
from app import create_app, db
from app.models import User

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # Create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()
    
    test_config = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': f'sqlite:///{db_path}',
        'WTF_CSRF_ENABLED': False,  # Disable CSRF for testing
        'SECRET_KEY': 'test-secret-key'
    }
    
    app = create_app(test_config=test_config)

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()

@pytest.fixture
def auth(client):
    """Authentication actions."""
    class AuthActions(object):
        def __init__(self, client):
            self._client = client

        def login(self, email='test@example.com', password='testpass'):
            return self._client.post(
                '/auth/login',
                data={'email': email, 'password': password}
            )

        def logout(self):
            return self._client.get('/auth/logout')

        def register(self, email='test@example.com', username='testuser', password='testpass'):
            return self._client.post(
                '/auth/register',
                data={
                    'email': email,
                    'username': username,
                    'password': password,
                    'password2': password
                }
            )

    return AuthActions(client)

@pytest.fixture
def test_user(app):
    """Create a test user."""
    with app.app_context():
        user = User(username='testuser', email='test@example.com')
        user.set_password('testpass')
        db.session.add(user)
        db.session.commit()
        return user
