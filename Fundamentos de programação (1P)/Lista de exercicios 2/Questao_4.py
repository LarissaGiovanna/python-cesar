numColuna = int(input("Digite o número da coluna: "))
operacao = input("Digite uma letra para a operação: ")

matriz = [[], [], []]
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input("Digite um número: ")))
        
soma = 0
produto = 1
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]}]", end=' ')
        
        if j == numColuna:
            if operacao.upper() == 'S':
                soma += matriz[i][j]
            elif operacao.upper() == 'P':
                produto *= matriz[i][j]
    print()
    
if operacao.upper() == 'S':
        print(f"Resultado da Soma da coluna {numColuna}: {soma}")
elif operacao.upper() == 'P':
        print(f"Resultado do Produto da coluna: {numColuna}: {produto}")