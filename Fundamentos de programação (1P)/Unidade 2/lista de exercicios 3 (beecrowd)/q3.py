alimentos = {
    "suco de laranja": 120,
    "morango fresco": 85,
    "mamao": 85,
    "goiaba vermelha": 70,
    "manga": 56,
    "laranja": 50,
    "brocolis": 34
}

dict_alimentos_consumidos = {}

qnt_e_alimento = []
def calculo_vitamina(qnt_e_alimento):
    resultados = []

    for i in range(len(qnt_e_alimento)):
        key_alimentos = qnt_e_alimento[i][0]
        alimentos_consumidos = []
        for j in range(int(key_alimentos)):
            alimentos_consumidos.append(qnt_e_alimento[i][j])
        dict_alimentos_consumidos[key_alimentos] = alimentos_consumidos

        # miligrama_alimento = alimentos[qnt_e_alimento[i][1]]

        # miligramas_consumidos = int(qnt_e_alimento[i][0]) * (miligrama_alimento)

        # if miligramas_consumidos > 110 and miligramas_consumidos < 130:
        #     resultados.append(f"{miligrama_alimento}  mg")
        # elif miligramas_consumidos > 130:
        #     quanto_precisa = miligramas_consumidos - 130
        #     resultados.append(f"Menos {quanto_precisa} mg")
        # elif miligramas_consumidos < 110:
        #     quanto_precisa = 110 - miligramas_consumidos
        #     resultados.append(f"Mais {quanto_precisa} mg")
    return resultados

qnt = 1
while qnt != 0:
    qnt = int(input())
    for i in range(qnt):
        qnt_e_alimento.append(input().split(' ', 1)) #manda dividir so uma vez

resultados = calculo_vitamina(qnt_e_alimento)
for i in resultados:
    print(i)
