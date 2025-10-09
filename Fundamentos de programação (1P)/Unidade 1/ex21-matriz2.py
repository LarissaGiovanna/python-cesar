matriz = [[], [], []]
produtoDiagonal = 1
soma = 0
media = 0
maior = 0
menorQaMedia = []

for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f"Digite um valor para a posição [ {i} ][ {j} ]: ")))
        
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]}]", end=' ')
        
        #multiplicar produtos da diagonais
        if j == i:
            produtoDiagonal = produtoDiagonal * matriz[i][j]
        
        #soma e media dos valores da matriz
        soma = soma + matriz[i][j]
        
        #maior valor da segunda coluna
        if j == 1:
            if matriz[i][j] > maior:
                maior = matriz[i][j]
    print()    
    
media = soma/(len(matriz[i])*len(matriz[j]))
for i in range(3):
    for j in range(3):
        #valores menores ou iguais a media
        if matriz[i][j] <= media:
            menorQaMedia.append(matriz[i][j])
            
print(f"Produto da diagonal: {produtoDiagonal}")
print(f"Media: {media}")
print(f"Maior: {maior}")
print(f"Valores maiores ou iguais a media: {menorQaMedia}")