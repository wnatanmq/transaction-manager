from typing import Union
from uuid import UUID

from fastapi import HTTPException, status
import sqlalchemy
from app.src.model.customer_model   import CustomerModel
from app.src.repository._repository import Repository
from app.src.utils.logging          import logging

logger = logging.getLogger(__name__)

class CustomerRepository(Repository):
    def __init__(self):
        super().__init__(
            table_name="customer"
        )

    def insert_customer(self, customer : CustomerModel):
        try:
            with self._engine.connect() as connection:
                insert_statement = self._table.insert().values(
                    **customer.model_dump()
                )
                connection.execute(insert_statement)
                connection.commit()
        except sqlalchemy.exc.IntegrityError as err:
            logger.error(err)
            raise HTTPException(
                 status_code=status.HTTP_409_CONFLICT
            )
        except Exception as err:
            logger.error(err)
            raise err
    
    def get_customer_by_agency_account(
        self,
        agency_sender: int,
        account_sender : int,
        agency_receiver: int,
        account_receiver : int
    ):
        with self._engine.connect() as connection:
            statement = self._table.select().filter(
                sqlalchemy.or_(
                    self._table.c.id==f"{agency_receiver}#{account_receiver}",
                    self._table.c.id==f"{agency_sender}#{account_sender}"
                    )
                )
            return connection.execute(statement).all()
