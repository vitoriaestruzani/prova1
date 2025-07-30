#exercício 6: Adivinhar um número secreto
secreto = 5

while True:
    palpite = int(input("Tente adivinhar o número secreto: "))

    if palpite > secreto:
        print("Muito alto.")
    elif palpite < secreto:
        print("Muito baixo.")
    else:
        print("Parabéns, você acertou!")
        break
