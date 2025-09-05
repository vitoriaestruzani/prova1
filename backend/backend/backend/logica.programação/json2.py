import json

livros = []

try:
    with open('biblioteca.json', 'r') as arquivo:
        livros = json.load(arquivo)
    print("Livros carregados com sucesso!")

except FileNotFoundError:
    print("Arquivo 'biblioteca.json' não encontrado.")

except json.JSONDecodeError:
    print("O arquivo existe, mas está vazio ou corrompido.")

print("\n--- Cadastro de Novo Livro ---")
titulo = input("Título: ")
autor = input("Autor: ")
editora = input("Editora: ")
genero = input("Gênero: ")
idioma = input("Idioma: ")

try:
    ano = int(input("Ano de publicação: "))
    paginas = int(input("Número de páginas: "))
except ValueError:
    print("Dados numéricos inválidos. O livro não será salvo.")
    exit()

livro = {
    "titulo": titulo,
    "autor": autor,
    "editora": editora,
    "ano_publicacao": ano,
    "genero": genero,
    "numero_paginas": paginas,
    "idioma": idioma
}

livros.append(livro)
print("Livro adicionado!")

with open('biblioteca.json', 'w') as arquivo:
    json.dump(livros, arquivo, indent=4)
    print("Arquivo 'biblioteca.json' atualizado com sucesso!")

