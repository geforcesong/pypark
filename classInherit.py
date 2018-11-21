class Parent:
    parentAttr = 100
    __privateAttr = 120

    def __init__(self, name):
        print('调用基类构造函数')
        self.name = name
        self.__privateAttr = 150
        print(Parent.__privateAttr)
    
    def parentMethod(self):
        print('调用父类方法')
    
    def setAttr(self, attr):
        Parent.parentAttr = attr
    
    def getAttr(self):
        print("父类属性:", Parent.parentAttr)
        return Parent.parentAttr
    
    def getPrivate(self):
        return self.__privateAttr

class Child(Parent):
    def __init__(self, name):
        super(Child, self).__init__(name) #显式调用父类构造函数
        #Parent.__init__(self) #另一种写法
        print('调用子类构造函数')

    def childMethod(self):
        print('调用子类方法', self.parentAttr)

    def getAttr(self):
        #Parent.getAttr(self)
        super(Child, self).getAttr() #较好的写法
        print('覆盖父类方法属性')
        return 200
    
    '''
    Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName（ 对象名._类名__私有属性名 ）访问属性
    def getPrivate(self):
        return self._Parent__privateAttr
    '''

p = Child('George')
p.childMethod()
print("Name:", p.name)

c= p.getAttr()
print('attr:', c)

print('public attr:', p.parentAttr)
print('private attr:', p.getPrivate())

