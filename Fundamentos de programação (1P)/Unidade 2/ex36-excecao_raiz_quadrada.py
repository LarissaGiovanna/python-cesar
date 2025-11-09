while True:
    try:
        num = int(input("Digite um número: "))
        raiz = num**(1/2)
        print(raiz)
        break
    except ValueError:
        print("Insira só números inteiros.")
    except EOFError:
        print("Não encerre o programa. Insira só números inteiros")
