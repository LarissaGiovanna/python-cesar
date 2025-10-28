arquivo_cadastro = open("ex32-adocao_animais.txt", "a", encoding="utf8")
nome = []
raca = []

for i in range(5):
    nome.append(input("Digite o nome do animal: "))
    raca.append(input("Digite a raça: "))

for i in range(5):
    arquivo_cadastro.write("Nome: " + nome[i] + " | " + "Raça: " + raca[i] + "\n")

arquivo_cadastro.close()

arquivo_cadastro = open("ex32-adocao_animais.txt", "r", encoding="utf8")
print(arquivo_cadastro.read())

arquivo_cadastro.close()