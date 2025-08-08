def lista_de_compras():
    nome = input("Olá! Digite seu nome para iniciar: ")
    print("Bem-vindo(a), " + nome + "! Vamos montar sua lista de compras?")
    
    lista = []
    opcao = ""

    while opcao != "Sair" and opcao !="sair":
        print("\nMenu:")
        print("1 - Cadastrar")
        print("2 - Excluir")
        print("3 - Mostrar lista")
        print("Sair")
        
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                produto = input("Digite o nome do produto para adicionar: ").strip().lower()
                lista.append(produto)
                print( produto + " adicionado à lista.")

            case "2":
                produto = input("Digite o nome do produto para excluir: ").strip().lower()
                if produto in lista:
                    lista.remove(produto)
                    print(produto + " removido da lista.")
                else:
                    print(produto + " não está na lista.")
                

            case "3":
                if lista:
                    print("Sua lista de compras atual:", lista)
                else:
                    print("Sua lista está vazia.")

            case "Sair" | "sair":
                print("Até logo," + nome + "!")

            case _:
                print("Opção inválida.")

lista_de_compras()
