# biblioteca para tirar as infos das pastas e sistemas no terminal
import os
os.system("cls")

distancia = float(input("Digite a distância total da viagem: "))
velocidade = float(input("Digite a velocidade média do veiculo: "))
consumo = float(input("Digite o consumo médio de combustível do veiculo: "))
preco = float(input("Digite o preço do litro do combustível: "))

tempo = distancia/velocidade
litros = distancia/consumo
total = litros*preco

print(f"O tempo estimado da viagem é de {tempo:.2f}h. \nA quantidade total de combustível necessário é de {litros:.2f} litros e o custo total estimado é de R$ {total:.2f}")