while (True):
    num_secreto = int(input("diga o número secreto: "))
    if num_secreto < 1 or num_secreto > 100:
        print("número invalido")
        continue
    else:
        break

chute = 0
tentativas = 0
while (chute != num_secreto):
    chute =  int(input("diga seu chute: "))
    tentativas = tentativas + 1
    
    if chute > num_secreto:
        print("muito alto")
    else:
        print("muito baixo") 

print(f"você acertou com {tentativas} tentativas")