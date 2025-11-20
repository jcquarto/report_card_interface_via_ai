import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestIndexPage:
    """Test the index page."""
    
    def test_index_page_loads(self, client):
        """Test that the index page loads successfully."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Report Card Interface' in response.data
    
    def test_index_page_shows_all_three_types(self, client):
        """Test that the index page displays all three report card types."""
        response = client.get('/')
        assert b'Funnel Report Card' in response.data
        assert b'QuickBooks Core Report Card' in response.data
        assert b'Custom Agency Report Card' in response.data
    
    def test_index_page_shows_sample_cards(self, client):
        """Test that the index page shows the sample report cards."""
        response = client.get('/')
        assert b'Q4 2024 Sales Funnel' in response.data
        assert b'November 2024 Financial Summary' in response.data
        assert b'Digital Marketing Campaign Performance' in response.data


class TestShowPage:
    """Test the show page."""
    
    def test_show_funnel_report_card(self, client):
        """Test showing a Funnel Report Card."""
        response = client.get('/report_card/1')
        assert response.status_code == 200
        assert b'Funnel Report Card' in response.data
        assert b'Q4 2024 Sales Funnel' in response.data
    
    def test_show_quickbooks_report_card(self, client):
        """Test showing a QuickBooks Core Report Card."""
        response = client.get('/report_card/2')
        assert response.status_code == 200
        assert b'QuickBooks Core Report Card' in response.data
        assert b'November 2024 Financial Summary' in response.data
    
    def test_show_custom_agency_report_card(self, client):
        """Test showing a Custom Agency Report Card."""
        response = client.get('/report_card/3')
        assert response.status_code == 200
        assert b'Custom Agency Report Card' in response.data
        assert b'Digital Marketing Campaign Performance' in response.data
    
    def test_show_non_existent_report_card(self, client):
        """Test showing a non-existent report card returns 404."""
        response = client.get('/report_card/999')
        assert response.status_code == 404
        assert b'404' in response.data
        assert b'Report Card Not Found' in response.data
    
    def test_show_page_has_back_link(self, client):
        """Test that show pages have a back link."""
        response = client.get('/report_card/1')
        assert b'Back to All Report Cards' in response.data
