matriz = [[], [], []] #matriz com 3 linhas
somaImpar = 0
somaColuna = 0

#atribuir valores em cada posição da matriz
for linha in range (3):
    for coluna in range (3):
        matriz[linha].append(int(input("Digite um número: ")))

for linha in range(3):
    for coluna in range(3):
        print(matriz[linha][coluna], end=' ') #printar matriz
        
        #somar valores impares
        if matriz[linha][coluna] % 2 != 0:
            impar = matriz[linha][coluna]
            somaImpar = somaImpar + impar
        
        #soma dos valores da primeira coluna    
        if coluna == 0:
            somaColuna = somaColuna+matriz[linha][coluna]
    print()
print(somaImpar)