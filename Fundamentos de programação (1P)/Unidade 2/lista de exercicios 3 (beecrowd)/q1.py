tesoura_ganha_de = ["papel", "lagarto"]
papel_ganha_de = ["pedra", "spock"]
pedra_ganha_de = ["lagarto", "tesoura"]
lagarto_ganha_de = ["spock", "papel"]
spock_ganha_de = ["tesoura", "pedra"]

ganhador = []
c = int(input())

def jogo(num_jogadas):
    for i in range(num_jogadas):
        opcao1 = input()
        opcao1 = opcao1.lower()
        opcao2 = input()
        opcao2 = opcao2.lower()

        #empate
        if opcao1 == opcao2:
            ganhador.append("empate")

        #tesoura
        elif opcao1 == "tesoura":
            if opcao2 in tesoura_ganha_de:
                ganhador.append("rajesh")
            else:
                ganhador.append("shelton")

        #papel
        elif opcao1 == "papel":
            if opcao2 in papel_ganha_de:
                ganhador.append("rajesh")
            else:
                ganhador.append("shelton")

        #pedra
        elif opcao1 == "pedra":
            if opcao2 in pedra_ganha_de:
                ganhador.append("rajesh")
            else: 
                ganhador.append("shelton")

        #lagarto
        elif opcao1 == "lagarto":
            if opcao2 in lagarto_ganha_de:
                ganhador.append("rajesh")
            else:
                ganhador.append("shelton")

        #spock
        elif opcao1 == "spock":
            if opcao2 in spock_ganha_de:
                ganhador.append("rajesh")
            else:
                ganhador.append("shelton")

    return ganhador
    
jogo(c)
for i in ganhador:
    print(i)