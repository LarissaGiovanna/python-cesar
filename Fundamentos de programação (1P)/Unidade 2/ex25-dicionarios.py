#dicionario com uma lista do numero e do seu quadrado
num = int(input("Digite um número inteiro: "))
dicionario_quadrado = {}

for i in range(num+1):
    dicionario_quadrado[i] = i*i

print(dicionario_quadrado)