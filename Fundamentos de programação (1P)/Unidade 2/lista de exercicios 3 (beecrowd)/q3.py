alimentos = {
    "suco de laranja": 120,
    "morango fresco": 85,
    "mamao": 85,
    "goiaba vermelha": 70,
    "manga": 56,
    "laranja": 50,
    "brocolis": 34
}

alimentos_consumidos = []

def calculo_vitamina():

    for i in range(len(alimentos_consumidos)):
        miligramas_consumidos = 0
        for j in range(len(alimentos_consumidos[i])):
            qnt_alimento = alimentos_consumidos[i][j][0]
            alimento = alimentos_consumidos[i][j][1]
            miligrama_alimento = alimentos[alimento]
            miligramas_consumidos += int(qnt_alimento) * miligrama_alimento
         
        if miligramas_consumidos >= 110 and miligramas_consumidos <= 130:
            print(f"{miligramas_consumidos} mg")
        elif miligramas_consumidos > 130:
            quanto_precisa = miligramas_consumidos - 130
            print(f"Menos {quanto_precisa} mg")
        elif miligramas_consumidos < 110:
            quanto_precisa = 110 - miligramas_consumidos
            print(f"Mais {quanto_precisa} mg")

qnt = 1
while True:
    qnt_e_alimento = []
    qnt = int(input())
    if qnt != 0:
        for i in range(qnt):
            qnt_e_alimento.append(input().strip().split(' ', 1)) #manda dividir so uma vez

        alimentos_consumidos.append(qnt_e_alimento)
    else:
        break

calculo_vitamina()
