#Sistema utilizado para processamento de pagamentos

#constantes necessárias
LIMITE_DIARIO = 3
LIMITE_VALOR_SAQUE = 500.00
historico_movimentacoes = []
numero_saques_diarios = 0
dinheiro_depositado = 3000.00
valor_saque = 0
lista_usuarios = []
contas_correntes = []

def criar_usuario (nome = None, data_nascimento = None, cpf = None, logradouro = None, numero = None, bairro = None, cidade = None, estado = None):
    return {"nome": nome, 
        "data_nascimento": data_nascimento,
        "cpf" : cpf,
        "endereco": {
            "logradouro": logradouro,
            "numero": numero,
            "bairro": bairro,
            "cidade/sigla": cidade,
            "estado" : estado
        }
    }

def criar_usuário_inputs () :
    return criar_usuario(
            nome = input("Qual é o seu nome?").strip(),
            data_nascimento = input("Qual a sua data de nascimento? (dd-mm-aaaa)").strip(),
            cpf = input("Qual o seu CPF? (apenas números)").strip(),
            logradouro = input("Qual o seu logradouro?").strip(),
            numero = input("Qual o número da sua residência?").strip(),
            bairro = input("Qual o seu bairro?").strip(),
            cidade = input("Qual a sua cidade?").strip(),
            estado = input("Qual o seu estado? (sigla)").strip()
        )

def criar_conta_corrente(numero_de_conta = None, usuario = None):
    return {
        "agencia" : "0001",
        "numero_da_conta" : numero_de_conta,
        "usuário": usuario
    }

def sacar(*, saldo, valor, extrato, limite, numero_saques):
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato, numero_saques

    if numero_saques < limite:
        if valor <= LIMITE_VALOR_SAQUE:
            if valor <= saldo:
                saldo -= valor
                numero_saques += 1
                extrato.append(f"Saque do usuário: R$ {valor:.2f} - Atual valor depositado: R$ {saldo:.2f}")
                print(f"Sucesso em sacar o valor de R${valor:.2f} - Saldo restante: R$ {saldo:.2f}")
            else:
                print("Saldo insuficiente!")
        else:
            print(f"Este valor é maior que R$ {LIMITE_VALOR_SAQUE:.2f}")
    else:
        print("Usuário já atingiu o limite diário! Por favor volte mais tarde!")
    return saldo, extrato, numero_saques

def depositar (saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Deposito do usuário: R$ {valor:.2f} - Atual valor depositado: R$ {saldo:.2f}")
        print(f"Sucesso ao depositar R$ {valor:.2f} em sua conta - Saldo : R$ {saldo:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def exibir_extrato (saldo, /, extrato) :
    texto = "Historico de movimentação do usuário \n"
    if not extrato:
        texto += "Não foram realizadas movimentações."
    else:
        for transacao in extrato:
            texto += transacao + "\n"
    print(texto)
    print(f"\nSaldo atual:\t\tR$ {saldo:.2f}")


while True:
    menu = """
        _______________________________________
            Bem-vindo ao Sistema Bancario
        _______________________________________
            1 - Depositar

            2 - Sacar

            3 - Exibir extrato

            4 - Criar Usuário

            5 - Criar Conta Corrente

            0 - Sair
        _______________________________________
        """    
    
    print(menu)
    opcao = input("Digite a opção desejada: ").strip()

    if opcao == "1":
        try:
            valor = float(input("Informe o valor do depósito: "))
            dinheiro_depositado, historico_movimentacoes = depositar(dinheiro_depositado, valor, historico_movimentacoes)
        except ValueError:
            print("Valor inválido! Por favor, digite apenas números (use ponto para centavos).")

    elif opcao == "2":
        try:
            valor = float(input("Informe o valor do saque: "))
            dinheiro_depositado, historico_movimentacoes, numero_saques_diarios = sacar(saldo=dinheiro_depositado, valor=valor, extrato=historico_movimentacoes, limite=LIMITE_DIARIO, numero_saques=numero_saques_diarios)
            print (f"O atual valor da conta depositada é: R${dinheiro_depositado:.2f}")
        except ValueError:
            print("Valor inválido! Por favor, digite apenas números (use ponto para centavos).")

    elif opcao == "3":
        exibir_extrato(dinheiro_depositado, extrato= historico_movimentacoes)
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == "4":
        novo_usuario = criar_usuário_inputs()
        usuario_existente = [usuario for usuario in lista_usuarios if usuario["cpf"] == novo_usuario["cpf"]]
        if usuario_existente:
            print("\nErro: Já existe um usuário com esse CPF!")
        else:
            lista_usuarios.append(novo_usuario)
            print("Usuário criado com sucesso!")

    elif opcao == "5":
        resposta = input("Já possui uma conta? (S/N)")
        if resposta.upper() == "S":
            cpf_usuario = input("Informe o CPF do usuário: ")
            usuario_encontrado = False
            for usuario in lista_usuarios:
                if usuario["cpf"] == cpf_usuario:
                    contas_correntes.append(criar_conta_corrente(numero_de_conta=len(contas_correntes) + 1, usuario=usuario))
                    usuario_encontrado = True
                    print("Conta corrente criada com sucesso!")
                    break
            if not usuario_encontrado:
                print("Usuário não encontrado com o CPF informado.")
        else:
            novo_usuario = criar_usuário_inputs()
            usuario_existente = [usuario for usuario in lista_usuarios if usuario["cpf"] == novo_usuario["cpf"]]
            if usuario_existente:
                print("\nErro: Já existe um usuário com esse CPF!")
            else:
                lista_usuarios.append(novo_usuario)
                contas_correntes.append(criar_conta_corrente(numero_de_conta = len(contas_correntes) + 1, usuario = novo_usuario))
                print("Conta corrente criada com sucesso!")

    elif opcao == "0":
        print("Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    
