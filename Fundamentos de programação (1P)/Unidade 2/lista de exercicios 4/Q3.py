def escrever_arquivo():
    arquivo = open("Q3_numeros.txt", "w")
    numero = int(input("Digite um número (ou digite qualquer outra coisa que não seja um número para sair): "))
    arquivo.write(str(numero) + "\n")
    arquivo.close()

    while True:
        try:
            numero = int(input("Digite um número: "))
            arquivo = open("Q3_numeros.txt", "r")
            
            numeros_arquivo = arquivo.readlines()
            for numeros in numeros_arquivo:
                numeros_lista = []
                numeros_lista.append(numeros.replace("\n", ""))
                arquivo.close()
                
                if numero in numeros_lista:
                    print("Número menor ou igual aos números já existentes do arquivo. Número não computado no arquivo.")
                else:
                    arquivo = open("Q3_numeros.txt", "a")
                    arquivo.write(str(numero) + "\n")
        except ValueError:
            break
    
    arquivo = open("Q3_numeros.txt", "r")
    return arquivo.read(), arquivo.close()

while True:
    opcao = int(input("O que você deseja fazer?\n 1 - Sair\n 2 - Ler arquivo\n 3 - Escrever no arquivo\nOpção: "))
    if opcao == 1:
        break
    elif opcao == 2:
        try:
            arquivo = open("Q3_numeros.txt", "r")
            print(f"Conteúdo do arquivo: \n{arquivo.read()}")
            arquivo.close()
        except FileNotFoundError:
            mensagem = input("Esse arquivo ainda não existe ou não foi encontrado. Você quer criar um agora? (sim/nao) ")
            if mensagem.lower() == "sim":
                escrever_arquivo()
    elif opcao == 3:
        escrever_arquivo()
    else:
        print("Opção inválida.")