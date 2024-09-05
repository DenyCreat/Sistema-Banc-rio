menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print('Por favor, selecionar a opção desejada')
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Por favor, Informar o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Falha na operação! O valor informado não é válido.")
    elif opcao == "2":
        valor = float(input("Por favor, informar o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Falha na operação! O seu saldo é insuficiente.")
        elif excedeu_limite:
            print("Falha na operação! O valor do saque está acima do limite.")
        elif excedeu_saques:
            print("Falha na operação! O número de saques atingiu o limite diário.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Falha na operação! Valor informado é inválido.")
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break
    else:
        print("Falha na operação, é necessário selecionar a opção desejadda.")
