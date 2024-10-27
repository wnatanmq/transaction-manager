import unittest
from fastapi.testclient import TestClient
from src.main import app


class TestMain(unittest.TestCase):
    def test_health_check():
        client = TestClient(app)
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}
