import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

API_KEY = "key"


def test_create_order():
    response = client.post(
        "/orders/",
        headers={"X-API-Key": API_KEY},
        json={"drink_name": "Espresso", "size": "small", "price": 120}
    )
    assert response.status_code == 200
    assert response.json()["drink_name"] == "Espresso"


def test_get_orders():
    response = client.get("/orders/", headers={"X-API-Key": API_KEY})
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_statistics():
    response = client.get("/orders/statistics/", headers={"X-API-Key": API_KEY})
    assert response.status_code == 200
    assert "total_orders" in response.json()
    assert "average_price" in response.json()
