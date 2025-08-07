def gerar_lista():
    print("Bem vindo!")
    print("ao encerrar, digite fim")
    with open("comida.txt", 'w') as comida:
        while True:
            item =input("Digite o item:")
            if item.lower() == "fim":
                print("encerrando lista")
                break
            comida.write(item +"\n")


def listar_itens():
    with open("comida.txt", 'r') as lista:
        print("----lista de compras----")
        for item in lista:
            produto = item.strip()
            print("item:", produto)
listar_itens()

