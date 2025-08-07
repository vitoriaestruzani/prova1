def lista_alunos():
    print("Liste o nome dos alunos:")
    print("ao finalizar, digite encerrar")
    with open("terceirao.txt", 'w') as terceirao:
        while True:
            item =input("Digite o nome do aluno:")
            if item.lower() == "encerrar":
                print("fim da lista")
                break
            terceirao.write(item +"\n")
lista_alunos()