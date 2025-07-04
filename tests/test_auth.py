"""
Integration tests for authentication routes.
"""
import pytest
from flask import url_for

class TestAuthRoutes:
    """Test cases for authentication routes."""
    
    def test_register_page_loads(self, client):
        """Test that the register page loads correctly."""
        response = client.get('/auth/register')
        assert response.status_code == 200
        assert b'Sign Up' in response.data or b'Register' in response.data
    
    def test_login_page_loads(self, client):
        """Test that the login page loads correctly."""
        response = client.get('/auth/login')
        assert response.status_code == 200
        assert b'Sign In' in response.data or b'Login' in response.data
    
    def test_user_registration(self, client, app):
        """Test user registration process."""
        response = client.post('/auth/register', data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password123',
            'password2': 'password123'
        }, follow_redirects=True)
        
        assert response.status_code == 200
        
        # Check that user was created in database
        with app.app_context():
            from app.models import User
            user = User.query.filter_by(username='newuser').first()
            assert user is not None
            assert user.email == 'newuser@example.com'
    
    def test_user_login(self, client, test_user):
        """Test user login process."""
        response = client.post('/auth/login', data={
            'email': 'test@example.com',
            'password': 'testpass'
        }, follow_redirects=True)
        
        assert response.status_code == 200
        # Should redirect to dashboard or home page after login
    
    def test_invalid_login(self, client):
        """Test login with invalid credentials."""
        response = client.post('/auth/login', data={
            'email': 'nonexistent@example.com',
            'password': 'wrongpassword'
        })
        
        # Should stay on login page or show error
        assert response.status_code in [200, 302]
    
    def test_logout(self, client, auth, test_user):
        """Test user logout process."""
        # First login
        auth.login()
        
        # Then logout
        response = client.get('/auth/logout', follow_redirects=True)
        assert response.status_code == 200
    
    def test_password_mismatch_registration(self, client):
        """Test registration with mismatched passwords."""
        response = client.post('/auth/register', data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
            'password2': 'different_password'
        })
        
        # Should stay on registration page with error
        assert response.status_code == 200
        # Form should show validation error
    
    @pytest.mark.integration
    def test_login_required_access(self, client):
        """Test that protected routes require login."""
        response = client.get('/dashboard')
        # Should redirect to login page
        assert response.status_code == 302
        assert '/auth/login' in response.location or 'login' in response.location
