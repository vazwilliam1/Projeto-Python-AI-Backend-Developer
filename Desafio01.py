menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

        deposito = float(input("Informe um valor para deposito: "))

        if deposito < 0:
            print("Não é possível depositar um valor menor que 0.")
        else:
            saldo += deposito
            extrato += f"Depósito de R${deposito:.2f}\n"
            print("Operação realizada com sucesso.")
            
    elif opcao == "s":
        print("Saque")

        valor_saque = float(input("Informe o valor desejado para o saque: "))

        if valor_saque > saldo:
            print("Operação inválida! Saldo insuficiente para saque.")
        
        elif valor_saque > limite:
            print("Operação inválida! Valor de saque excede o limite estabelecido.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação inválida! A quantidade de saques permitida foi excedida.")
        
        elif valor_saque >= 0:
            saldo -= valor_saque
            extrato += f"Saque de R${valor_saque:.2f}\n"
            numero_saques += 1
            print("Operação realizada com sucesso.")
        
        else:
            print("Operação inválida! Valor informado é inválido.")
    
    elif opcao == "e":
        print("Extrato")

        print("\n===============EXTRATO===============")
        print("Não houve nenhuma movimentação no período." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("=======================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida! Por favor, selecione novamente a operação desejada.")
        