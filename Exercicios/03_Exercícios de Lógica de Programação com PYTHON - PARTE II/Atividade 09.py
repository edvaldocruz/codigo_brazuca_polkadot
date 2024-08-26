num1 = 0
num2 = 2
num3 = 1

lista = [num1, num2, num3]

menor = min(lista)
maior = max(lista)

lista.remove(menor)
lista.remove(maior)

print(menor)
print(lista[0])
print(maior)




# if num1 > num2:
#     if num2 > num3:
#         print(f'{num3}, {num2}, {num1}')
#     else:
#         print(f'{num2}, {num3}, {num1}')
# elif 
#     if num2 > num3:
#         print(f'{num3}, {num2}, {num1}')
#     else:
#         print(f'{num2}, {num3}, {num1}')