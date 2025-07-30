#exercício 5: Soma de números até que o usuário digite 0
soma = 0

while True:
    valor = int(input("Digite um número (0 para parar): "))
    if valor == 0:
        break
    soma += valor

print(f"Soma total: {soma}")
