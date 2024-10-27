import unittest
from fastapi.testclient import TestClient
from fastapi import status
from app.src.main import app


class TestMain(unittest.TestCase):
    def test_health_check(self):
        client = TestClient(app)
        response = client.get("/health")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {"status": "online"}
        )