#exercicio 8: Encontrar o maior número em uma lista
numeros = [10, 5, 20, 8, 15]
maior = numeros[0]

for num in numeros:
    if num > maior:
        maior = num

print(f"O maior número da lista é: {maior}")
