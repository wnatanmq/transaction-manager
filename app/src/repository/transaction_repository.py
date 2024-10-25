from app.src.model.transaction_model    import TransactionModel
from app.src.repository._repository     import Repository
from app.src.utils.logging              import logging

logger = logging.getLogger(__name__)

class TransactionRepository(Repository):
    def insert_transaction(self, transaction : TransactionModel):
        with self._engine.connect() as connection:
            statement = self._table.insert().values(
                **transaction.model_dump()
            )
            connection.execute(statement)
            connection.commit()

    def get_transactions_by_sender_and_channel(self, agency : int, account : int, canal : int):
        with self._engine.connect() as connection:
            statement = self._table.select().where(
                self._table.c.sender_agency==agency and\
                    self._table.c.sender_account==account and\
                        self._table.c.channel==canal
            )
            connection.execute(statement)
            connection.commit()
            
