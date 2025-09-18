contador = 0
harry = 0
somaHarry = 0
hermione = 0
somaHermione = 0
branco = 0
somaBranco = 0
while True:
    voto = input("Digite o seu voto: ")
    if voto == 1:
        harry=+1
        somaHarry =+1
        contador=+1
    elif voto == 2:
        hermione =+1
        somaHermione =+1
        contador=+1
    elif voto == 3:
        branco =+1
        somaBranco=+1
        contador=+1
    else:
        break
#if somaHermione > somaHarry:
print(f"numero de votos {contador}\n")
