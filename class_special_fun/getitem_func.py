class stepper:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, i):
        return self.data[i]

x=stepper('Spam')
print(x[1])


for item in x:
    print(item)

print()
print('p' in x)

print([c for c in x])
print(map(None, x))