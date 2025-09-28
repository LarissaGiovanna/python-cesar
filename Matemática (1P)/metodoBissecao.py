#testes
    #x**3 + math.sin(x) [-1, 1]
    #x**2 + 2 [0, 1]
    #x**2 - math.cos(x) [0.5, 1]
    #(x/2)**2 + sin(x) [-2, -1]
    #3*x**4 - x + 3 [5, 1]
    #math.sin(x) + math.cos(x) - (3/x) [-2, -3]

from matplotlib import pyplot as mpl
import numpy
import math
funcao = "x**2 - math.cos(x)" #pessoa digita a função
intervalo = [0.5, 1] #pessoa digita um intervalo(array)

a = intervalo[0]
b = intervalo[1]
parada = 0.01

tentativasX =[]
tentativasY = []

print(f"Intervalo: {intervalo}")
print(f"Critério de parada: {parada}")
print(f"Função: {funcao}")

#função para calcular a imagem
def calcularImagem(x):
    y = x**2 - math.cos(x)
    return y

#calcular a média dos pontos
def mediaPontos(a, b):
    media = (a+b)/2
    return media

#comparar os pontos e saber qual deve ser substituido
def comparacaoPontos(a, b, xMedio):
    if calcularImagem(a) > 0 and calcularImagem(b) < 0 and calcularImagem(xMedio) > 0 or calcularImagem(a) < 0 and calcularImagem(b) > 0 and calcularImagem(xMedio) < 0:
        print(f"f(a) = {calcularImagem(a)}")
        print(f"f(b) = {calcularImagem(b)}")
        print(f"f(xMedio) = {calcularImagem(xMedio)}")

        a = xMedio
        print("O ponto 'a' foi substituido\n")

        resultado = ["a", a]
        tentativasX.append(a)
        tentativasY.append(calcularImagem(a))
        return resultado
    
    elif calcularImagem (a) < 0 and calcularImagem(b) > 0 and calcularImagem(xMedio) > 0 or calcularImagem(a) > 0 and calcularImagem(b) < 0 and calcularImagem(xMedio) < 0:
        print(f"f(a) = {calcularImagem(a)}")
        print(f"f(b) = {calcularImagem(b)}")
        print(f"f(xMedio) = {calcularImagem(xMedio)}")

        b = xMedio
        print("O ponto 'b' foi substituido\n")

        resultado = ["b", b]
        tentativasX.append(b)
        tentativasY.append(calcularImagem(b))
        return resultado
    
    else:
        resultado = "Não foi possivel achar uma raíz real nesse intervalo"
        return resultado

#calcular o módulo
def modulo(x):
    moduloX = x 
    if moduloX < 0: 
        moduloX = moduloX * (-1) # se x der negativo, multiplica por -1 e o valor fica positivo
    return moduloX 

#looping
while (True):
    print(f"a = {a}")
    print(f"b = {b}")
    #calcular a média dos intervalos
    xMedio = mediaPontos(a, b)
    print(f"xMédio = {xMedio}")

    #imagem da media
    ImagemXMedio = calcularImagem(xMedio)

    #calcular modulo da imagem
    moduloImagem = modulo(ImagemXMedio)

    #verificação do critério de parada
    if moduloImagem > parada:
        print(f"|f(xMedio)| não atingiu o critério de parada (<= {parada})")
        comparacao = comparacaoPontos(a, b, xMedio)
        if comparacao[0] == "a": 
            a = comparacao[1] #substituição do novo a
        elif comparacao[0] == "b":
            b = comparacao[1] #novo b
        else:
            print(f"{comparacao}")
            xMedio = None
            break
    else:
        print(f"f(xMedio) = {calcularImagem(xMedio)}")
        print(f"|f(xMedio)| atingiu o critério de parada (<= {parada})")
        print(f"Raíz encontrada: {xMedio}")
        break #se atingir o criterio de parada, encerrra

#grafico
opcao = input("Quer o gráfico? (s/n) ")
if opcao == 's':
    x = numpy.linspace(intervalo[0], intervalo[1], 1000) #definição do eixo x
    y = x**2 - numpy.cos(x) #funcao que determina o y
    fig, axe = mpl.subplots(figsize=(7, 4)) #tamanho da figura
    axe.plot([intervalo[0],intervalo[1]], [0,0], color="gray") #linha que passa pelo eixo x

    #formatação/estilo do grafico
    for i in range(len(tentativasX)):
        axe.plot([tentativasX[i], tentativasX[i]], [0, tentativasY[i]], color="gray", linestyle="--") #linha tracejada vertical do x pro y
        axe.plot(tentativasX[i], tentativasY[i], marker="o", color="gray") #bolinha pra marcar o ponto

        #formatação do texto
        if tentativasX[i] > 0:
            axe.text(tentativasX[i], -0.05, f"{i+1}ºx = {tentativasX[i]}", fontsize="7")
        else:
            axe.text(tentativasX[i], 0.01, f"{i+1}ºx = {tentativasX[i]}", fontsize="7")

    #se tiver xMedio/for encontrado uma raiz
    if type(xMedio) is float or type(xMedio) is int:
        axe.plot([xMedio, xMedio], [0, calcularImagem(xMedio)]) #linha verical da raiz encontrada
        axe.plot(xMedio, calcularImagem(xMedio), marker="o", color="blue") #bolinha

        #formatação de texto
        if xMedio > 0:
            axe.text(xMedio, -0.05, f"{len(tentativasX)+1}ºx = {xMedio}", fontsize="7", color="blue")
        else:
            axe.text(xMedio, 0.01, f"{len(tentativasX)+1}ºx = {xMedio}", fontsize="7", color="blue")

    axe.plot(x, y) #criar o grafico
    mpl.show() #mostrar o grafico
else:
    print("ok")