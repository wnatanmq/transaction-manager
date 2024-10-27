from typing import Self
from pydantic                   import BaseModel, Field, model_validator
from datetime                   import datetime
from decimal                    import Decimal
from app.src.enum.channel       import Channel


class TransactionModel(BaseModel):
    id:                 str         = Field(..., alias="id_da_transacao",           description="ID da transação"           )    
    amount:             Decimal     = Field(..., alias="valor_da_transacao",        description="Valor da transação"        )    
    timestamp:          datetime    = Field(..., alias="data_e_hora_da_transacao",  description="Data e hora da transação"  )
    channel:            Channel     = Field(..., alias="canal",                     description="Canal da transação"        )
    sender_agency:      int         = Field(..., alias="agencia_de_origem",         description="Agência de origem",   ge=1 )
    sender_account:     int         = Field(..., alias="conta_de_origem",           description="Conta de origem",     ge=1 )
    receiver_agency:    int         = Field(..., alias="agencia_de_destino",        description="Agência de destino",  ge=1 )
    receiver_account:   int         = Field(..., alias="conta_de_destino",          description="Conta de destino",    ge=1 )
    suspect:            int         = Field(default=False,                          description="indicio de suspeita")
