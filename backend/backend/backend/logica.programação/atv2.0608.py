idade = int(input("Digite sua idade: "))

match idade:
    case x if x < 12:
        fasedavida = "criança"
        print("Sua fase da vida é:", fasedavida)

    case x if x >=12  and x < 18:
        fasedavida = "adolescente"
        print("Sua fase da vida é:", fasedavida)

    case x if x >= 18 and x < 60:
        fasedavida = "adulto"
        print("Sua fase da vida é:", fasedavida)

    case x if x >= 60 and x < 100:
        fasedavida = "adulto"
        print("Sua fase da vida é:", fasedavida)

    case x if x >=100:
        fasedavida = "mumia"
        print("Sua fase da vida é:", fasedavida)

