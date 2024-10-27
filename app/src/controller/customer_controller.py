from typing import Union
from http import HTTPStatus
from fastapi import APIRouter, status, Response

from app.src.dto.customer_dto import CustomerPostDto, CustomerPut
from app.src.model.customer_model import CustomerModel
from app.src.service.customer_service import CustomerService

customer_controller = APIRouter()

# @customer_controller.put("/customer/{agency}/{account}")
# def customer_put(
#         agency : int,
#         account : int,
#         customer : CustomerPut,
#         response: Response
#     ):
#     CustomerService().create_customer(customer)
#     response.status_code = status.HTTP_201_CREATED

@customer_controller.post("/customer")
def customer_put(customer : CustomerPostDto, response: Response):
    CustomerService().create_customer(customer)
    response.status_code = status.HTTP_201_CREATED
