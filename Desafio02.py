import textwrap

def menu():
    menu = """\n
    ==========MENU==========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    ==> """

    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de \t\tR${valor:.2f}\n"
        print("\n###--Operação realizada com sucesso.--###")

    else:
        print("\nOperação inválida! Não é possível depositar um valor menor que 0.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação inválida! Saldo insuficiente para saque.")

    elif excedeu_limite:
        print("\nOperação inválida! Valor de saque excede o limite estabelecido.")

    elif excedeu_saques:
        print("\nOperação inválida! A quantidade de saques permitida foi excedida.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque de \t\tR${valor:.2f}\n"
        numero_saques += 1
        print("\n###--Operação realizada com sucesso.--###")

    else:
        print("\nOperação inválida! Valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("===========================================")

def criar_usuario(usuarios):
    cpf = input("Por favor, informe o CPF (somente os números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuários com esse CPF!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd/mm/yyyy): ")
    endereco = input("Informe o endereço completo (logradouro, número, bairro, cidade/UF estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n###--Operação realizada com sucesso. Usuários cadastrado--###")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n###--Operação realizada com sucesso. Conta cadastrada--###")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuários não foi localizado. Criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """

        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe um valor para deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor desejado para o saque: "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
            
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\nOperação inválida! Por favor, selecione novamente a operação desejada.")

main()


