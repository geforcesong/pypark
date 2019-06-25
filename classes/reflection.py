def foo(): pass

class Cat:
    def __init__(self, name= 'kitty'):
        self.name = name

    def sayHi(self):
        print(self.name)

cat = Cat();

cat.sayHi()

if hasattr(cat, 'name'):
    setattr(cat, 'name', 'tiger')

cat.sayHi()

print(Cat.__doc__)
print(Cat.__name__)
print(Cat.__module__)
print(Cat.__bases__)
print(Cat.__dict__)
print(cat.__class__ == Cat)