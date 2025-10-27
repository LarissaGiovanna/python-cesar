fraseDividida = []
frase = ""

while frase != "0":
    frase = input().strip()
    if frase != "0":
        fraseDividida.append(frase.split())

def separar_e_contar(frase):
    maior_palavra = ""
    codigo = []
    for i in range(len(frase)):
        qnt_caracteres = []
        for j in range (len(frase[i])):
            qnt_caracteres.append(str(len(frase[i][j])))
            
            #inserir os codigos na lista
            try:
                codigo[i] =  "-".join(qnt_caracteres)
            except IndexError:
                codigo.append("-".join(qnt_caracteres))

            if len(frase[i][j]) >= len(maior_palavra):
                maior_palavra = frase[i][j]

    for k in codigo:
        print(k)

    print(f"The biggest word: {maior_palavra}")

separar_e_contar(fraseDividida)