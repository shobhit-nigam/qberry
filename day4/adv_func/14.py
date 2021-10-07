lista = ['l', 'e', 't', ' ', 't', 'h', 'e', ' ', 'f',
        'o', 'r', 'c', 'e', ' ', 'b', 'e', ' ', 'w',
        'i', 't', 'h', ' ', 'y', 'o', 'u']

def extract(c):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return c in vowels


listc = list(filter(extract, lista))
print(listc)
