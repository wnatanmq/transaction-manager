from typing                                 import Union
from http                                   import HTTPStatus
from fastapi                                import APIRouter, status, Response

from app.src.dto.transaction_dto            import TransactionPostDto
from app.src.service.transaction_service    import TransactionService

transaction_controller = APIRouter()

@transaction_controller.post("/transaction")
def transaction_put(transaction : TransactionPostDto, response: Response):
    TransactionService().create_transaction(
        transaction
    )
    response.status_code = status.HTTP_201_CREATED
    return {
        "suspect" : transaction.suspect
    }
