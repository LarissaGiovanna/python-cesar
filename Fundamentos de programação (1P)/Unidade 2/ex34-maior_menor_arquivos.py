num = []
arquivo = open("ex34-maior_menor_arquivos.txt", "w", encoding="utf8")
for i in range(10):
    num.append(input())
for i in range(10):
    arquivo.write(num[i] + "\n")

arquivo.close()

maior = 0
maiores_num = []
for index in range(1, 10):
    if int(num[index]) > maior:
        maiores_num.append(num[index])
    maior = int(num[index])

print()
print(len(maiores_num))
print(maiores_num)