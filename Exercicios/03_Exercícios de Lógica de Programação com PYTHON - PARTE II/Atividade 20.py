num = 0
lista = []

while num != -1:
    num = int(input("digite seus números e -1 para finalizar e calcular: "))
    if num != -1:
        lista.append(num)

maximo = max(lista)
minimo = min(lista)
media = sum(lista) / len(lista)

print(f'''
    media: {media} \n 
    maximo: {maximo} \n
    minimo: {minimo} \n
    ''')
