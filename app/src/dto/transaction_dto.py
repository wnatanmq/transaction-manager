from typing     import Optional
from pydantic   import BaseModel, Field
from datetime   import datetime

class TransactionPostDto(BaseModel):
    id_da_transacao             :str            = Field(... , description="transaction unique id", min_length=1, max_length=100,)
    data_e_hora_da_transacao    :datetime       = Field(... , description="transaction timestamp")
    valor_da_transacao          :float          = Field(... , description="transaction amount",                 ge=0)
    canal                       :int            = Field(... , description="channel where transaction occurs",   ge=0)
    agencia_de_origem           :int            = Field(... , description="agency where transaction comes",     ge=0)
    conta_de_origem             :int            = Field(... , description="account where transaction comes",    ge=0)
    agencia_de_destino          :int            = Field(... , description="agency where transaction goes",      ge=0)
    conta_de_destino            :int            = Field(... , description="account where transaction goes",     ge=0)
    suspect                     :bool           = Field(default=False, description="account where transaction goes")