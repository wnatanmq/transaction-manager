from fastapi                                    import FastAPI
from app.src.controller.transaction_controller  import transaction_controller
from app.src.controller.customer_controller     import customer_controller
from app.src.utils.logging                      import logging
from dotenv                                     import load_dotenv

load_dotenv()

# def main():
app = FastAPI()

logger = logging.getLogger(__name__)
logger.info("app is up.")

app.include_router(customer_controller      )
app.include_router(transaction_controller   )

@app.get("/health")
def health_check():
    logger.debug("health check.")        
    return {"status": "online"}

# main()