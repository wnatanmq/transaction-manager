from fastapi                                import HTTPException, status
import sqlalchemy
from app.src.model.transaction_model        import TransactionModel
from app.src.repository._repository         import Repository
from app.src.repository.customer_repository import CustomerRepository
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

