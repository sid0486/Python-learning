from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_product():
    data = {
        "name": "Tablet",
        "description": "Android tablet",
        "price": 15000,
        "quantity": 2
    }
    response = client.post("/products/", json=data)
    assert response.status_code == 200

def test_get_product():
    response = client.get("/products/1")
    assert response.status_code in [200, 404]

def test_delete_product():
    response = client.delete("/products/1")
    assert response.status_code in [200, 404]