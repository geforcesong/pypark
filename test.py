# b=2

def external():
    b = 100

    def internal():
        nonlocal b
        print(b)
        b = 300
        return b
    internal()
    print(b)


external()
print(b)
