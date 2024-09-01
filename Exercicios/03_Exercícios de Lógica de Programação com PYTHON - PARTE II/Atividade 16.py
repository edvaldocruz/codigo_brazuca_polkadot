texto = input("escreva um texto: ")
qtd_caracteres = len(texto)
novo_texto = ''

for i in range(qtd_caracteres):
    novo_texto += texto[(qtd_caracteres - 1) - i]

print(novo_texto)

