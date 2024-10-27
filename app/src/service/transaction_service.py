from fastapi                                    import HTTPException, status
from typing                                     import List
from app.src.dto.transaction_dto                import TransactionPostDto
from app.src.model.transaction_model            import TransactionModel, TransactionModelNoAlias
from app.src.model.customer_model               import CustomerModelNoAlias
from app.src.repository.transaction_repository  import TransactionRepository
from app.src.repository.customer_repository     import CustomerRepository
from app.src.service.suspicios_detect_service   import SuspiciousDetectService
from app.src.utils.logging                      import logging
from datetime import datetime


logger = logging.getLogger(__name__)

class TransactionService():
    transation_hour_min = 10
    transation_hour_max = 16

    def __init__(self):
        self.transaction_repository     = TransactionRepository()
        self.customer_repository        = CustomerRepository()
        self.suspicios_detect_service   = SuspiciousDetectService()

    def create_transaction(self, transaction : TransactionPostDto):
        customers = self.customer_repository.get_customer_by_agency_account(
            account_sender=transaction.conta_de_origem,
            agency_sender=transaction.agencia_de_origem,
            account_receiver=transaction.conta_de_destino,
            agency_receiver=transaction.agencia_de_destino
        )
        if len(customers) != 2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="wrong with receiver or sender customer, someone dont exits."
            )
        customer_receiver = CustomerModelNoAlias(**customers[0]._asdict()) \
            if customers[0].id == f"{transaction.agencia_de_origem}#{transaction.conta_de_origem}"\
            else CustomerModelNoAlias(**customers[1]._asdict()) 
        customer_sender = CustomerModelNoAlias(**customers[1]._asdict()) \
            if customers[0].id == customer_receiver.id else CustomerModelNoAlias(**customers[0]._asdict())
        if result_suspect_analisys := self.suspicios_detect_service.suspection_detect_rules(transaction):
            logger.warning({
                "error" : "error_by_suspicious_validation",
                "detail": {
                    "result_suspect_analisys" : result_suspect_analisys
                }
            })
            transaction.suspect = True
        self.transaction_repository.insert_transaction(
            TransactionModel(**transaction.model_dump())
        )
        self.customer_repository.update_customer_balance(
            transaction=transaction,
            customer_sender=customer_sender,
            customer_receiver=customer_receiver
        )

    def get_last_transaction_by_customer(self, agency :int, account: int) -> List[TransactionModelNoAlias]:
        if last_transaction := self.transaction_repository.get_last_transaction_by_customer(
            account=account,
            agency=agency
        ):
            return list(map(lambda x:TransactionModelNoAlias(**x._asdict()),last_transaction))