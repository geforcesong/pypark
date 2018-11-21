class Parent:
    parentAttr = 100

    def __init__(self, name):
        print('调用基类构造函数')
        self.name = name
    
    def parentMethod(self):
        print('调用父类方法')
    
    def setAttr(self, attr):
        Parent.parentAttr = attr
    
    def getAttr(self):
        print("父类属性:", Parent.parentAttr)
        return Parent.parentAttr

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

p = Child('George')
p.childMethod()
print("Name:", p.name)

c= p.getAttr()
print('attr:', c)
