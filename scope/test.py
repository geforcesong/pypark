def f1():
    x = 88

    def f2():
        nonlocal x
        print(x)
        x = 99
    f2()
    print('f1', x)


f1()
