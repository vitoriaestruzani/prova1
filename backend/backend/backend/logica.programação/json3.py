
import json
inventario = []
novo_inventario = []

with open("biblioteca.json", 'r') as biblioteca:
    inventario = json.load(biblioteca)

produto_para_alterar = int(input("Digite o ID do produto para alterar o nome: "))
livro_para_excluir = int(input("Digite o ID do produto para excluir: "))


for livro in inventario:
    if produto_para_alterar == livro["id"]:
        novo_nome = input("Digite o novo nome: ")
        livro["nome"] = novo_nome

    if livro["id"] != livro_para_excluir:
        novo_inventario.append(livro)

with open("biblioteca.json", 'w') as biblioteca:
    json.dump(novo_inventario, biblioteca, indent=4) 
