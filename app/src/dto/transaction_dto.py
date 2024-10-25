from typing     import Optional
from pydantic   import BaseModel, Field
from datetime import datetime

class TransactionPost(BaseModel):
    id_da_transacao             :str            = Field(... , min_length=1, max_length=100, description="transaction unique id")
    data_e_hora_da_transacao    :datetime       = Field(... , description="transaction timestamp")
    valor_da_transacao          :float          = Field(... , ge=0, description="transaction amount")
    canal                       :int            = Field(... , ge=0, description="channel where transaction occurs")
    agencia_de_origem           :int            = Field(... , ge=0, description="agency where transaction comes")
    conta_de_origem             :int            = Field(... , ge=0, description="account where transaction comes")
    agencia_de_destino          :int            = Field(... , ge=0, description="agency where transaction goes")
    conta_de_destino            :int            = Field(... , ge=0, description="account where transaction goes")
