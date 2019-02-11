class Person:

    def say(self, name):
        print('Hello', name)


c= Person()
c.say('GG')

Person.say(c, 'MM')


d = eval('Person()')
d.say('D.D')