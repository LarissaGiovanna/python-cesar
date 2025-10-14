cardapio = {"coxinha": "R$5,00", "Pastel": "R$4,00", "Suco": "R$3,50", "Bolo": "R$4,50"}
opcao = ""
while(True):
    print("1 - Remover\n2 - Adicionar\n3 - Modificar\n4 - Encerrar")
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        produto = input("Digite o nome do produto: ")
        if produto in cardapio:
            cardapio.pop(produto)
            print(f"Cardápio: {cardapio}")

    elif opcao == 2:
        produto_novo = input("Digite o nome do novo produto: ")
        preco_novo = input("Digite o preço do novo produto em reais: ")
        cardapio[produto_novo] = preco_novo
        print(f"Cardápio: {cardapio}")

    elif opcao == 3:
        produto = input("Digite o nome do produto que você quer modificar: ")
        
        if produto in cardapio:
            produto_novo = input("Novo nome: ")
            preco_novo = input("Novo preço: ")
            del cardapio[produto]
            cardapio[produto_novo] = preco_novo
            print(f"Cardápio: {cardapio}")

    elif opcao == 4:
        break

    else:
        print("Opção inválida")