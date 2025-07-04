"""
Unit tests for the Flask application models.
"""
import pytest
from app.models import User

class TestUserModel:
    """Test cases for the User model."""
    
    def test_user_creation(self, app):
        """Test creating a new user."""
        with app.app_context():
            user = User(username='testuser', email='test@example.com')
            assert user.username == 'testuser'
            assert user.email == 'test@example.com'
            assert user.password_hash is None
    
    def test_password_hashing(self, app):
        """Test password hashing and verification."""
        with app.app_context():
            user = User(username='testuser', email='test@example.com')
            user.set_password('testpassword')
            
            # Password should be hashed
            assert user.password_hash is not None
            assert user.password_hash != 'testpassword'
            
            # Check password verification
            assert user.check_password('testpassword') is True
            assert user.check_password('wrongpassword') is False
    
    def test_user_repr(self, app):
        """Test user string representation."""
        with app.app_context():
            user = User(username='testuser', email='test@example.com')
            assert repr(user) == '<User testuser>'
    
    def test_duplicate_username(self, app):
        """Test that duplicate usernames are handled properly."""
        with app.app_context():
            from app import db
            
            # Create first user
            user1 = User(username='testuser', email='test1@example.com')
            user1.set_password('password1')
            db.session.add(user1)
            db.session.commit()
            
            # Try to create second user with same username
            user2 = User(username='testuser', email='test2@example.com')
            user2.set_password('password2')
            db.session.add(user2)
            
            # This should raise an integrity error
            with pytest.raises(Exception):
                db.session.commit()
