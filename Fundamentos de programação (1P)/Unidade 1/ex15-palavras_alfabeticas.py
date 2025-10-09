#guardar palavras em um array/lista e imprimir palavras em ordem alfabetica
palavras =[]
for i in range (5):
    palavra = input("Digite uma palavra: ")
    palavras.append(palavra)
    
palavras.sort()
for i in palavras:
    print(i)