#codigo que recebe uma frase e diz a quantidade de palavras naquela frase
def contar_palavras(frase):
    return len(frase)

frase = input("Digite uma frase: ")
frase_divida = frase.split()
print(f"A frase '{frase}' possui {contar_palavras(frase_divida)} palavra(s)")