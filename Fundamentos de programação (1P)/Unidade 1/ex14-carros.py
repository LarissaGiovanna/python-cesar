#comparação de anos de carros (nao concluido)
while True:
    marca = input("Digite a marca do carro: ")
    ano = int(input("Digite o ano do carro: "))
    ano2 = 0
    if marca == "nao" or marca == "n":
        break
    else:
        if ano > ano2 and ano2 == 0:
            ano2 = ano
            print(ano2, ano)
        elif ano2 < ano:
            antigo = ano2
            print(antigo)
        else:
            novo = ano2
            print(novo)

        