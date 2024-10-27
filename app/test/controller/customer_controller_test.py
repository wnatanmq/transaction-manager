from unittest.mock import MagicMock, patch
from app.src.controller.customer_controller import customer_controller
from fastapi import FastAPI, status


import unittest
from fastapi.testclient import TestClient

customer_mocks = [
    {
        "agencia":130032,
        "conta":1110044,
        "idade":30,
        "nome":"Mockelin Silva"
    }
]

class TestMain(unittest.TestCase):

    @patch("app.src.controller.customer_controller.CustomerService")
    def test_post_customer(self, customer_service_mock : MagicMock):
        app = FastAPI()
        app.include_router(customer_controller)
        client = TestClient(app)
        response = client.post(
            "/customer",
            json=customer_mocks[0]
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

