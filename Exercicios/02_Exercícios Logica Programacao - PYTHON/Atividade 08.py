def avalia_par_impar(num):
  if num % 2 == 0:
    print("O número " + str(num) + " é par")
  else:
    print("O número " + str(num) + " é impar")

numero = int(input("Digite um número para avaliar: "))

avalia_par_impar(numero) # Chama a função saudacao com o argumento "Maria"