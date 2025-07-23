def caixa_eletronico():
    soma = 0  
    valor = 1
    while valor != 0:
        tipo = input("v para somar, f para subtrair: ")
        valor = int(input("Digite um valor (0 para sair): "))

        if tipo == "v":
            soma += valor
        elif tipo == "f":
            soma -= valor
        else:
            print("Opção errada, tente de novo.")

        print("Saldo agora é:", soma)

    print("Saldo final é:", soma)

caixa_eletronico()