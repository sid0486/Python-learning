from fastapi.testclient import TestClient
from main import app
import random

client = TestClient(app)

def test_get_students():
    response = client.get("/students/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_student():
    data = {
    "name": f"TestStudent{random.randint(1000, 9999)}",
    "std": 10,
    "address": "Laxmi Nagar",
    "mobile": "9313429179"
}
    response = client.post("/students/", json=data)
    assert response.status_code == 200

def test_get_student():
    response = client.get("/students/1")
    assert response.status_code in [200, 404]

def test_delete_student():
    response = client.delete("/students/1")
    assert response.status_code in [200, 404]