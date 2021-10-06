# for with range
lista = ['aa', 'vv', 'rr', 'rr', 'ff', 'hh', 'rr', 'ff', 'rr']

for i in range(len(lista)):
    if lista[i] == 'gg':
        print("gg is at index", i)
        break
else:
    print("not found")

# for for 1 else
