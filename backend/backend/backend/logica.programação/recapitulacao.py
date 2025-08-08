def caixa_eletronico():
    nome = input("Digite seu nome para cadastrar a conta: ")
    saldo = 0.00
    print("Bem-vindo(a), " + nome + "! Seu saldo atual é: R$ ", saldo)
    
    opcao = ""

    while opcao != "Sair":
        print("\nMenu:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver Saldo")
        print("Sair")
        
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                valor = float(input("Valor para depositar: R$ "))
                saldo += valor
                print("Depósito realizado.")

            case "2":
                valor = float(input("Valor para sacar: R$ "))
                if valor <= saldo:
                    saldo -= valor
                    print("Saque realizado.")
                else:
                    print("Saldo insuficiente.")

            case "3":
                print("Saldo atual: R$", saldo)

            case "Sair":
                print("Até logo," + nome + "!")

            case _:
                print("Opção inválida.")


                
caixa_eletronico()
