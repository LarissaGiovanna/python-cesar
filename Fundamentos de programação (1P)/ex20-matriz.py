matriz = [[], [], []] #matriz com 3 linhas

for linha in range (3):
    for coluna in range (3):
        matriz[linha].append(int(input("Digite um número: ")))

somaImpar = 0

for linha in range(3):
    for coluna in range(3):
        print(matriz[linha][coluna], end=' ')
        if matriz[linha][coluna] % 2 != 0:
            impar = matriz[linha][coluna]
            somaImpar = somaImpar + impar
    print()
print(somaImpar)