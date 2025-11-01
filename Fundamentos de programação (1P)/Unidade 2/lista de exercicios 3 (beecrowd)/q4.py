def contar_votos(votos, qnt_jogadores):
    a_favor = 0
    for i in range(len(votos)):
        a_favor = 0
        for j in votos[i]:
            if j == "1":
                a_favor +=1

        if ((2/3) * qnt_jogadores[i]) <= a_favor:
            print("impeachment")
        else:
            print("acusacao arquivada")

votos = []
qnt_jogadores = []

while True:
    try:
        qnt_jogadores.append(int(input()))
        votos.append(input().split())
    except EOFError or qnt_jogadores == "" or ValueError:
        contar_votos(votos, qnt_jogadores)
        break
  
