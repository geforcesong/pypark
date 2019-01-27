class ThirdClass:
    def __init__(self, value):
        self.data = value

    def __add__(self, value):
        return ThirdClass(self.data + value)

    def __mul__(self, other):
        return ThirdClass(self.data * other)

    def display(self):
        print('current value is:' + self.data)

a = ThirdClass('abc')
a.display()

b = a + 'xyz'
b.display()

c = a * 5
c.display()