#No Python, o try...except é como dizer: “Tenta fazer isso... e se der erro, tudo bem, vamos resolver.” 
#É uma forma de evitar que o programa pare de funcionar quando algo inesperado acontece. 
#Você tenta rodar um trecho de código, e se der problema (tipo o usuário digitar algo errado) o Python pula para o except e segue em frente com uma solução ou uma mensagem de aviso.
#ZeroDivisionError: Ocorre quando se tenta dividir um número por zero. 
#TypeError: Ocorre quando uma operação é realizada com tipos de dados incompatíveis, por exemplo, tentar somar uma string com um número. 
#ValueError: Ocorre quando uma função recebe um argumento com o tipo correto, mas com um valor inválido, por exemplo, converter uma string não numérica em inteiro. 
#NameError: Ocorre quando uma variável não foi definida ou não está no escopo atual. 
#IndexError: Ocorre quando se tenta acessar um elemento de uma sequência (lista, tupla, etc.) com um índice fora dos limites. 
#KeyError: Ocorre quando se tenta acessar um elemento de um dicionário usando uma chave que não existe. 
#FileNotFoundError: Ocorre quando um arquivo não é encontrado. 
#ImportError: Ocorre quando ocorre uma falha ao importar um módulo. 
#AttributeError: Ocorre quando se tenta acessar um atributo que não pertence a um objeto. 
#IOError: Um erro de E/S, como um problema de leitura ou escrita em um arquivo. 
#SyntaxError: Ocorre quando o código possui erros de sintaxe, como erros de digitação ou estrutura incorreta. 
#IndentationError: Ocorre quando há erros de indentação no código Python. 

def gerar_lista():
    print("Bem vindo!")
    print("ao encerrar, digite fim")
    try:
        with open("comida.txt", 'w') as comida:
            while True:
                item =input("Digite o item:")
                if item.lower() == "fim":
                    print("encerrando lista")
                    break
                comida.write(item +"\n")
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    except TypeError:
        print("Digite apenas letras.")


def listar_itens():
    try:
        with open("comida.txt", 'r') as lista:
            print("----lista de compras----")
            for item in lista:
                produto = item.strip()
                print("item:", produto)
    except FileNotFoundError:
        print("Arquivo não encontrado!")
listar_itens()