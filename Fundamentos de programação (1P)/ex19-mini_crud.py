dados =[]
while(True):
    print("1. CREATE (Criar)\n2. READ (Ler)\n3. UPDATE (Atualizar)\n4. DELETE (Deletar)")
    opcao = int(input("Opção: "))
    print("\n")
    
    if opcao == 5:
        print("Programa encerrado")
        break
    elif opcao > 5 or opcao < 1:
        print("Opção inválida")
    elif opcao == 1:
        dado = input("Digite o que será adicionado: ")
        dados.append(dado)
    elif opcao == 2:
        for i in dados:
            print(f"Dado: {i}; Indice: [{dados.index(i)}]")
    elif opcao == 3:
        indice = int(input("Digite o índice que vc deseja alterar: "))
        if indice < 0 and indice >=len(dados):
            print("Esse índice não existe nessa lista")
        else:
            novoDado = input(f"Digite o novo dado que será adicionado no índice [{indice}]: ")
            dados[indice] = novoDado
    else:
        indice = int(input("Digite o índice que você quer remover: "))
        if indice < 0 and indice >=len(dados):
            print("Esse índice não existe nessa lista")
        else:
            dados.pop(indice)
            print(f"[{indice}] removido")