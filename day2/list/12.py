# list functions
# refernces
lista = ['tt','ee', 'ss', 'nn', 'cc']
listb = ['gg', 'mm', 'xx', lista.copy(), 'rr', 'yy']

listx = lista.copy()

print("lista =", lista)
print("listb =", listb)
print("listx =", listx)
print("------")
lista.sort()
lista[2] = 'qq'
lista.insert(1, 'oo')
lista.reverse()
print("lista =", lista)
print("listb =", listb)
print("listx =", listx)
