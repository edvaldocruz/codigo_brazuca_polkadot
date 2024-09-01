nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
nota3 = int(input("Digite a nota 3: "))

pes1 = 2
pes2 = 3
pes3 = 5

media_ponderada = (nota1*pes1 + nota2*pes2 + nota3*pes3) / (pes1 + pes2 + pes3)

print(f"A média ponderada é {media_ponderada}")