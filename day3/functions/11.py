def funca (la=55, lb=77, lc=66):
    return la+lb, la+lc, "hey", [la, lb, lc]

u, v, w, x = funca(100, 22, 10)
print("u =", u)
print("v =", v)
print("w =", w)
print("x =", x)

u = funca(100, 22, 10)
print("u =", u)

# error
u, v = funca(100, 22, 10)
