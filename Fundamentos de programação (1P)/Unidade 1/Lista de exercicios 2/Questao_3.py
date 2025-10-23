matriz = [[], [], []]
soma = 0
media = 0
somaDiagonal = 0
for i in range(3):
    for j in range(3):
        if j == 0:
            matriz[i].append(float(input("Digite o salário médio dessa profissão: R$ ")))
        elif j == 1:
            matriz[i].append(int(input("Digite o tempo mínimo de experiência: ")))
        else:
            matriz[i].append(float(input("Digite o valor por hora de trabalho: R$ ")))
          
for i in range(3):
    for j in range(3):
        if j == 0:
            soma += matriz[i][j]
            print(f"| R$ {matriz[i][j]} |", end='\t')
        else:
            print(f"| {matriz[i][j]} |", end='\t')
            
        if i == j:
            somaDiagonal += matriz[i][j]
    print()
    
media = soma/len(matriz[i])
print(f"Média salarial das três profissões: {media:.2f}")
print(f"Soma dos valores da diagonal: {somaDiagonal}")