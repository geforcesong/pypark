class Empty:
    def __init__(self, address):
        self.address = address
        self.age =1

    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError

    def __setattr__(self, attr, value):
        print('__setattr__ called', attr)
        self.__dict__[attr] = value


x = Empty('san mateo')
print(x.age)
print(x.address)
x.haha = 'a'
print(x.haha)
