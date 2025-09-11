#calculo da potencia do voltorb com base no level

from math import pow #pow(base, expoente)
level = int(input("Digite o level do voltorb (1-100): "))

if level <=0:
    print("Valor inválido")
elif level <=20:
    potencia = 20 + pow(level, 3) #ou: potencia = 20 + level**3
    print(potencia, "W")
elif level >=21 and level <=40: #ou: elif >=21 level <=40
    potencia = 8000 + pow((level-10), 2) 
    print(potencia, "W")
elif level >=41 and level <=60:
    potencia = 9000 + 5 * level
    print(potencia, "W")
elif level >=61 and level <=80:
    potencia = 9300 + 2 * level
    print(potencia, "W")
elif level >=81 and level <=100:
    potencia = 9500 + level
    print(potencia, "W")
else:
    print("Valor invalido")