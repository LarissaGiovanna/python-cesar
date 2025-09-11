#app que faz o reajuste salarial com base no ano do ultimo reajuste
import os
os.system("cls")

anoEntrada = int(input("Digite o ano de entrada na empresa: "))
salarioAtual = float(input("Digite o seu salario atual: "))
anoAjuste = int(input("Digite o último ano que seu salário foi reajustado: "))

tempoUltimoAjuste = 2025 - anoAjuste
tempoAnosCasa = 2025 - anoEntrada

if tempoUltimoAjuste < 2:
    print("Não está apto para receber o reajuste")
else:
    if tempoAnosCasa < 5:
        salarioFinal = salarioAtual + (salarioAtual*0.1) 
        print(f"Seu salario final ficará R$ {salarioFinal}")
    elif tempoAnosCasa >=5 and tempoAnosCasa <=10:
        salarioFinal = salarioAtual + (salarioAtual*0.2)
        print(f"Seu salario final ficará R$ {salarioFinal}")
    else:
        salarioFinal = salarioAtual + (salarioAtual*0.3)
        print(f"Seu salario final ficará R$ {salarioFinal}")