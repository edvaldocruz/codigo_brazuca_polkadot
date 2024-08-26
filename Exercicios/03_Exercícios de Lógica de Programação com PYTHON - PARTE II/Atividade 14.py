num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
operacao = input("digite a operação desejada (soma, subtração, divisão, multiplicação): ")
resultado = 0

if operacao == "soma":
    resultado = num1 + num2
elif operacao == "subtração":
    resultado = num1 - num2
elif operacao == "divisão":
    resultado = num1 / num2
elif operacao == "multiplicação":
    resultado = num1 * num2
else:
    print("verifique texto digitado")

print(resultado)