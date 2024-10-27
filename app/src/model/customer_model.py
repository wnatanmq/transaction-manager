from pydantic   import BaseModel, Field, model_validator, root_validator
from typing     import Optional, Self


class CustomerModel(BaseModel):
    id      :str            = Field(None)
    agency  :int            = Field(..., ge=1,  alias="agencia",    description="Número da agência" )
    account :int            = Field(..., ge=1,  alias="conta",      description="Número da conta"   )
    name    :str            = Field(...,        alias="nome",       description="Nome do cliente", min_length=1, max_length=100,)
    age     :Optional[int]  = Field(None,ge=0,  alias="idade",      description="Idade do cliente"  )
    balance :float          = Field(default=0,                      description="Balanco dinheiro"  )

    
    @model_validator(mode='after')
    def add_automatic_fields(self) -> Self:
        self.id = f"{self.agency}#{self.account}" 
        return self

class CustomerModelNoAlias(BaseModel):
    id      :str            = Field(None)
    agency  :int            = Field(..., ge=1,      description="Número da agência")
    account :int            = Field(..., ge=1,      description="Número da conta")
    name    :str            = Field(...,            description="Nome do cliente", min_length=1, max_length=100,)
    age     :Optional[int]  = Field(None,ge=0,      description="Idade do cliente")
    balance :float          = Field(...,            description="Balanco dinheiro")
