def cadastrar_produto(lista):
    produto = input("Digite o nome do produto para adicionar: ").strip().lower()
    if produto not in lista:
        lista.append(produto)
        print(produto + " adicionado à lista.")
    else:
        print(produto + " já está na lista.")

def excluir_produto(lista):
    produto = input("Digite o nome do produto para excluir: ").strip().lower()
    if produto in lista:
        lista.remove(produto)
        print(produto + " removido da lista.")
    else:
        print(produto + " não está na lista.")

def mostrar_lista(lista):
    if lista:
        print("Sua lista de compras atual:")
        for item in lista:
            print("- " + item)
    else:
        print("Sua lista está vazia.")

def lista_de_compras():
    nome = input("Olá! Digite seu nome para iniciar: ").strip()
    print("Bem-vindo(a), " + nome + "! Vamos montar sua lista de compras?")
    
    lista = []
    opcao = ""

    while opcao != "Sair" and opcao !="sair":
        print("\nMenu:")
        print("1 - Cadastrar")
        print("2 - Excluir")
        print("3 - Mostrar lista")
        print("Sair")

        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                cadastrar_produto(lista)
            case "2":
                excluir_produto(lista)
            case "3":
                mostrar_lista(lista)
            case "Sair" | "sair":
                print("Até logo," + nome + "!")
                break
            case _:
                print("Opção inválida. Tente novamente.")

lista_de_compras()
