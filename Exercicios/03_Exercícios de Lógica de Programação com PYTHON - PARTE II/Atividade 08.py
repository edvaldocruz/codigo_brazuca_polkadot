seq = int(input("digite a qtd de números de fibonacci: "))
n1 = 0
n2 = 1
n3 = None

for i in range(seq):
    if i == 0:
        print(0)
    elif i == 1:
        print(1)
    else:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3)

