situacao = int(input("Digite sua nota:"))

match situacao:
    case 10:
        situacao = "Parabéns! Nota máxima. Aprovado"
        print("Sua situação é:", situacao)

    case 7|8|9:
        situacao = "Aprovado"
        print("Sua situação é:", situacao)

    case 0|1|2|3|4|5|6:
        situacao = "Reprovado"
        print("Sua situação é:", situacao)

    case _:
        print("Nota inválida.")