# from only copy the names, it won't affect the value in another module
from nested1 import X, printer

print(X)
printer()
X=88
print('*'*50)

print(X)
printer()