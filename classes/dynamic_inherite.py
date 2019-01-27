class rec: pass

rec.name='Bob'
rec.age = 40


print(rec.name)

x=rec()
y=rec()

print(x.name, y.name)
x.name = 'Sue'
print(x.name, y.name)

print(rec.__dict__.keys())
print(x.__dict__.keys())
print(y.__dict__.keys())

def upperName(self):
    return self.name.upper()

rec.method = upperName

print(x.method())
print(y.method())
print(rec.method(x))