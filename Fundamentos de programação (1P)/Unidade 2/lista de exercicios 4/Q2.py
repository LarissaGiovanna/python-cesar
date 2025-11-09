print("Votação melhor filme\n 1 - Star Wars\n 2 - Star Trek")
votos = open("Q2_votos.txt", "w")

for _ in range(10):
    votos.write(str(input("Seu voto: ")) + "\n")

votos.close()

votos = open("Q2_votos.txt", "r")
s_wars = 0
s_trek = 0
nulos = 0

for _ in range(10):
    voto = votos.readline()
    try:
        if int(voto) == 1:
            s_wars += 1
        elif int(voto) == 2:
            s_trek += 1
        else:
            nulos += 1
    except ValueError:
        print("Só aceitamos entradas do tipo String.")
        nulos += 1

votos.close()

def verificar_ganhador(candidato1, candidato2):
    if candidato1 > candidato2:
        return "Ganhador: Star Wars " + f"Votos: {candidato1}"
    elif candidato2 > candidato1:
        return "Ganhador: Star Trek " + f"Votos: {candidato2}"
    elif candidato1 == candidato2 and candidato1 != 0 and candidato2 != 0:
        return "Empate"
    else:
        return "Ninguém ganhou"

print("======== Resultados ========")
print(verificar_ganhador(s_wars, s_trek))
print(f"Votos nulos: {nulos}")
