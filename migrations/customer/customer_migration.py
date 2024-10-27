import os 
from sqlalchemy     import create_engine, MetaData, Table, Column, Integer, String, Float
from utils.logging  import logging

logger = logging.getLogger(__name__)

def customer_migration_handler():
    try:
        logger.info("starting transaction migration.")
        uri_postgresql = os.getenv("URI_POSTGRESQL")
        logger.debug({
            "uri_postgresql" : uri_postgresql
        })    
        engine = create_engine(uri_postgresql)
        metadata = MetaData()
        table = Table('customer', metadata,
            Column('id', 
                String, 
                primary_key=True
            ),
            Column('name'   , String    ),
            Column('age'    , String    ),        
            Column('agency' , Integer   ),
            Column('account', Integer   ),
            Column('balance', Float     ),            
        )
        table.create(bind=engine)        
        logger.info("transaction migration has finished.")
    except Exception as e:
        logger.error({"e" : e})
