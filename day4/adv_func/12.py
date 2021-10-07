lista = [20, 10, 5, 4, 6, 8]
listb = [3, 8, 15, 6, 12, 9]

def add(a, b):
    return a+b

listc = list(map(add, lista, listb))
print(listc)
