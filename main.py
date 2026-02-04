#Sitema utilizado para processamento de pagamentos

#constantes necessárias
LIMITE_DIARIO = 3
historico_movimentacoes = []
limite_usuario = 0
dinheiro_depositado = 3000.00



def Sacar (valor):
    global dinheiro_depositado, limite_usuario
    if limite_usuario < LIMITE_DIARIO:
        if valor <= 500:
            if valor <= dinheiro_depositado:
                dinheiro_depositado -= valor
                limite_usuario += 1
                historico_movimentacoes.append(f"Saque do usuário: R$ {valor:.2f} - Atual valor depositado: R$ {dinheiro_depositado:.2f}")
                print(f"Sucesso em sacar R$ {valor:.2f}")
            else:
                print("Saldo insuficiente!")
        else:
            print("Este valor é maior que R$ 500,00!")
    else:
        print("Usuário já atingiu o limite diário! Por favor volte mais tarde!")

def depositar (valor):
    global dinheiro_depositado
    dinheiro_depositado += valor
    historico_movimentacoes.append(f"Deposito do usuário: R$ {valor:.2f} - Atual valor depositado: R$ {dinheiro_depositado:.2f}")
    print(f"Sucesso, valor depositado de R${valor:.2f}")

def consultar_saldo():
    print(f"O valor do usuário é de R$ {dinheiro_depositado:.2f}")

def exibir_extrato () :
    texto = "Historico de movimentação do usuário \n"
    if not historico_movimentacoes:
        texto += "Não foram realizadas movimentações."
    else:
        for transacao in historico_movimentacoes:
            texto += transacao + "\n"
    print(texto)


while True:
    menu = """
        _______________________________________
            Bem-vindo ao Sistema Bancario
        _______________________________________
            1 - Depositar

            2 - Sacar

            3 - Consultar Saldo

            4 - Exibir extrato

            0 - Sair
        _______________________________________
        """    
    
    print(menu)
    opcao = input("Digite a opção desejada: ").strip()

    if opcao == "1":
        try:
            valor = float(input("Informe o valor do depósito: "))
            depositar(valor)
        except ValueError:
            print("Valor inválido! Por favor, digite apenas números (use ponto para centavos).")

    elif opcao == "2":
        try:
            valor = float(input("Informe o valor do saque: "))
            Sacar(valor)
        except ValueError:
            print("Valor inválido! Por favor, digite apenas números (use ponto para centavos).")

    elif opcao == "3":
        consultar_saldo()

    elif opcao == "4":
        exibir_extrato()
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == "0":
        print("Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    
