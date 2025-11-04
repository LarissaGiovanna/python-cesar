vetor = []
i = 0
while i <= 10:
    try:
        vetor.append(int(input("Digite um número: ")))
        i += 1
        if i == 10:
            break
    except ValueError:
        print("Digite valores inteiros")

print(vetor)
menor = 0
maior = 0
igual = 0
for i in range(1, 10):
    try:
        if vetor[i] < vetor[0]:
            menor += 1
        elif vetor[i] > vetor[0]:
            maior += 1
        elif vetor[i] == vetor[0]:
            igual += 1
    except IndexError:
        print("O indice não existe")
try:
    print(f"Quantos nums maior que o primeiro num: {maior}")
    print(f"Quantos nums menor que o primeiro num: {menor}")
    print(f"Quantos nums iguais ao primeiro num: {igual}")
except ValueError:
    print()