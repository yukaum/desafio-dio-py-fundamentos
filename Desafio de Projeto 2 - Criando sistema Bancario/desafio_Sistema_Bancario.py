menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao =="d":
        deposito = float(input("Insira o valor do depósito: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f} \n"
        
        else:
            print("Erro ao processar a operação. Valor de depósito inválido.")

    elif opcao =="s":
        saque = float(input("Insira o valor do saque: "))

        if numero_saques >= 3:
            print("Erro ao processar a operação. Limite de saques excedido.")

        elif saque > 500:
            print("Erro ao processar a operação. Valor de saque excede o limite.")

        elif saque > saldo:
            print("Erro ao processar a operação. Não há saldo suficiente.")
            
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f} \n"
            numero_saques += 1
            
        else:
            print("Erro ao processar a operação. Valor de saque inválido.")


    elif opcao == "e":
        print("================= \nEXTRATO\n=================")
        
        if extrato == "":
            print("\nNão foram realizadas movimentações. \n\n=================")
        
        else:
            print(f"""
{extrato}
=================            
Saldo: RS {saldo:.2f}
=================
""")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


