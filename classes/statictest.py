class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances += 1

    def printNumInstances():
        print('%s instances created!' % Spam.numInstances)

    printNumInstances = staticmethod(printNumInstances)

a = Spam()
b = Spam() 
c = Spam()

Spam.printNumInstances()

a.printNumInstances()

class B(Spam): pass

e = B()
e.printNumInstances()