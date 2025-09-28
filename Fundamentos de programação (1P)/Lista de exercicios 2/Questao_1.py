defeitos =[]
quantMouses = int(input("Digite a quantidade de mouses: "))
for i in range(quantMouses):
    print("\n1- Necessita da esfera\n2 - Necessita de limpeza\n3 - Necessita troca do cabo ou conector\n4 - Quebrado ou inutilizado")
    defeito = int(input("Situação: "))
    if defeito < 1 or defeito > 4:
        print("Opção inválida")
    else:
        defeitos.append(defeito)

print(f"\nQuantidade de mouses: {quantMouses} mouses")
print(f"\nSituação\t\t\t\tQuantidade\t\tPercentual\n")
print(f"1-Necessita da esfera\t\t\t\t{defeitos.count(1)}\t\t{(defeitos.count(1)/quantMouses)*100:.1f}%")
print(f"2-Necessita de limpeza\t\t\t\t{defeitos.count(2)}\t\t{(defeitos.count(2)/quantMouses)*100:.1f}%")
print(f"3-Necessita troca do cabo ou conector\t\t{defeitos.count(3)}\t\t{(defeitos.count(3)/quantMouses)*100:.1f}%")
print(f"4-Quebrado ou inutilizado\t\t\t{defeitos.count(4)}\t\t{(defeitos.count(4)/quantMouses)*100:.1f}%")