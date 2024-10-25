import os
from sqlalchemy                         import MetaData, Table, create_engine
from app.src.utils.logging              import logging

logger = logging.getLogger(__name__)

class Repository():
    def __init__(self):
        uri_postgresql = os.getenv("URI_POSTGRESQL")
        logger.debug({
            "uri_postgresql" : uri_postgresql
        })            
        self._engine = create_engine(uri_postgresql)
        self._table = Table(
            'transaction', 
            MetaData(), 
            autoload_with=self._engine
        )
