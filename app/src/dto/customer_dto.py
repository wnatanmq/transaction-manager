from typing     import Optional
from pydantic   import BaseModel, Field


class CustomerPost(BaseModel):
    agencia:int             = Field(... , ge=1, description="agency number")
    conta:  int             = Field(... , ge=1, description="account number")
    idade:  Optional[int]   = Field(None, ge=0, description="customer age")
    nome:   str             = Field(... , min_length=1, max_length=100, description="customer name")

class CustomerPut(CustomerPost):
    pass