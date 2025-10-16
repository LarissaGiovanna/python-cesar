def calcular_idadde(ano_atual, ano_nascimento):
    if ano_atual > ano_nascimento:
        idade = ano_atual - ano_nascimento
        return idade
    else:
        print("ano de nascimento invalido")
        
def maioridade(nome, idade):
    if idade >= 18:
        print(f"{nome} é maior de idade")
    else:
        print(f"{nome} é de menor")
        
nome = input("Digite seu nome: ")
ano_agora = int(input("Em que ano estamos? "))
ano_nascimento = int(input("Digite o ano do seu nascimento: "))
maioridade(nome, calcular_idadde(ano_agora, ano_nascimento))
    