import unittest
from app.src.model.customer_model import CustomerModel, CustomerModelNoAlias


class TestCustomerModel(unittest.TestCase):
    def test_customer_model(self):
        model_validate = {
            "id" : "2321938#3213123",
            "agency" : 2321938,
            "account": 3213123,
            "name": "Mocklinio Stephen",
            "age": 44,
            "balance" : 540
        }
        model_to_validate = CustomerModelNoAlias(**model_validate)
        self.assertEqual(
            model_to_validate.id,
            f"{model_validate["agency"]}#{model_validate["account"]}"
        )
        self.assertEqual(
            model_to_validate.agency,
            model_validate["agency"]
        )
        self.assertEqual(
            model_to_validate.account,
            model_validate["account"]
        )