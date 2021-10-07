# do not use id() in programming
# interned objects

varx = 30
vary = 33
varz = 30

print(id(varx))
print(id(vary))
print(id(varz))

varz = 34
print(id(varz))
