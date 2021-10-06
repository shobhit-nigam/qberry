ga = 100

def funca():
    la = 200
    # ga considered as a local object
    ga = 150
    print("ga =", ga)
    print("la =", la)

print("outside ga =", ga)
print("----")
funca()
print("----")
print("outside ga =", ga)
