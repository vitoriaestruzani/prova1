#não mexer \
import json

categorias = []
produtos = []
dados = []
try:
    with open('categorias.json', 'r') as arquivo:
        categorias = json.load(arquivo)
    print("Categorias carregadas com sucesso!")

except FileNotFoundError:
    print("Arquivo 'categorias.json' não encontrado.")

except json.JSONDecodeError:
    print("O arquivo de categorias existe, mas está vazio ou corrompido.")


def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

#não mexer \
    
def salvar_dados(dados):
    with open(categorias.json, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

#não mexer \
        
def cadastrar_categoria():
    categorias = carregar_dados('categorias.json')
    print("\n--- Cadastro de Nova Categoria ---")
    id_categoria = input("ID da categoria: ")
    nome_categoria = input("Nome da categoria: ")

    nova_categoria = {
        "id_categoria": id_categoria,
        "nome_categoria": nome_categoria
    }

    categorias.append(nova_categoria)
    salvar_dados('categorias.json', categorias)
    print("Categoria salva com sucesso!")
        
###################################################################
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


def listar_produtos():
    if dados:
        print("Sua lista de produtos:")
        i = 1
        for produto in dados:
            print(i, ". Nome:", carro['nome'])
            print("   Ano:", carro['ano'])
            print("   KM:", carro['km'])
            print("   Marca:", carro['marca'])
            print("   Preço: R$", carro['preco'])
            print("   Cor:", carro['cor'])
            print("   Quantidade:", carro['quantidade'])
            print("")
            i += 1
    else:
        print("Seu estoque está vazio.")
    
nome = input("Nome: ")
    
while True:
    try:
        preco = float(input("Digite o preço do produto (ex: 199.99): "))
        break
    except ValueError:
        print("Erro: Por favor, digite um número válido para o preço.")

while True:
    try:
        ano = int(input("Digite o ano: "))
        break 
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido para o ano.")

while True:
    try:
        quilometragem = int(input("Digite a quilometragem: "))
        break 
    except ValueError:
        print("Erro: Por favor, digite um número válido.")


marca = input("Marca:")
cor = input("Cor:")

while True:
    try:
        quantidade = int(input("Digite a quantidade em estoque: "))
        break 
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido para a quantidade.")

carro = {
    "nome": nome,
    "ano": ano,
    "km": quilometragem,
    "marca": marca,
    "preco": preco,
    "cor": cor,
    "quantidade": quantidade
}

dados.append(carro)
print("Veículo adicionado!")

with open('estoque_veiculos.json', 'w') as arquivo:
    json.dump(dados, arquivo, indent=4)
print("Arquivo 'estoque_veiculos.json' atualizado com sucesso!")


###NÃO MEXER MAIS NESSA PORRA

def menu():

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

menu()