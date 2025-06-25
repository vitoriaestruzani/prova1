def contar_ate_dez():
    for numero in range(1, 11):
        print(numero)

# contar_ate_dez()

def soma_valores():
    soma = 0
    valor = 1

    while valor != 0:
        valor = int(input("Digite um valor:"))
        soma += valor
        print("Valor total da soma", soma)

    print("O total da soma foi:", soma)

# soma_valores()

def senha_correta():
    senha = ""

    while senha != "Vitoria":
        senha = input("Digite sua senha:")
        print("Senha Incorreta")

    print("Bem vindo!")

senha_correta()