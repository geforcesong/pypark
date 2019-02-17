class A:
    attr =1

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

x=D()
print(x.attr)
