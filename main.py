def menu_inicial():
    menu_inicial = """

    ====== MENU ======
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Nova Conta
        [5] Listar Contas
        [6] Novo Usuário
        [0] Sair
    ==================
    """
    return input(menu_inicial)

def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor do depósito deve ser positivo.")

    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, limite, n_saque, l_saques):
    if valor_saque > saldo:
        print("Operação falhou! Saldo insuficiente.")
      
    elif valor_saque > limite:
        print("Operação falhou! O valor excede o limite de R$ 500,00 por saque.")

    elif n_saque >= l_saques:
        print("Operação falhou! Limite diário de 3 saques atingido.")
        
    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        n_saque += 1
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente os número):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Usuário com CPF já cadastrado!")
        return
    
    nome = input("Informe o nome completo:")
    data_nascimento = input("Informe a data de nacscimento (dd-mm-aaaa):")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado):")
    usuarios.append({"nome": nome,"data_nascimento": data_nascimento,"cpf": cpf,"endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)



def main():
    L_SAQUE = 3
    AGENCIA = "0001"

    saldo  = 0
    limite = 500 #Valor limite por saque em R$ 
    extrato = ""
    n_saque = 0 #Numero de saque realizado
    usuarios = []
    contas = []

    while True:
        opcao = menu_inicial()


        if opcao == "1": # Depositar
            valor_deposito = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == "2": # Sacar
            valor_saque = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo, valor_saque=valor_saque, extrato=extrato, limite=limite,n_saque=n_saque,l_saque=L_SAQUE,)

        elif opcao == "3": # Extrato
            exibir_extrato(saldo, extrato=extrato)4

        elif opcao == "4":# Nova conta
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
            
        elif opcao == "5":# Listar contas
            listar_contas(contas)

        elif opcao == "6":# Criar usuário
            criar_usuario(usuarios)

        elif opcao == "0": # Sair
            print("Saindo...")
            break

        else:
            print("Opção Inválida, tente novamente...")

main()
