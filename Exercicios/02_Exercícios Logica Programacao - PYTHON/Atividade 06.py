soma = 0
contador = 1
numero = None

print("insira os números que quer somar e insira 0 para ver o resultado")

while numero != "0":
  numero = input(f"digite os {contador}º número: ")
  soma += int(numero)
  contador += 1

print("A soma dos números é:", soma)