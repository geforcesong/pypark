class Animal(object):
    def run(self):
        print('Animal is running ...')

class Dog(Animal):

    def run(self):   #overwrite method in parent class
        print('Dog is running ...')
    
    def runParent(self):
        print('*' * 50)
        print('Dog call parent run method')
        Animal.run(self)

    def runParentSuper(self):
        print('*' * 50)
        super(Dog, self).run()

class Cat(Animal):
    pass

animal = Animal()
dog = Dog()
cat = Cat()

def run(ani):
    ani.run()

run(animal)
run(dog)
run(cat)  #inherite run method from parent class

dog.runParent()
dog.runParentSuper()

print('#' * 50)

print ('Instance check: ', isinstance(dog, Dog) and isinstance(dog, Animal))
print ('Instance check: ', isinstance(dog, Cat))