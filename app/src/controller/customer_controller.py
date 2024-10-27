from typing import Union
from http import HTTPStatus
from fastapi import APIRouter, status, Response

from app.src.dto.customer_dto import CustomerPostDto, CustomerPut
from app.src.model.customer_model import CustomerModel
from app.src.service.customer_service import CustomerService
from app.src.service.transaction_service import TransactionService

customer_controller = APIRouter()

@customer_controller.post("/customer")
def customer_put(customer : CustomerPostDto, response: Response):
    CustomerService().create_customer(customer)
    response.status_code = status.HTTP_201_CREATED

@customer_controller.get("/customer/{agency}/{account}")
def customer_put(agency :int, account: int):
    if customer := CustomerService().get_customer(
        agency=agency,
        account=account
    ):
        last_transaction = TransactionService().get_last_transaction_by_customer(
            agency=agency,
            account=account
        )
        last_transaction = list(map(lambda x: 
            {
                "agencia": x.receiver_agency,
                "conta": x.receiver_account,
                "type": "debit",
                "valor": x.amount,
                "suspect": x.suspect
            } if f"{x.sender_agency}#{x.sender_account}" == f"{agency}#{account}" else 
            {
                "agencia": x.sender_agency,
                "conta": x.sender_account,
                "type": "credit",
                "valor": x.amount,
                "suspect": x.suspect
            }, 
            last_transaction))
        
        return {
        "nome": customer.name,
        "idade": customer.age,
        "last_transactions": last_transaction,
        "balance": customer.balance
        }
