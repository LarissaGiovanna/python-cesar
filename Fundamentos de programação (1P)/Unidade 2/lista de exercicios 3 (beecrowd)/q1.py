tesoura_ganha_de = ["papel", "lagarto"]
papel_ganha_de = ["pedra", "spock"]
pedra_ganha_de = ["lagarto", "tesoura"]
lagarto_ganha_de = ["spock", "papel"]
spock_ganha_de = ["tesoura", "pedra"]

ganhador = []
c = int(input())

opcao = []


def jogo(num_jogadas):
    for _ in range(num_jogadas):
        opcao.append(input().strip().split())

    for i in range(num_jogadas):
        # empate
        if opcao[i][0] == opcao[i][1]:
            ganhador.append("empate")
        # tesoura
        elif opcao[i][1] in tesoura_ganha_de and opcao[i][0] == "tesoura":
            ganhador.append("rajesh")
        # papel
        elif opcao[i][1] in papel_ganha_de and opcao[i][0] == "papel":
            ganhador.append("rajesh")
        # pedra
        elif opcao[i][1] in pedra_ganha_de and opcao[i][0] == "pedra":
            ganhador.append("rajesh")
        # lagarto
        elif opcao[i][1] in lagarto_ganha_de and opcao[i][0] == "lagarto":
            ganhador.append("rajesh")
        # spock
        elif opcao[i][1] in spock_ganha_de and opcao[i][0] == "spock":
            ganhador.append("rajesh")
        else:
            ganhador.append("sheldon")

    return ganhador


jogo(c)
for i in ganhador:
    print(i)
