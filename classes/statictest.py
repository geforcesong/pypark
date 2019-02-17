class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances += 1

    def printNumInstances():
        print('%s instances created!' % Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)

    def classFunc(cls, x):
        print(cls, x)
    classFunc= classmethod(classFunc)

    @staticmethod
    def easywayStaticFunc():
        print('this is easier way to implement the class static method')

a = Spam()
b = Spam() 
c = Spam()

Spam.printNumInstances()

a.printNumInstances()

class B(Spam): pass

e = B()
e.printNumInstances()

Spam.classFunc(100) # python automatically passed class as 1st parameter
B.classFunc(200)

Spam.easywayStaticFunc()