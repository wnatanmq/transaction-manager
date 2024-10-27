from typing                                 import Union
from app.src.dto.customer_dto               import CustomerPostDto, CustomerPut
from app.src.model.customer_model           import CustomerModel, CustomerModelNoAlias
from app.src.repository.customer_repository import CustomerRepository



class CustomerService():
    def __init__(self):
        self.repository = CustomerRepository()

    def create_customer(self, customer : Union[CustomerPut, CustomerPostDto]):
        self.repository.insert_customer(CustomerModel(**customer.model_dump()))

    def get_customer(
        self,
        agency: int,
        account : int
        ) -> Union[CustomerModelNoAlias, None]:
        customer = self.repository.get_customer_by_key(
            agency=agency,
            account=account
        )
        return CustomerModelNoAlias(**customer._asdict()) if customer else None

    