from pydantic   import BaseModel, Field
from typing     import Optional
from datetime   import date

class Customer(BaseModel):
    agency:     int             = Field(..., ge=1, description="Número da agência")
    account:    int             = Field(..., ge=1, description="Número da conta")
    name:       str             = Field(..., min_length=1, max_length=100, description="Nome do cliente")
    age:        Optional[int]   = Field(None, ge=0, description="Idade do cliente")
