frase = input("Digite uma frase: ").lower()
contador = 0
qtd_letras = len(frase)

for i in frase:
    if i in ("a", "e", "i", "o", "u"):
        contador += 1

print(f"A quantidade de vogais é {contador}")