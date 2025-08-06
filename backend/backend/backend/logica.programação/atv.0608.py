num1 = int(input("Digite o primeiro valor:"))
num2 = int(input("Digite o segundo valor:"))
operacao = input("Digite a operação (+,-,*,/):")

match operacao: 
    case "+": 
        soma = num1 + num2
        print("Soma:", soma)

    case "/":
        divisao = num1/num2
        print("Divisão:", divisao)

    case "-":
        subtracao = num1-num2
        print("Subtração:", subtracao)

    case "*":
        multiplicacao = num1*num2
        print("Multiplicação:", multiplicacao)

