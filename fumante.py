import os
os.system("cls")

mediaCigarros = float(input("Digite a quantidade média de cigarros por dia: "))
anosFumados = int(input("Digite a quantidade de anos que a pessoa já fumou: "))

minutosPerdidos = (anosFumados*365)*mediaCigarros
diasPerdidos = (minutosPerdidos*10)/1440

print(f"Você poderia ter vivido {diasPerdidos:.0f} dias a mais se você não fumasse.")