from fastapi import FastAPI
from utils import logging

app = FastAPI()

logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    return {"Hello": "World"}
