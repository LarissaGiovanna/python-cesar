tabuleiro = [[],[],[],[],[],[],[],[]] #tabuleiro 8x8

def atribuicao_letra_num(posicao_x): #mudar string pra num da posição
    if posicao_x.lower() == 'a':
        return 1
    elif posicao_x.lower() == 'b':
        return 2
    elif posicao_x.lower() == 'c':
        return 3
    elif posicao_x.lower() == 'd':
        return 4
    elif posicao_x.lower() == 'e':
        return 5
    elif posicao_x.lower() == 'f':
        return 6
    elif posicao_x.lower() == 'g':
        return 7
    elif posicao_x.lower() == 'h':
        return 8
    else:
        print("posição invalida")

def definir_posicao_bispo(posicao_input):
    #letras = colunas
    #numeros = linhas
    coluna = atribuicao_letra_num(posicao_input[0])
    linha = posicao_input[1]
    for i in range(8):
        for j in range(8):
            tabuleiro[i].append("nada")

            if i == linha and j == coluna:
                tabuleiro[i].append("bispo")

def imprimir_tabuleiro():
    for i in range(8):
        for j in range(8):
            print(f"[{tabuleiro[i][j]}]", end=' ')
        print()

posicao = input("Digite a posição do bispo: ")
definir_posicao_bispo(posicao)
imprimir_tabuleiro()