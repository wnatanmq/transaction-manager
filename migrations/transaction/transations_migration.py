from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, Uuid, Time
import os 

from utils.logging import logging

logger = logging.getLogger(__name__)

def transaction_migration_handler():
    try:
        logger.info("starting customer migration.")
        uri_postgresql = os.getenv("URI_POSTGRESQL")
        logger.debug({
            "uri_postgresql" : uri_postgresql
        })    
        engine = create_engine(uri_postgresql)
        metadata = MetaData()
        Table('customer', metadata,
            Column('id', 
                Uuid, 
                primary_key=True
            ),
            Column('amount'   , Float   ),
            Column('timestamp'    , Time),        
            Column('channel' ,  Integer),
            # considerar o canal como fkey
            Column('sender_agency', Integer     ),
            Column('sender_account', Integer    ),
            Column('receiver_agency', Integer    ),
            Column('receiver_account', Integer   ),
        )
        metadata.create_all(engine)
        logger.info("customer migration has finished.")
    except Exception as e:
        logger.error(e)