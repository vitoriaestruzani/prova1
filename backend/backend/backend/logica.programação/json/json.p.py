def cadastrar_produto():
    produtos = carregar_dados('produtos.json')
    categorias = carregar_dados('categorias.json')

    if not categorias:
        print("Nenhuma categoria encontrada. Cadastre uma categoria primeiro.")
        return

    print("\n--- Cadastro de Novo Produto ---")
    nome = input("Nome do produto: ")

    while True:
        try:
            preco = float(input("Preço do produto: "))
            break
        except ValueError:
            print("Erro: Digite um número válido para o preço.")

    print("\nCategorias disponíveis:")
    for cat in categorias:
        print(f"{cat['id_categoria']}: {cat['nome_categoria']}")

    id_categoria_associada = input("Digite o ID da categoria do produto: ")

    # Verifica se a categoria existe
    categoria_valida = any(cat['id_categoria'] == id_categoria_associada for cat in categorias)
    if not categoria_valida:
        print("Erro: ID da categoria não encontrado. Produto não será cadastrado.")
        return

    novo_produto = {
        "nome": nome,
        "preco": preco,
        "id_categoria_associada": id_categoria_associada
    }

    produtos.append(novo_produto)
    salvar_dados('produtos.json', produtos)
    print("Produto salvo com sucesso!")
