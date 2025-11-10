def listar_nomes():
    arquivo = open("Q4_nomes.txt", "r", encoding="utf8")
    conteudo_arquivo = arquivo.readlines()
    nomes_repetidos = []
    vezes_repetido = []

    for i in conteudo_arquivo:
        nome_formatado = i.strip() #apaga o \n
        if nome_formatado != "" and conteudo_arquivo.count(i) > 1 and nome_formatado not in nomes_repetidos:
            nomes_repetidos.append(nome_formatado)
            vezes_repetido.append(conteudo_arquivo.count(i))

    if nomes_repetidos != []:
        print("Nome dos alunos registrados no arquivo: ")
        for nomes in conteudo_arquivo:
            print(nomes.strip())
            
        print("\nNome dos alunos que se repetiram: ")
        for j in range(len(nomes_repetidos)):
            print(f"{nomes_repetidos[j]}: {vezes_repetido[j]} vezes")
    else:
        print("Não houve nenhum aluno com o nomes repetido.")
        print("Nome dos alunos: ")
        for nomes in conteudo_arquivo:
            print(nomes.strip())

    arquivo.close()

while True:
    nome = input("Digite o nome do aluno ou digite 'sair' para encerrar o programa: ")
    try:
        if nome.lower() == "sair":
            listar_nomes()
            break
        elif nome == "":
            print("Entrada inválida. Se quiser encerrar, digite 'sair'")
            continue
        else:
            arquivo = open("Q4_nomes.txt", "a", encoding="utf8")
            arquivo.write(nome.lower() + "\n")
            arquivo.close()
    except ValueError:
        print("Entrada inválida. Se quiser encerrar, digite 'sair'")