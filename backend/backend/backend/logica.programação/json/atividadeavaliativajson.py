import json

categorias = []
produtos = []
dados = []
id_categoria = 0
id_produto = 0

try:
    with open('categorias.json', 'r') as arquivo:
        categorias = json.load(arquivo)
    print("Categorias carregadas com sucesso!")
except FileNotFoundError:
    print("Arquivo 'categorias.json' não encontrado.")
except json.JSONDecodeError:
    print("O arquivo de categorias existe, mas está vazio ou corrompido.")



def cadastrar_categoria():
    global id_categoria
    global categorias
    try:
        with open('categorias.json', 'r') as arquivo:
            categorias = json.load(arquivo)
        print("Categorias carregadas com sucesso!")
    except FileNotFoundError:
        print("Arquivo 'categorias.json' não encontrado.")
    except json.JSONDecodeError:
        print("O arquivo de categorias existe, mas está vazio ou corrompido.")
      

    print("--- Cadastrar Nova Categoria ---")
    nome = input("Digite o nome da categoria: ").strip()

    nova_categoria = {
        "id": id_categoria,
        "nome": nome
    }

    id_categoria += 1
    categorias.append(nova_categoria)


    try:
        with open('categorias.json', 'w') as arquivo:
            json.dump(categorias, arquivo, indent=4)
        print("Categoria cadastrada com sucesso!")
    except:
        print("Erro ao salvar a categoria.")

    categorias.append(nova_categoria)

def cadastrar_produto():
    global id_categoria
    global id_produto
    global categorias

    try:
        with open('categorias.json', 'r') as arquivo:
            categorias = json.load(arquivo)
        print("Categorias carregadas com sucesso!")
    except FileNotFoundError:
        print("Arquivo 'categorias.json' não encontrado.")
    except json.JSONDecodeError:
        print("O arquivo de categorias existe, mas está vazio ou corrompido.")


    try:
        with open('produtos.json', 'r') as arquivo:
             produtos = json.load(arquivo)
        print("Produtos carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo 'produtos.json' não encontrado.")
    except json.JSONDecodeError:
        print("O arquivo de produtos existe, mas está vazio ou corrompido.")
       
    while True:
        try:
            id_categoria = int(input("Escolha o ID da categoria: "))
            existe = 'id_categoria' == id_categoria
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

    id_produto += 1

    novo_produto = {
        "id_produto": id_produto,
        "nome_produto": nome,
        "preco": preco,
        "id_categoria_associada": id_categoria
    }

    produtos.append(novo_produto)

    try:
        with open('produtos.json', 'w') as arquivo:
            json.dump(produtos, arquivo, indent=4)
        print("Produto cadastrado com sucesso!\n")
    except:
        print("Erro ao salvar o produto.")

def listar_produtos():
    if dados:
        print("Sua lista de produtos:")
        i = 1
        for produto in dados:
            print(i, ". Categoria:", ['categoria'])
            print("   Nome:", ['nome'])
            print("   Preço: R$", ['preco'])
            i += 1
    else:
        print("Seu estoque está vazio.")


###NÃO MEXER MAIS NESSA PORRA
def sistema_ecommerce():
    print("=== SISTEMA DE GESTÃO ===")

    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar nova categoria")
        print("2. Cadastrar novo produto")
        print("3. Listar produtos com nome da categoria")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_categoria()
        elif opcao == '2':
            cadastrar_produto()
        elif opcao == '3':
            listar_produtos()
        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

sistema_ecommerce()