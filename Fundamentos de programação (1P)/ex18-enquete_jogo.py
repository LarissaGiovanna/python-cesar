votos = []
while (True):
    voto = int(input("Digite o seu voto (entre 7 e 11): "))
    if voto == 0:
        print("Votação encerrada")
        break
    elif voto < 7 or voto > 11:
        print("Voto inválido")
    else:
        votos.append(voto)

totalVotos = len(votos)
print(f"Quantidade total de votos: {totalVotos}")

print()