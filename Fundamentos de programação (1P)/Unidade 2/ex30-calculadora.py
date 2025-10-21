def somar(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}\n")

def subtrair(num1, num2):
    print(f"{num1} - {num2} = {num1 - num2}\n")

def multiplicar(num1, num2):
    print(f"{num1} * {num2} = {num1 * num2}\n")

def dividir(num1, num2):
    if num1 >= num2:
        print(f"{num1} / {num2} = {num1 / num2}\n")
    else:
        print(f"{num2} / {num1} = {num2 / num1}\n")
        

while True:
    opcao = int(input("Digite a operação que vc quer fazer: \n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Encerrar\n\n Opção: "))
    if opcao == 1:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        somar(valor1, valor2)

    elif opcao == 2:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        subtrair(valor1, valor2)

    elif opcao == 3:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        multiplicar(valor1, valor2)

    elif opcao == 4:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        dividir(valor1, valor2)

    elif opcao == 5:
        break

    else:
        print("Opçao invalida")