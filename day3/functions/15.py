def funca (la, lb, *args, **kwargs):
    print("la =", la)
    print("lb =", lb)
    print("args =", args)
    print("kwargs =", kwargs)
    print("-----")
    for k, v in kwargs.items():
        print("k =", k)
        print("v =", v)
    return args, kwargs

ta, da = funca(100, 200, 300, 400, 500, norway='oslo', india='new delhi')
