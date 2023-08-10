menu = '''
    Escolha a operação que deseja realizar:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
'''

saldo = 0
LIMITE_CASH = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
saques_realizados = 0

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Quanto deseja depositar?"))
        saldo = saldo + deposito
        extrato += f"Valor depositado de R${deposito}.\n" 
    elif opcao == "s":
        if saldo <= 0:
            print("Desculpe, sue saldo está zerado. Operação cancelada.")
        elif saques_realizados == 3:
            print("Você atingiu o limite de saques diários. Tente a partir de amanhã.")
        else:
            saque = float(input("Informe o valor do saque:"))
            if saque > saldo:
                print("Saldo insuficiente para realizar a operação.")
            elif saque > 500:
                print(f"Seu limite de saque é de R$ {LIMITE_CASH}.")
                print('Por favor, saque um valor menor.')
            else:
                extrato += f"Valor sacado de R${saque}.\n"
                saldo = saldo - saque
                saques_realizados+=1
        
    elif opcao == "e":
        if extrato == "":
            print("Não foram realizadas operações.")
            print(f"Seu saldo é de R${saldo:.2f}")
        else:
            print(extrato)
            print(f"Seu saldo é de R${saldo:.2f}")
    elif opcao == "q":
        break
    else:
        print("Opção inválida. Tente novamente")

