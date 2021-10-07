lista = [20, 10, 5, 4, 6, 8]
listb = [3, 8, 15, 6, 12, 9]
tc = (2, 4, 6, 8, 10, 12)

def calculate(a, b, c):
    return (a+b) * (a+c)

listc = list(map(calculate, lista, listb, tc))
print(listc)
