num = int(input("digite um número: "))
calc = num

for i in range (1, calc):
    calc *= i

print(f'O fatorial de {num} é: {calc}')