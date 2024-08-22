def eh_primo(numero):
  if numero <= 1:
    return False
  if numero % 2 == 0:
    return False
  for i in range(3, int(numero ** 0.5) + 1):
    if numero % i == 0:
      return False
  return True
# print(eh_primo(15)) # Retorna True, pois 7 é primo

num1 = int(input("digite o primeiro número do intervalo de avaliação de números primos: "))
num2 = int(input("digite o último número do intervalo de avaliação de números primos: "))

for i in range(num1, num2):
    if eh_primo(i):
        print(f"{i} é primo")