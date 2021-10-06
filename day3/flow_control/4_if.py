# nested if
varx = 30
vary = 40
varz = 20

# varx < vary < varz

if varx < vary:
    print("good morning")
    print("hey")
    if varx < varz:
        print("....")
    else:
        pass

elif varx == 30:
    print("namaste")
    print("salaam")
else:
    pass
print("hello")
