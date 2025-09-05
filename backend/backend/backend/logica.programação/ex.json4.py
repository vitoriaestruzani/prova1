#eu como dono de concessionária de carros importados, preciso de um sistema para controlar meu estoque de veículos. 
#Para me organizar melhor, além de nome, gostaria de guardar o ano, quilometrragem, marca, preço, cor e quantidade de cada veículo.
#quero um menu onde eu possa cadastra, alterar, excluir e listar meus veículos.
#para me sentir especial, quero o nome da minha loja apareça no topo do menu: MOYA'S IMPORTS.
import json
estoque = []

def carregar_estoque():
    try:
        with open('estoque_veiculos.json', 'r') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salvar_estoque(estoque):
    with open('estoque_veiculos.json', 'w') as arquivo:
        json.dump(estoque, arquivo, indent=4)



def cadastrar_veiculo(estoque):


    try:
        with open('estoque_veiculos.json', 'r') as arquivo:
            estoque = json.load(arquivo)
        print("Estoque carregado com sucesso!")
    except FileNotFoundError:
        print("Arquivo 'estoque_veiculos.json' não encontrado.")
    except json.JSONDecodeError:
        print("Arquivo está vazio ou corrompido.")

    print("\n--- Cadastro de Novo Veículo ---")

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

estoque.append(carro)
print("Veículo adicionado!")

with open('estoque_veiculos.json', 'w') as arquivo:
    json.dump(estoque, arquivo, indent=4)
print("Arquivo 'estoque_veiculos.json' atualizado com sucesso!")


def alterar_veiculo(estoque):
    produto_para_alterar = int(input("Digite o número do veículo para alterar o nome: "))

    i = 0
    for carro in estoque:
        if i == produto_para_alterar:
            novo_nome = input("Digite o novo nome: ")
            carro["nome"] = novo_nome
            print("Nome alterado com sucesso!")
            return  # sai da função depois de alterar
        i += 1

    print("Número inválido, nenhum veículo alterado.")



def excluir_veiculo(estoque):
    nome_para_excluir = input("Digite o nome do veículo para excluir: ").strip().lower()

    novo_estoque = []
    encontrado = False
    for carro in estoque:
        if carro['nome'].lower() != nome_para_excluir:
            novo_estoque.append(carro)
        else:
            encontrado = True

    if encontrado:
        print(f"Veículo excluído com sucesso!")
    else:
        print(f"Veículo não encontrado.")

    return novo_estoque




def listar_veiculos(estoque):
    if estoque:
        print("Sua lista de veículos atual:")
        i = 1
        for carro in estoque:
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




def sistema_moya():
    print("MOYA'S IMPORTS - Os importados que fazem história.")
    estoque = carregar_estoque()

    while True:
        print("\nMenu:")
        print("1 - Cadastrar veículo")
        print("2 - Alterar veículo")
        print("3 - Excluir veículo")
        print("4 - Listar veículos")
        print("Sair")

        opcao = input("Escolha uma opção: ").strip().lower()

        if opcao == "1":
            cadastrar_veiculo(estoque)
        elif opcao == "2":
            alterar_veiculo(estoque)
        elif opcao == "3":
            excluir_veiculo(estoque)
        elif opcao == "4":
            listar_veiculos(estoque)
        elif opcao == "sair":
            print("Obrigado por usar MOYA'S IMPORTS! Até logo.")
            break
        else:
            print("Opção inválida. Tente novamente.")

sistema_moya()