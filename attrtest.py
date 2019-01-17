class MyObject:
    def __init__(self):
        self.x =9
    
    def power(self):
        return self.x * self.x

obj = MyObject()

print("hasattr(obj, 'x'): ", hasattr(obj, 'x'))
print("hasattr(obj, 'y'): ", hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print("hasattr(obj, 'y'): ", hasattr(obj, 'y'))
print('obj.y:', obj.y)
print("getattr(obj, 'y'):", getattr(obj, 'y'))

print("getattr(obj, 'z'):", getattr(obj, 'z', 100)) # will raise an error if fetch non-existed field unless set default, e.g. 100 here


fn = getattr(obj, 'power')

print(fn())