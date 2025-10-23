tabuleiro = [[],[],[],[],[],[],[],[]] #tabuleiro 8x8

# ------------------- Definição e atribuição das peças -----------------------------
def transformacao_posicao_indice(posicao): #mudar string pra num da posição
    letra = posicao[0].lower()
    numero = posicao[1]
    coluna = 0
    if letra in ["a", "b", "c", "d", "e", "f", "g", "h"]:
        coluna = ord(letra) - ord('a') #ord transforma o caractere no numero da tabela ascii
        #97 (a) - 97 (a) = 0 (indice 0)
    else:
        print("posição invalida") 

    linha = 8 - int(numero) #indice (ex: 8 - 7 = 1(indice 1))

    nova_posicao = [linha, coluna]
    return nova_posicao

def definir_posicao_bispo(posicao_input):
    #letras = colunas
    #numeros = linhas
    posicao_transformada = transformacao_posicao_indice(posicao_input)
    for i in range(8):
        for j in range(8):
            tabuleiro[i].append("_")

            linha, coluna = posicao_transformada

            if i == linha and j == coluna:
                tabuleiro[i][j] = "B"

def imprimir_tabuleiro():
    for i in range(8):
        for j in range(8):
            print(f"[{tabuleiro[i][j]}]", end=' ')
        print()

def definicao_pecas_inimigas(qnt_pecas):
    inimigas = []
    inimigas_posicao = []

    for i in range(qnt_pecas):
        inimigas.append(input(f"Posição peça {i+1}: "))

        inimigas_posicao.append(transformacao_posicao_indice(inimigas[i])) #transformação de posição para indice guardando numa lista

    atribuicao_posicao_inimigas(inimigas_posicao)
    return inimigas_posicao

def atribuicao_posicao_inimigas(inimigas_posicao):
    for i in range(8):
        for j in range(8):
            for k in range (len(inimigas_posicao)): #for para percorrer as posições das peças inimigas
                linha, coluna = inimigas_posicao[k]

                if i == linha and j == coluna and tabuleiro[i][j] != "B":
                    tabuleiro[i][j] = "X"

# ----------------------- Varredura --------------------------

def mover_bispo__inferior_esquerda(posicao_bispo):
    nova_linha = posicao_bispo[0] - 1
    nova_coluna = posicao_bispo[1] - 1
    nova_posicao = [nova_linha, nova_coluna]
    return nova_posicao

def mover_bispo__inferior_direita(posicao_bispo):
    nova_linha = posicao_bispo[0] + 1
    nova_coluna = posicao_bispo[1] - 1
    nova_posicao = [nova_linha, nova_coluna]
    return nova_posicao

def mover_bispo__superior_esquerda(posicao_bispo):
    nova_linha = posicao_bispo[0] - 1
    nova_coluna = posicao_bispo[1] + 1
    nova_posicao = [nova_linha, nova_coluna]
    return nova_posicao

def mover_bispo__superior_direita(posicao_bispo):
    nova_linha = posicao_bispo[0] + 1
    nova_coluna = posicao_bispo[1] + 1
    nova_posicao = [nova_linha, nova_coluna]
    return nova_posicao

def pode_comer_pecas(posicao_inicial_bispo, posicao_pecas_inimigas, qnt_pecas_inimigas):
    #  inf. esquerda | sup. direita | sup. esquerda | inf. direita
    pode_capturar = 0
    for i in range(qnt_pecas_inimigas): #qnt das pecas inimigas
        #correr pelo tabuleiro
        for j in range(8):
            for k in range(8):

                posicao_atual_bispo = posicao_inicial_bispo

                inf_direita_posicao = mover_bispo__inferior_direita(posicao_atual_bispo)
                inf_esquerda_posicao = mover_bispo__inferior_esquerda(posicao_atual_bispo)
                sup_direita_posicao = mover_bispo__superior_direita(posicao_atual_bispo)
                sup_esquerda_posicao = mover_bispo__superior_direita(posicao_atual_bispo)

                if inf_direita_posicao == posicao_pecas_inimigas[i]:
                    pode_capturar += 1
                elif inf_esquerda_posicao == posicao_pecas_inimigas[i]:
                    pode_capturar += 1
                elif sup_direita_posicao == posicao_pecas_inimigas[i]:
                    pode_capturar +=1
                elif sup_esquerda_posicao == posicao_pecas_inimigas[i]:
                    pode_capturar += 1
                else:
                    pode_capturar = pode_capturar

                #verificacao se pode capturar
                # if j == (posicao_pecas_inimigas[i])[0] and k == (posicao_pecas_inimigas[i])[1]:
                #     pode_capturar += 1
    
    return pode_capturar


#-------------------------- MAIN -------------------------------

posicao = input("Digite a posição do bispo: ")
definir_posicao_bispo(posicao)
nova_posicao_bispo = transformacao_posicao_indice(posicao)
imprimir_tabuleiro()

qnt_pecas_inimigas = int(input("Digite a quantidade de peças inimigas: "))
posicoes_pecas_inimigas = definicao_pecas_inimigas(qnt_pecas_inimigas)
imprimir_tabuleiro()

pode_capturar = pode_comer_pecas(nova_posicao_bispo, posicoes_pecas_inimigas, qnt_pecas_inimigas)

print(f"Podem ser capturadas {pode_capturar} peças.")