def boil(data):
    print("boiling", data)

def tadka(data):
    print("adding tadka to", data)

def grill(data):
    print("grilling", data)

def cook(gen, datb):
    gen(datb)

# higher order functions
cook(tadka, "daal")

# tadka("daal")
