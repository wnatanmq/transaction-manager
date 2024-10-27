from typing     import Optional
from pydantic   import BaseModel, Field


class CustomerPostDto(BaseModel):
    agencia:int             = Field(... , description="agency number",  ge=1)
    conta:  int             = Field(... , description="account number", ge=1)
    idade:  Optional[int]   = Field(None, description="customer age",   ge=0)
    nome:   str             = Field(... , min_length=1, max_length=100, description="customer name")

class CustomerPut(CustomerPostDto):
    pass