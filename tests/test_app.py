from src import app
import pytest


def test_prices():
    with app.app.test_client() as client:
        response = client.get(f'/price')
        assert response.status_code == 200
        assert response.get_json() == 123
