itens = []
item = ""

while item != "sair":
    item = input('Adicione um item ou digite "sair" para encerrar: ')
    # print(item)
    if item != "sair":
        itens.append(item)

print("Itens da lista: ")
for i in itens:
    print(i)