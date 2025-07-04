
# Desafio de Projeto DIO - Criando um Sistema Bancário com Python

Este projeto trata-se da resolução do desafio do curso Santander 2025 - Back-End com Python com a DIO. Utilizando dos princípios de desenvolvimento com Python, praticando os conhecimentos adquiridos sobre Operadores e Manipulação de String.  


## Objetivo Geral

Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.
Como primeira versão do projeto vamos considerar que há apenas um usuário e que as operações são realizadas em um mesmo dia. 

## Requisitos das Operações

### Depósito:
Deve ser possível depositar valores positivos.
Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

### Saque:
O sistema deve permitir realizar até 03 saques diários com limite máximo de R$ 500,00 por saque.
Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possívelsacar o dinheiro por falta de saldo.
Todos os saques devem ser armazenados em uma variável e exibidos n operação extrato.

### Extrato:
Esta operação deve listar todas movimentações realizadas na conta.
No fim da listagem deve er exibido o saldo atual.
Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ter o formato R$ xx.xx
