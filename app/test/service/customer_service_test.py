import unittest
from unittest.mock import MagicMock, patch
from app.src.dto.customer_dto import CustomerPut
from app.src.model.customer_model import CustomerModel
from app.src.service.customer_service import CustomerService

customer_mocks = [
    {
        "agencia":130032,
        "conta":1110044,
        "idade":30,
        "nome":"Mockelin Silva"
    }
]

class TestMain(unittest.TestCase):

    @patch("app.src.service.customer_service.CustomerRepository")
    def test_default(self, customer_repository_mock : MagicMock):
        customer_service = CustomerService()
        customer_post = CustomerPut(**customer_mocks[0])
        self.assertEqual(
            customer_service.create_customer(customer_post),
            None
        )
        customer_repository_mock.return_value.insert_customer.assert_called_once_with(
            CustomerModel(**customer_post.model_dump())
        )
