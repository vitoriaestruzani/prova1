def repetir_nome():
    nome = input("Digite seu nome: ")
    numero = int(input("Digite o número de repetições: "))
    
    for _ in range(numero):
        print(nome)

repetir_nome()
