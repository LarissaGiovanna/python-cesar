nome = input("Digite o nome do cliente: ")
pedido = int(input("Digite o número do pedido: "))
valor = float(input("Digite o valor da compra: "))
pagamento = input("Digite a forma de pagamento: ")

print(f"O cliente {nome} realizou um pedido de número {pedido} no valor de R${valor}, e o seu pagamento será {pagamento}")