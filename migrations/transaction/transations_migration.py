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
        table = Table('transaction', metadata,
            Column('id', 
                String, 
                primary_key=True
            ),
            Column('amount'   , Float   ),
            Column('timestamp'    , Time),        
            Column('channel' ,  Integer),
            Column('sender_agency', Integer     ),
            Column('sender_account', Integer    ),
            Column('receiver_agency', Integer    ),
            Column('receiver_account', Integer   ),
        )
        table.create(bind=engine)
        logger.info("customer migration has finished.")
    except Exception as e:
        logger.error({"e" : e})