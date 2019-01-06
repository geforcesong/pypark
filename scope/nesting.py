def f1():
    x = 99

    def f2():
        def f3():
            nonlocal x
            print('f3', x)
            x = 101
        f3()
    f2()
    print('f1', x)


f1()
