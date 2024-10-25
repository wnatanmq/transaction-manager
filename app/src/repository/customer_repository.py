from app.src.model.customer_model   import CustomerModel
from app.src.repository._repository import Repository
from app.src.utils.logging          import logging

logger = logging.getLogger(__name__)

class CustomerRepository(Repository):
    def insert_customer(self, customer : CustomerModel):
        with self._engine.connect() as connection:
            insert_statement = self._table.insert().values(
                **customer.model_dump()
            )
            connection.execute(insert_statement)
            connection.commit()
