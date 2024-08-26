import random

sorteado = random.randint(0, 100)
chute = None

print(sorteado)

while sorteado != chute:
    chute = int(input("digite seu chute: "))
    if sorteado == chute:
        print("Acertou!")
    elif sorteado > chute:
        print(f"O número é maior que {chute}")
    else:
        print(f"O número é menor que {chute}")

    