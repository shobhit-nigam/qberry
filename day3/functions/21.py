def boil(data):
    print("boiling", data)

def tadka(data):
    print("adding tadka to", data)

def grill(data):
    print("grilling", data)

def owen(data):
    print(data, "heating in owen")

def cook(gen, datb):
    gen(datb)

def bake(gen, datb):
    gen(datb)

def make(gen, fun, datc):
    gen(fun, datc)

make(cook, tadka, "daal")
# cook(tadka, "daal")
# tadka("daal")
