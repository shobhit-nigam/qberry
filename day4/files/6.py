
fa = open("books.txt", "r")
fb = open("new_books.txt", "w")
lista = fa.readlines()

for line in lista:
    if line[0] == 'T':
        fb.write(line)

fa.close()
