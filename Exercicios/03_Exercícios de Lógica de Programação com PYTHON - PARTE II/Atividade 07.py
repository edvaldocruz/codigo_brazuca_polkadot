l_notas = []
contador = 1
nota = None
soma = 0

while nota != -1:
    nota = int(input(f'Digite a nota {contador} e digite -1 para encerrar: '))
    if nota != -1:
        l_notas.append(nota)
        contador += 1

for i in l_notas:
    soma += i

media = soma/len(l_notas)

print("media notas: " + media )