#verificar se um numero é perfeito
num = int(input("Digite um número: "))
divisores = 0

for i in range (1, num):
    if num%1 == 0:
        divisores +=1

if divisores == num:
    print("É perfeito")
else:
    print("Não é perfeito")