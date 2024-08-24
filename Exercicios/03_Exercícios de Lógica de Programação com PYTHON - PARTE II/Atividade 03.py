massa = int(input("Qual seu peso (Kg): "))
altura = float(input("Qual sua altura (m): "))

imc = massa / (altura ** 2)

print(f"seu imc é {imc}")