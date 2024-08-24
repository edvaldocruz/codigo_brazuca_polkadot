palavra = "matamr"
count = 1
palindromo = None

qtd_letras = len(palavra)

if qtd_letras % 2 == 0:
    limit_count = qtd_letras / 2
else:
    limit_count = (qtd_letras - 1) / 2

while count <= limit_count:
    if palavra[count - 1] == palavra[(-1)*count]:
        palindromo = True
        count += 1
    else:
        palindromo = False
        break

# print(polindromo)
if palindromo == True:
    print(f'A palavra "{palavra}" é um palindromo')
else:
    print(f'A palavra "{palavra}" não é um palindromo')
    
