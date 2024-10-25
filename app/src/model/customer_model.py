from pydantic   import BaseModel, Field
from typing     import Optional
from uuid       import UUID, uuid4


class CustomerModel(BaseModel):
    id      :UUID           = Field(default_factory=uuid4)
    agency  :int            = Field(..., ge=1,  alias="agencia",    description="Número da agência" )
    account :int            = Field(..., ge=1,  alias="conta",      description="Número da conta"   )
    name    :str            = Field(...,        alias="nome",       description="Nome do cliente", min_length=1, max_length=100,)
    age     :Optional[int]  = Field(None,ge=0,  alias="idade",      description="Idade do cliente"  )
