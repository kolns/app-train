"""
Integration tests for main application routes.
"""
import pytest

class TestMainRoutes:
    """Test cases for main application routes."""
    
    def test_home_page(self, client):
        """Test that the home page loads correctly."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Welcome' in response.data or b'Home' in response.data
    
    def test_404_error(self, client):
        """Test 404 error handling."""
        response = client.get('/nonexistent-page')
        assert response.status_code == 404
    
    @pytest.mark.integration
    def test_navigation_links(self, client):
        """Test that navigation links work correctly."""
        response = client.get('/')
        assert response.status_code == 200
        
        # Check that common navigation elements exist
        data = response.data.decode()
        # This will depend on your actual navigation structure
