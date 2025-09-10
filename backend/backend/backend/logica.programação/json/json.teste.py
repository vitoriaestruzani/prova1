import json

# Carregar dados de um arquivo JSON, retornando lista vazia se não existir
def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Salvar lista de dados em arquivo JSON
def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

# Cadastrar nova categoria
def cadastrar_categoria():
    categorias = carregar_dados('categorias.json')
    print("\n--- Cadastrar Nova Categoria ---")
    nome = input("Digite o nome da categoria: ").strip()
    novo_id = len(categorias) + 1
    nova_categoria = {
        "id_categoria": novo_id,
        "nome_categoria": nome
    }
    categorias.append(nova_categoria)
    salvar_dados('categorias.json', categorias)
    print("Categoria cadastrada com sucesso!\n")

# Listar categorias
def listar_categorias():
    categorias = carregar_dados('categorias.json')
    print("\n--- Categorias Cadastradas ---")
    if not categorias:
        print("Nenhuma categoria encontrada.")
    else:
        for categoria in categorias:
            print(f"{categoria['id_categoria']} - {categoria['nome_categoria']}")
    print()

# Cadastrar novo produto
def cadastrar_produto():
    categorias = carregar_dados('categorias.json')
    produtos = carregar_dados('produtos.json')

    if not categorias:
        print("Você precisa cadastrar uma categoria antes de adicionar produtos.\n")
        return

    print("\n--- Cadastrar Novo Produto ---")
    print("Categorias disponíveis:")
    for cat in categorias:
        print(f"{cat['id_categoria']} - {cat['nome_categoria']}")

    while True:
        try:
            id_categoria = int(input("Escolha o ID da categoria: "))
            existe = any(cat['id_categoria'] == id_categoria for cat in categorias)
            if existe:
                break
            else:
                print("Categoria não encontrada. Tente novamente.")
        except ValueError:
            print("Digite um número válido.")

    nome = input("Nome do produto: ").strip()
    
    while True:
        try:
            preco = float(input("Preço do produto (ex: 199.99): "))
            break
        except ValueError:
            print("Digite um preço válido.")

    novo_id = len(produtos) + 1
    novo_produto = {
        "id_produto": novo_id,
        "nome_produto": nome,
        "preco": preco,
        "id_categoria_associada": id_categoria
    }
    produtos.append(novo_produto)
    salvar_dados('produtos.json', produtos)
    print("Produto cadastrado com sucesso!\n")

# Listar produtos com nome da categoria
def listar_produtos():
    produtos = carregar_dados('produtos.json')
    categorias = carregar_dados('categorias.json')

    print("\n--- Lista de Produtos ---")
    if not produtos:
        print("Nenhum produto cadastrado.\n")
        return

    # Criar dicionário para facilitar a busca do nome da categoria pelo id
    cat_dict = {cat['id_categoria']: cat['nome_categoria'] for cat in categorias}

    for produto in produtos:
        nome_categoria = cat_dict.get(produto['id_categoria_associada'], "Categoria não encontrada")
        print(f"ID: {produto['id_produto']} | Nome: {produto['nome_produto']} | Preço: R$ {produto['preco']:.2f}")
        print(f"Categoria: {nome_categoria}\n")

# Menu principal
def sistema_ecommerce():
    print("=== SISTEMA DE GESTÃO DE E-COMMERCE ===")

    while True:
        print("\nMenu:")
        print("1 - Cadastrar Categoria")
        print("2 - Listar Categorias")
        print("3 - Cadastrar Produto")
        print("4 - Listar Produtos")
        print("Sair")

        opcao = input("Escolha uma opção: ").strip().lower()

        if opcao == "1":
            cadastrar_categoria()
        elif opcao == "2":
            listar_categorias()
        elif opcao == "3":
            cadastrar_produto()
        elif opcao == "4":
            listar_produtos()
        elif opcao == "sair":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
sistema_ecommerce()
