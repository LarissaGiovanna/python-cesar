def escrever_arquivo():
    numeros_lista = []
    arquivo = open("Q3_numeros.txt", "w")

    while True:
        try:
            numero = int(
                input(
                    "Digite um número (ou digite qualquer outra coisa que não seja um número para sair): "
                )
            )
            print(numeros_lista)

            if numeros_lista != []: #quando a lista tiver algum conteudo
                if numero <= max(numeros_lista): #se o numero for menor ou igual ao maior numero da lista
                    print(
                        "Número menor ou igual aos números já existentes do arquivo. Número não computado no arquivo."
                    )
                else:
                    numeros_lista.append(numero)
                    arquivo.close()
                    arquivo = open("Q3_numeros.txt", "a")
                    arquivo.write(str(numero) + "\n")
                    arquivo.close()

            else: #caso a lista nao tenha nenhum conteudo
                numeros_lista.append(numero)
                arquivo.write(str(numero) + "\n")

        except ValueError: 
            arquivo = open("Q3_numeros.txt", "r")
            print(f"Conteúdo do arquivo: \n{arquivo.read()}")
            arquivo.close()
            break


while True:
    opcao = int(
        input(
            "O que você deseja fazer?\n 1 - Sair\n 2 - Ler arquivo\n 3 - Escrever no arquivo\nOpção: "
        )
    )
    try:
        if opcao == 1:
            break
        elif opcao == 2:
            try:
                arquivo = open("Q3_numeros.txt", "r")
                print(f"Conteúdo do arquivo: \n{arquivo.read()}")
                arquivo.close()
            except FileNotFoundError:
                mensagem = input(
                    "Esse arquivo ainda não existe ou não foi encontrado. Você quer criar um agora? (sim/nao) "
                )
                if mensagem.lower() == "sim":
                    escrever_arquivo()
        elif opcao == 3:
            escrever_arquivo()
        else:
            print("Opção inválida.")
    except ValueError:
        print("Opção inválida. Se quiser sair, digite 1")
