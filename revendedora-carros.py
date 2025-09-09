import os
os.system("cls")

carrosVendidos = int(input("Digite a quantidade de carros vendidos: "))
comissao = float(input("Digite o valor da comissão: "))
salario = float(input("Digite o valor do salario fixo: "))
valorVendas = float(input("Digite o valor total das vendas dos carros: "))

salarioFinal = salario + comissao + (0.05 * valorVendas)
print(f"Salario final: {salarioFinal}")