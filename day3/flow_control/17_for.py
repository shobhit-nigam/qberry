# for with range
lista = ['aa', 'vv', 'rr', 'rr', 'ff', 'hh', 'rr', 'ff', 'rr']

listx = []

for i in range(len(lista)):
    if lista[i] == 'rr':
        print("rr is at index", i)
        listx.append(i)
        if len(listx) == 3:
            break

print(listx)
