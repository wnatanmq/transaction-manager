from typing                                 import Union
from app.src.dto.customer_dto               import CustomerPostDto, CustomerPut
from app.src.model.customer_model           import CustomerModel
from app.src.repository.customer_repository import CustomerRepository



class CustomerService():
    def __init__(self):
        self.repository = CustomerRepository()

    def create_customer(self, customer : Union[CustomerPut, CustomerPostDto]):
        self.repository.insert_customer(CustomerModel(**customer.model_dump()))

    def get_customer(self, customer : Union[CustomerPut, CustomerPostDto]):
        self.repository.insert_customer(CustomerModel(**customer.model_dump()))

    