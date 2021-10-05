varx = ['ww', 'hh', 'tt', 'uu', 'pp', 'dd', 'yy', 'ee', 'ss', 'qq']
print("varx =", varx)
print("----")
del varx[4]
print("varx =", varx)
print("----")
del varx[2:6]
print("varx =", varx)
print("----")
varx.clear()
print("varx =", varx)
print("----")
del varx
# error
print("varx =", varx)
