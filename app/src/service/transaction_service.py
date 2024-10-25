from typing import Union
from app.src.dto.transaction_dto                import TransactionPost
from app.src.model.transaction_model            import TransactionModel
from app.src.repository.transaction_repository  import TransactionRepository
from app.src.enum.channel                       import Channel
from datetime import datetime

class TransactionService():
    transation_hour_min = 10
    transation_hour_max = 16
    limit_atm_value     = 1000.0

    def __init__(self):
        self.repository = TransactionRepository()

    def create_transaction(self, transaction : TransactionPost):
        self.repository.insert_transaction(
            TransactionModel(**transaction.model_dump())
        )

    def suspection_detect_rules(self):
        rules = [
            self._hour_validation
        ]
    
    def _hour_validation_channel(self, transaction : TransactionPost):
        map_channel_validator = {
            Channel.TELLER : lambda transaction: None if transaction.data_e_hora_da_transacao.hour < self.transation_hour_max \
                and transaction.data_e_hora_da_transacao.hour > self.transation_hour_max\
                    else {
                        "reason" : "out_hour_limit_range",
                        "more" : {
                            "hour" : f"{transaction.data_e_hora_da_transacao.hour}"
                        }
                    },
            Channel.ATM : lambda transaction: None if transaction.valor_da_transacao > self.transation_hour_max\
                    else {
                        "reason" : "out_hour_limit_range",
                        "more" : {
                            "hour" : f"{transaction.valor_da_transacao}"
                        }
                    }
        }
        if fn_channel_validato := map_channel_validator.get(transaction.canal):
            fn_channel_validato(transaction)

    def _ibk_or_mbk_suspections(self, transaction : TransactionPost):
        if transaction.canal not in [Channel.INTERNET_BANKING, Channel.MOBILE_BANKING]:
            self.repository.get_transactions_by_sender(
                channel=Channel.INTERNET_BANKING if transaction.canal == Channel.MOBILE_BANKING \
                    else Channel.MOBILE_BANKING,
                account=transaction.conta_de_origem,
                agency=transaction.agencia_de_origem
            )
