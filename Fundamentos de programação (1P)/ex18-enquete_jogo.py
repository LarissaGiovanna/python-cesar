votos = []
#loop
while (True):
    voto = int(input("Digite o seu voto (entre 7 e 11): "))
    if voto == 0:
        print("Votação encerrada")
        break
    elif voto < 7 or voto > 11:
        print("Voto inválido")
    else:
        votos.append(voto)

#quantidade total dos votos
totalVotos = len(votos)
print(f"Quantidade total de votos: {totalVotos}")

#contagem dos votos
votosJogador7 = votos.count(7)
votosJogador8 = votos.count(8)
votosJogador9 = votos.count(9)
votosJogador10 = votos.count(10)
votosJogador11 = votos.count(11)

#porcentagem dos votos
percent7 = (votosJogador7/len(votos))*100
percent8 = (votosJogador8/len(votos))*100
percent9 = (votosJogador9/len(votos))*100
percent10 = (votosJogador10/len(votos))*100
percent11 = (votosJogador11/len(votos))*100

#verificação jogador ganhador
if votosJogador7 > votosJogador8 and votosJogador7 > votosJogador9 and votosJogador7 > votosJogador10 and votosJogador7 > votosJogador11:
    ganhador = "Jogador 7"
    ganhadorVotos = votosJogador7
    ganhadorPercent = percent7
elif votosJogador8 > votosJogador7 and votosJogador8 > votosJogador9 and votosJogador8 > votosJogador10 and votosJogador8 > votosJogador11:
    ganhador = "Jogador 8"
    ganhadorVotos = votosJogador8
    ganhadorPercent = percent8
elif votosJogador9 > votosJogador7 and votosJogador9 > votosJogador8 and votosJogador9 > votosJogador10 and votosJogador9 > votosJogador11:
    ganhador = "Jogador 9"
    ganhadorVotos = votosJogador9
    ganhadorPercent = percent9
elif votosJogador10 > votosJogador7 and votosJogador10 > votosJogador8 and votosJogador10 > votosJogador9 and votosJogador10 > votosJogador11:
    ganhador = "Jogador 10"
    ganhadorVotos = votosJogador10
    ganhadorPercent = percent10
else:
    ganhador = "Jogador 11"
    ganhadorVotos = votosJogador11
    ganhadorPercent = percent11

#mensagem final
print(f"Jogador 7: {votosJogador7} votos ({percent7}%)\nJogador 8: {votosJogador8} votos ({percent8}%)\nJogador 9: {votosJogador9} votos ({percent9}%)\nJogador 10: {votosJogador10} votos ({percent10}%)\nJogador 11: {votosJogador11} votos ({percent11}%)")
print(f"O ganhador final foi o {ganhador} com {ganhadorVotos} votos ({ganhadorPercent}%).")