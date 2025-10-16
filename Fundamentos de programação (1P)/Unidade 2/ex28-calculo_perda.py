def calcular_percentual_perda(peso_inicial, peso_atual):
    diferenca = peso_inicial - peso_atual
    percentual = diferenca / peso_inicial * 100
    return percentual

peso_inicial = float(input("Digite o seu peso inicial em kg: "))
peso_atual = float(input("Digite o seu peso atual em kg: "))

print(f"O seu percentual de perda é de {calcular_percentual_perda(peso_inicial, peso_atual):.2f} %")