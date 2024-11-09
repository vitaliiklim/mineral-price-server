import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_mineral_price(client):
    response = client.get('/mineral-price')
    assert response.status_code == 200
    data = response.get_json()
    assert "mineral" in data
    assert "price" in data
    assert "currency" in data
