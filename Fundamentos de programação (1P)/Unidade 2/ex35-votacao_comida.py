print("Votação:\n 1- Sushi\n2 - Churrasco")
votos = []
arquivo = open("ex35-votacao_comida.txt", "w", encoding="utf8")
for i in range (10):
    num = input("Seu voto: ")
    if num == "1" or num == "2":
        votos.append(num)
        arquivo.write(num + "\n")

arquivo.close()

sushi = 0
churrasco = 0
for i in range(len(votos)):
    if votos[i] == 1:
        sushi += 1
    else: 
        churrasco +=1

if sushi > churrasco:
    print("Sushi ganhou")
elif churrasco > sushi:
    print("Churrasco ganhou")
else: 
    print("Empate")