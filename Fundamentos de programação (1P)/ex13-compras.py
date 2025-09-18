soma = 0
while True:
    valorProduto = float(input("Digite os valores dos produtos: "))
    if valorProduto == 0:
        break
    elif valorProduto > 0:
        soma = soma+valorProduto
        if soma > 1000:
            soma = soma - (soma*0.1)
            continue
        else:
            continue
    else:
        continue
    
print(f"Valor total: R$ {soma}")           
