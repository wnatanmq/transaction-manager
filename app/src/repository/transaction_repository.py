from typing import Any
from fastapi                                import HTTPException, status
import sqlalchemy
from sqlalchemy                             import Row, Sequence, asc, desc
from app.src.model.transaction_model        import TransactionModel
from app.src.repository._repository         import Repository
from app.src.utils.logging                  import logging

logger = logging.getLogger(__name__)

class TransactionRepository(Repository):
    def __init__(self):
        super().__init__(table_name="transaction")

    def insert_transaction(self, transaction : TransactionModel):
        try:
            with self._engine.connect() as connection:
                statement = self._table.insert().values(
                    **transaction.model_dump()
                )
                connection.execute(statement)
                connection.commit()
        except sqlalchemy.exc.IntegrityError as err:
            logger.error(err)
            raise HTTPException(
                 status_code=status.HTTP_409_CONFLICT
            )
        except Exception as err:
            logger.error(err)
            raise err
        
    def get_have_some_transaction_like_count(self, transaction : TransactionModel):
        # TODO: Should have a query for 1 day before today
        with self._engine.connect() as connection:
            statement = self._table.select().where(self._table.c.sender_agency==transaction.sender_agency)\
                .where(self._table.c.sender_account==transaction.sender_account)\
                    .where(self._table.c.channel==transaction.channel)\
                        .where(self._table.c.amount==transaction.amount)
            return connection.execute(statement).rowcount

    def get_last_transaction_by_customer(self, agency :int, account: int) -> Sequence[Row[Any]]:
        # TODO: Add a join table to get name for every sender if debit, or receiver if credit        
        with self._engine.connect() as connection:
            statement_sender = self._table.select()\
                .where(self._table.c.sender_agency==agency)\
                    .where(self._table.c.sender_account==account)\
                .order_by(desc(self._table.c.timestamp)).limit(5)
            sender_ts = connection.execute(statement_sender).all() 
            
            statement_receiver = self._table.select()\
                .where(self._table.c.receiver_agency==agency)\
                    .where(self._table.c.receiver_account==account)\
                .order_by(desc(self._table.c.timestamp)).limit(5)
            receiver_ts = connection.execute(statement_receiver).all() 
            result = sender_ts + receiver_ts
            result = sorted(result, key=lambda x: x.timestamp, reverse=True)
        return result[:5]
