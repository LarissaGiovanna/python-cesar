frase = input("Digite uma frase: ").upper()
palavra = input("Digite uma palavra que existe na frase: ").upper()
novaPalavra = input("Digite uma nova palavra: ").upper()

if palavra in frase:
    frase = frase.replace(palavra, novaPalavra)
    print(frase)
else:
    print(f"A palavra '{palavra}' não está contida na frase.")