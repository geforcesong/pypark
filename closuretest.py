def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


for f in count():
    print(f())

print('*'*50)


def count1():
    fs = []
    for i in range(1, 4):
        def f(t=i):
            return t * t
        fs.append(f)
    return fs


for f in count1():
    print(f())


def createCounter():
    total =0
    def counter():
        nonlocal total
        total += 1
        return total
    return counter

cter = createCounter()
print(cter())
print(cter())
print(cter())
print(cter())