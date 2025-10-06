nome_produto = []
quant_produto = []

while(True):
    opcao = input("Digite a função que vc quer: ")
    if opcao.upper() == "AP": #add novo produto
        nome_produto.append(input("Digite o nome do produto: "))
        quant_produto.append(int(input("Digite a quantidade inicial: ")))

    elif opcao.upper() == "RP":
        nome = input("Digite o nome do produto a ser removido: ")
        index = nome_produto.index(nome)
        
        nome_produto.remove(nome)
        quant_produto.pop(index)
        print(f"produto '{nome}' removido")
    
    elif opcao.upper() == "AE":
        nome = input("Digite o nome do produto que sera alterada a quantidade: ")
        add = int(input("Digite quantas unidades esse pruduto tera: "))
        
        index = nome_produto.index(nome)
        acresenta = quant_produto[index] + add
        quant_produto.pop(index)
        quant_produto.insert(index, acresenta)
        
        print(f"O produto '{nome}' agora possui {quant_produto[index]} unidades")
        
    elif opcao.upper() == "RE":
        nome = input("Digite o nome do produto que sera removida a quantidade: ")
        delete = int(input("Digite a quantidade que sera removida: "))
        
        index = nome_produto.index(nome)
        subtrai = quant_produto[index] - delete
        quant_produto.pop(index)
        quant_produto.insert(index, subtrai)
        
        print(f"O produto '{nome}' agora possui {quant_produto[index]} unidades")
        
    elif opcao.upper() == "S":
        for i in range (len(nome_produto)):
            print(f"{nome_produto[i]}: {quant_produto[i]}")
        break
    
    else:
        print("funcao invalida")
        continue
    