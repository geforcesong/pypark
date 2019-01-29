# metaclass是类的模板，所以必须从`type`类型派生：

class ListMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaClass ):
    pass

L = MyList()
L.add(1)
print(L)

# No add method in original List class
L0 = list()
#L0.add(1)
print(L0)