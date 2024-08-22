texto = input("escreva uma frase: ")
letra_buscada = "E"

texto_maiusculo = (texto.upper()) # Converte para maiúsculas
texto_sem_letra_buscada = texto_maiusculo.replace("E", "")
qtd_letra_buscada = len(texto_maiusculo) - len(texto_sem_letra_buscada)

print(f'A quantidade de "' + letra_buscada + '" é ' + str(qtd_letra_buscada))