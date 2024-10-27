# Api de validacao de transacao


## POST /api/customer/{agencia}/{conta}
```json
{
  "agencia": 999999,
  "conta": 99999,
  "nome": "Peterson Pete",
  "idade": 33
}
```
### Retornos Possiveis

201 - Created
422 - BadRequest
409 - Conflict

## POST /api/transaction/create
```json
{
  "id_da_transacao": "",
  "data_e_hora_da_transacao": 1704070800,
  "valor_da_transacao": 0.0,
  "canal": 0,
  "agencia_de_origem": 0,
  "conta_de_origem": 0,
  "agencia_de_destino": 0,
  "conta_de_destino": 0
}
```

### Retornos Possiveis

201 - Created
- Sempre retorna de acordo com regras de suspeita:
{
  "suspect": false
}
422 - BadRequest
409 - Conflict

## GET /api/customer/{agencia}/{conta}

### Retornos Possiveis
- Sempre retorna quando possui um resultado com status 200:
```json
{
  "nome": "",
  "idade": 0,
    "last_transactions": [
      {
        "agencia": 0,
        "conta": 0,
        "type": "debit|credit",
        "valor": 0.0,
        "suspect": false
      }
  ],
  "balance": 0.0
}
```
