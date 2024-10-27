import os
from sqlalchemy                         import MetaData, Table, create_engine
from app.src.utils.logging              import logging

logger = logging.getLogger(__name__)

class Repository():
    def __init__(self, table_name):
        self.table_name = table_name
        uri_postgresql = os.getenv("URI_POSTGRESQL")
        logger.debug({
            "uri_postgresql" : uri_postgresql
        })            
        self._engine = create_engine(uri_postgresql)
        self._table = Table(
            self.table_name, 
            MetaData(), 
            autoload_with=self._engine
        )
