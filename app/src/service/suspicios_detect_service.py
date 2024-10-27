from app.src.dto.transaction_dto import TransactionPostDto
from app.src.enum.channel import Channel
from app.src.model.transaction_model import TransactionModel
from app.src.repository.customer_repository     import CustomerRepository
from app.src.repository.transaction_repository  import TransactionRepository


class SuspiciousDetectService():
    transation_hour_min = 10
    transation_hour_max = 16

    def __init__(self):
        self.transaction_repository = TransactionRepository()
        self.customer_repository    = CustomerRepository()

    def suspection_detect_rules(self, transaction : TransactionPostDto):
        rules = [
            self._validation_channel_by_channel,
            self._ibk_or_mbk_suspections,
            self._repeated_transaction_in_short_time,
            self._high_amount_for_non_frequenty_receiver,            
            self._uncommom_transaction_for_third_age_in_digital_channel
        ]
        result_rules = []
        for rule in rules:
            result = rule(transaction)
            if result:
                result_rules.append(result)
        return result_rules

    def _validation_channel_by_channel(self, transaction : TransactionPostDto):
        map_channel_validator = {
            Channel.TELLER : lambda transaction: None if transaction.data_e_hora_da_transacao.hour < self.transation_hour_max \
                and transaction.data_e_hora_da_transacao.hour > self.transation_hour_min\
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

    def _ibk_or_mbk_suspections(self, transaction : TransactionPostDto):
        if transaction.canal in [Channel.INTERNET_BANKING, Channel.MOBILE_BANKING]:
            transaction_model = transaction
            transaction_model.canal = Channel.INTERNET_BANKING if transaction.canal == Channel.MOBILE_BANKING \
                    else Channel.MOBILE_BANKING
            like_transaction = self.transaction_repository.get_have_some_transaction_like_count(
                transaction=TransactionModel(**transaction_model.model_dump())
            )
            return None if like_transaction == 0 else {
                "reason" : "ibk_or_mbk_like_transaction",
                "more" : {
                    "like_transaction_count" : f"{like_transaction}"
                }
            }
    def _repeated_transaction_in_short_time(self, transaction : TransactionPostDto):
        pass
    
    def _high_amount_for_non_frequenty_receiver(self, transaction : TransactionPostDto):
        pass    
    
    def _uncommom_transaction_for_third_age_in_digital_channel(self, transaction : TransactionPostDto):
        pass        
