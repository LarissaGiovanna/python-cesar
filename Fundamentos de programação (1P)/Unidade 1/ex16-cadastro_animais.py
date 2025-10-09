repteis =[]
mamiferos =[]
aves =[]
outros =[]

print("====== Cadastro animais ======")
print("1-Reptil\n2-Mamifero\n3-Ave\n4-Outro")

for i in range (10):
    animal = input("Digite o nome do bicho: ")
    categoria = int(input("Digite a categoria: "))

    if categoria < 1 or categoria > 4:
        print("valor invalido")
    else:
        if categoria == 1:
            repteis.append(animal)
        elif categoria == 2:
            mamiferos.append(animal)
        elif categoria == 3:
            aves.append(animal)
        else:
            outros.append(animal)

print(f"Répteis: {repteis}; Quantidade: {len(repteis)}\nMamíferos: {mamiferos}; Quantidade: {len(mamiferos)}\nAves: {aves}; Quantidade: {len(aves)}\nOutros: {outros}; Quantidade: {len(outros)}")