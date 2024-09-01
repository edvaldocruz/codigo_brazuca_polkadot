numero = 29
lista_divisores = []
soma = 0

for i in range(1,numero):
    if numero % i == 0:
        soma += i

if soma == numero:
    print(f'{numero} é um número perfeito')
else:
    print(f'{numero} não é um número perfeito')

