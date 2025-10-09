frase = input("Digite uma frase ou palavra: ").upper().replace(" ", "")
if frase == frase[::-1]:
    print(f"A frase/palavra '{frase}' é um palindromo")
else:
    print(f"A frase/palavra '{frase}' não é um palindromo")