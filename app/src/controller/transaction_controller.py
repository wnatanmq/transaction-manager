from typing                                 import Union
from http                                   import HTTPStatus
from fastapi                                import APIRouter, status, Response

from app.src.dto.transaction_dto            import TransactionPost
from app.src.service.transaction_service    import TransactionService

transaction_controller = APIRouter()

@transaction_controller.post("/transaction")
def transaction_put(transaction : TransactionPost, response: Response):
    TransactionService().create_transaction(
        transaction
    )
    response.status_code = status.HTTP_201_CREATED
