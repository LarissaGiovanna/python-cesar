print("========= Serviços: =========\n1 - banho\n2 - tosa\n3 - banho e tosa\n4 - outros")

banho = 0
tosa = 0
banhoTosa = 0
outros = 0
invalido = 0

for i in range(5):
    servico = int(input("Digite o número do serviço solicitado: "))
    if servico == 1:
        print("selecionado banho")
        banho =+1
    elif servico == 2:
        print("selecionado tosa")
        tosa =+1
    elif servico == 3:
        print("selecionado banho e tosa")
        banhoTosa =+1
    elif servico == 4:
        print("selecionado outros")
        outros =+ 1
    else:
        print("invalido")
        invalido =+ 1

print (f"Solicitações:\n{banho} solicitação(ões) para banho\n{tosa} solicitação(ões) para tosa\n{banhoTosa} solicitação(ões) para banho e tosa\n{outros} solicitação(ões) para outros\n{invalido} solicitação(ões) invalida(s)\n")