import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_page(client):
    """Test that the index page loads."""
    response = client.get('/')
    assert response.status_code in [200, 302]  # 200 OK or 302 redirect if not logged in


def test_register_page(client):
    """Test that the register page loads."""
    response = client.get('/register')
    assert response.status_code in [200, 302]


def test_login_page(client):
    """Test that the login page loads."""
    response = client.get('/login')
    assert response.status_code in [200, 302]


def test_app_exists():
    """Test that the Flask app exists."""
    assert app is not None


def test_app_is_testing():
    """Test Flask app configuration."""
    app.config['TESTING'] = True
    assert app.config['TESTING'] is True
