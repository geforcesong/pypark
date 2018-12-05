funcs = []
for x in range(7):
    d = x*10
    def some_func(x=x, d=d):
        print(d)
        return x
    funcs.append(some_func)

print([func() for func in funcs])