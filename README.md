# transaction-manager

# Consideracoes inicia







Conversa aberta. Uma mensagem lida.

Pular para o conteúdo
Como usar o Gmail com leitores de tela
teste 
1 de 6
Teste Topaz - Vaga Sr Developer Analyst

Renata Nascimento Honorio
Anexos
ter., 22 de out., 14:05 (há 1 dia)
para mim, Italo, Samuel

Willian, tudo bem? 

Conforme falamos, estamos enviando nosso teste para a vaga de Sr Developer Analyst.

Por gentileza, considerar o retorno do teste concluído até 27/10/24.

Aguardo retorno.
				
RENATA HONORIO
Sr Talent Acquisition Analyst
Topaz Brasil
11997630841
topazevolution.com
Instagram @topazevolution	Linkedin /topazevolution	
/topazevolution

  

Importante: As informações deste e-mail são confidenciais. O uso não autorizado é proibido por lei. Por favor, considere o ambiente antes de imprimir.

Important: The information on this e-mail is confidential. Non-authorized use is prohibited by law. Please Consider the Environment Before Printing.

...

[Mensagem cortada]  Exibir toda a mensagem
1 anexo
  •  Anexos verificados pelo Gmail
# Teste - Back End Topaz

# Objetivo
 
Averiguar as capacidades do candidato em desenvolver/manter um projeto em python usando flask e sqlalchemy/mongo usando containers. O importante não é o desenvolvimento completo de todo o escopo, e sim a execução e estratégia em pontos chaves, como:
 
- Queries de banco de dados complexas
- Organização de Código
- Exemplos de testes unitários/integração
- Documentação
- Observabilidade
 
# Projeto a ser construído para averiguar conhecimento
 
O candidato deve criar um projeto usando flask ou fastapi em python que irá analisar comportamentos de transações financeiras e determinar se é conhecida ou não de acordo com um conjunto de regras pré-definidas.
 
Considerando que uma transação contenha as seguintes informações:
- id da transação - str
- data e hora da transação - timestamp
- valor da transação - Decimal
- canal - enum (ATM, Teller, Internet Banking ou Mobile Banking)
- agência de origem - int
- conta de origem - int
- agência de destino - int
- conta de destino - int

E que cada agência e origem possa ter um cadastro em um banco não relacionado com os campos:
- agência
- conta
- nome
- idade
 
## Regras pré-definidas para considerar uma transação suspeita
- Horário incompatível com o canal
	- transação com um teller (caixa) antes das 10:00 e após as 16:00
	- Valor alto em ATM de madrugada
	- Múltiplas transações iguais via IBK ou MBK
- Transações repetidas em espaço curto de tempo com valores próximos
- Transações com valores altos para destinos não muito frequentes
- Transações incomuns de usuários da terceira idade em canais digitais
 
# Endpoint esperado para a aplicação
 
## PUT /api/customer/{agencia}/{conta}
```json
{
  "agencia": 0,
  "conta": 0,
  "nome": "",
  "idade": 0
}
```
Retornos esperados
- 201 - Created - Caso de criação bem sucedida
- 400 - BadRequest - Caso falte alguma chave ou a chave tenha o tipo inválido
- 409 - Conflict - Caso já tenha cadastro
 
## PUT /api/transaction/create
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
 
Retornos esperados:
- 201 - Created - Caso de criação bem sucedida
```json
{
  "suspect": false
}
```
- 400 - BadRequest - Caso falte alguma chave ou a chave tenha o tipo inválido
 
## GET /api/customer/{agencia}/{conta}
Retornos esperados:
- 200
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
      "nome": "",
      "idade": "",
      "suspect": false
    }
  ],
  "balance": 0.0
}
```
 
Onde:
- "last_transactions" retornar somente as 5 últimas transações
- "suspect" informa se a transação em questão bateu em algumas das regras pré definidas
- "type" é débito ou crédito dependente se a transação tem a agencia/conta enviada na requisição está como origem ou destino
- "balance" é o resultado da soma de todos os créditos com a subtração de todos os débitos
 
- 404 - NotFound - Caso não exista cadastro
 

# Entrega
 
Subir o projeto em um servidor git de sua preferência, pode ser projeto aberto ou privado, na escolha de
subir um projeto privado, informar qual serviço será utilizado para fornecermos um usuário para obter
acesso.
 
# Conclusão
 
O objetivo é avaliar a qualidade da entrega com base no escopo, e tambem discutir temas como:
- Como o código foi organizado
- Organização dos testes
- Qual a stack escolhida (obrigatório uso de python, porém fica a sua escolha quais bancos de dados)
- Otimização de queries
Teste - Back End - Topaz (1).md
Exibindo Teste - Back End - Topaz (1).md.