#replace() é um método de string que substitui partes do texto por outra



def cadastrar_usuario():
    print("Bem vindo!")
    print("ao encerrar, digite fim")
    try:
        with open("usuario.txt", 'w') as usuario:
            while True:
                nome =input("Digite o nome do usuário (ou 'fim' para encerrar): ").strip()
                if nome.lower() == "fim":
                    print("encerrando lista")
                    break
                usuario.write(nome +"\n")
        print("Cadastro finalizado.\n")
    except TypeError:
        print("Digite apenas caracteres válidos.")


def listar_usuarios():
    try:
        with open("usuario.txt", 'r') as arquivo:
            print("----Lista de usuarios cadastrados----")
            for nome in arquivo:
                usuario = nome.strip()
                print("Usuário:", usuario)
    except:
        print("Erro ao listar usuarios cadastrados.")


def alterar_usuario():
    try:
        nome_antigo = input("Digite o nome que deseja alterar: ").strip()
        nome_novo = input("Digite o novo nome: ").strip()
        i = 0

        with open("usuario.txt", "r") as arquivo:
            dados = arquivo.readlines() # [felipe, moia, thiago]

        while i < len(dados): # percorre a lista de dados
            nome = dados[i]
            nome_formatado = nome.strip()

            if nome_formatado == nome_antigo:
                dados[i] = nome_novo + '\n'
                print("Nome alterado com sucesso.")
                break
            i+=1
        
        with open("usuario.txt", "w") as arquivo:
                    arquivo.writelines(dados) # escreve as linhas

    except FileNotFoundError:
        print("A merda do arquivo não foi encontrado ou foi escrito errado por mim")

    except IOError as e:
        print("Erro ao alterar o nome")
        print(e)


def excluir_usuario():
    try:
        nome = input("Digite o nome que deseja excluir: ").strip()
        linhas = open("usuario.txt").readlines()

        for i in range(len(linhas)):
            if linhas[i].strip() == nome:
                linhas.pop(i)
                open("usuario.txt", "w").writelines(linhas)
                print("Nome excluído.")
                break
        else:
            print("Nome não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except:
        print("Erro ao excluir.")

# lista.pop() -> remove o ultimo item da lista
# lista.pop(1) -> remove a posição específica
# lista.remove("nome desejado ou registro") -> remove pela descrição.



def menu():
    while True:
        print("=== Menu ===")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Alterar nome de usuário")
        print("4 - Excluir usuário")
        print("5 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número.\n")
            continue

        if opcao == 1:
            cadastrar_usuario()
        elif opcao == 2:
            listar_usuarios()
        elif opcao == 3:
            alterar_usuario()
        elif opcao == 4:
            excluir_usuario()
        elif opcao == 5:
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.\n")


menu()