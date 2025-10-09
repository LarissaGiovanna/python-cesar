#Calculo para ver quantas pessoas podem ou nao podem entrar no parque de acordo com a altura
numVisitantes = int(input("Digite a quantidade de visitantes do parque: "))
minAltura = float(input("Digite a altura mínima para entrar no parque: "))
maxAltura = float(input("Digite a altura máxima para entrar no parque: "))

pode = 0
naoPode = 0

for i in range(0, numVisitantes):
    altura = float(input("Digite a sua altura: "))
    if altura >= minAltura and altura <= maxAltura:
        pode=pode+1
    else:
        naoPode=naoPode+1

print(f"Podem entrar: {pode} pessoas\nNão Podem entrar: {naoPode}")