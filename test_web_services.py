from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Available APIs: create_user"}


def test_get_user():
    response = client.get("/user/1234")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Received parameters succesfully",
        "user_id": 1234,
    }

