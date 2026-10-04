"""
Unit tests for the application
"""
import unittest
from src.app import app


class TestApp(unittest.TestCase):
    """Test cases for Flask application"""

    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        """Test home endpoint"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')

    def test_health(self):
        """Test health check endpoint"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'healthy')

    def test_api_endpoint(self):
        """Test API data endpoint"""
        response = self.app.get('/api/v1/data')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['count'], 5)


if __name__ == '__main__':
    unittest.main()
