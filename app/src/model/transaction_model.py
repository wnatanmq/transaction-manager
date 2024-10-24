from pydantic   import BaseModel, Field
from datetime   import datetime
from decimal    import Decimal
from enum       import Enum

# Definindo o enum para o canal de transação
class Channel(str, Enum):
    ATM = 'ATM'
    TELLER = 'Teller'
    INTERNET_BANKING = 'Internet Banking'
    MOBILE_BANKING = 'Mobile Banking'

# Definindo o modelo para a transação
class Transaction(BaseModel):
    amount:             Decimal     = Field(..., description="Valor da transação"       )    
    transaction_id:     str         = Field(..., description="ID da transação"          )
    timestamp:          datetime    = Field(..., description="Data e hora da transação" )
    channel:            Channel     = Field(..., description="Canal da transação"       )
    origin_agency:      int         = Field(..., description="Agência de origem",   ge=1)
    origin_account:     int         = Field(..., description="Conta de origem",     ge=1)
    destination_agency: int         = Field(..., description="Agência de destino",  ge=1)
    destination_account:int         = Field(..., description="Conta de destino",    ge=1)
