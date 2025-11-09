enderecos_ip = open("Q1_enderecos_ip.txt", "w")
for i in range(8):
    enderecos_ip.write(input("Digite o endereço ip: ") + "\n")
enderecos_ip.close()

try:
    enderecos_ip = open("Q1_enderecos_ip.txt", "r")
except FileNotFoundError:
    print("Arquivo não encontrado ou caminho incorreto.")

validos = []
invalidos = []

for _ in range(8):
    endereco_ip = enderecos_ip.readline()
    endereco_ip = endereco_ip.split()
    for endereco in endereco_ip:
        endereco_dividido = endereco.split(sep=".")
        parte_invalida = 0
        for i in range(len(endereco_dividido)):
            try:
                if int(endereco_dividido[i]) > 255:
                    parte_invalida += 1
            except ValueError:
                print(f"'{endereco_dividido[i]}' não é um valor inteiro.")
                parte_invalida +=1
        if parte_invalida >= 1:
            invalidos.append(endereco)
        else:
            validos.append(endereco)

print("\n=========== Endereços IP: ===========")
print("Válidos: ")
if validos != []:
    for enderecos in validos:
        print(enderecos)
else:
    print("Não foi encontrado nenhum endereço válido.")

print("\nInválidos: ")
if invalidos != []:
    for enderecos in invalidos:
        print(enderecos)
else:
    print("Não foi encontrado nenhum endereço inválido.")
