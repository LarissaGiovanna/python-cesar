nome = []
idade = []
sobrenome = []
cadastro = open("ex33-cadastro_pessoas.txt", "w", encoding="utf8")
qnt = int(input("Digite a quantidade de pessoas que serao cadastradas: "))

for i in range (qnt):
    nome.append(input("Digite o nome da pessoa: "))
    sobrenome.append(input("Digite o sobrenome da pessoa: "))
    idade.append(input("Digite a idade da pessoa: "))

cadastro.write("Há "+ str(qnt)+" pessoa(s) cadastradas: \n")

for i in range(qnt):
    cadastro.write("Nome: " + nome[i] + " " + sobrenome[i] + " | " + "Idade: " + idade[i] + "\n")

cadastro.close()

cadastro = open("ex33-cadastro_pessoas.py", "r", encoding="utf8")
print(cadastro.read())
cadastro.close()