nomes = []
idades = []
maior = 0
soma = 0
media = 0
qntFuncionarios = int(input("Digite a quantidade de funcionários aptos para a aposentadoria: "))

for i in range(qntFuncionarios):
    nome = input("Digite o nome do funcionário: ")
    idade = int(input("Digite a idade: "))
    
    if idade < 60:
        print("Idade não apta. Insira os dados novamente")
    else: 
        nomes.append(nome)
        idades.append(idade)
        soma = soma + idade
        
        if idade > maior:
            maior = idade
            maiorNome = nome

print("== Funcionários a se aposentar em 2025: ==")
for i in range(len(nomes)):
    print(f"Nome: {nomes[i]}\t\t Idade: {idades[i]} anos")

print(f"Funcionário mais antigo: {maiorNome}")

media = soma/len(idades)
print(f"Média da soma de todas as idades: {media}")