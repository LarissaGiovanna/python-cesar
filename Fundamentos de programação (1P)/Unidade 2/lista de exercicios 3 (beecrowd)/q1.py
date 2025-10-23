c = int(input())
opcao1 = input()
opcao2 = input()

def verificar_ganhador(num_jogadas, opcao1, opcao2):
    ganhador = ""
    opcao1 = opcao1.lower()
    opcao2 = opcao2.lower()
    for i in range(num_jogadas):

        #tesoura e papel
        if opcao1 == "tesoura" and opcao2 == "papel":
            ganhador = "jogador 1"
        elif opcao1 == "papel" and opcao2 == "tesoura":
            ganhador = "jogador 2"

        #papel e pedra
        elif opcao1 == "papel" and opcao2 == "pedra":
            ganhador = "jogador 1"
        elif opcao1 == "pedra" and opcao2 == "papel":
            ganhador = "jogador 2"

        #pedra e lagarto
        elif opcao1 == "pedra" and opcao2 == "lagarto":
            ganhador = "jogador 1"
        elif opcao1 == "lagarto" and opcao2 == "pedra":
            ganhador = "jogador 2"

        #lagarto e spock
        elif opcao1 == "lagarto" and opcao2 == "spock":
            