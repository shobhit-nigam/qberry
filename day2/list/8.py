# list functions
lista = ['aa', 'vv', 'rr', 'rr', 'ff', 'hh', ['yy', 'tt', '44']]
listnum = [45, 89, 12, 45, 78.65, 34, 64.9]
listb = ['tt','ee', 'ss', 'WW', 'nn', 'cc', 'FF', '20', '45']

print(listb)
# ascii based sorting
listb.reverse()
print(listb)
listb.sort()
print(listb)
listb.sort(reverse=True)
print(listb)

# error
lista.sort()
