class Employee:
    '员工基类'
    empCount = 0  # 静态变量,通过Employee.empCount 访问

    def __init__(self, name, salary):  # 构造函数
      self.name = name
      self.salary = salary
      Employee.empCount += 1

    def __del__(self):
      print( "类似析构函数~销毁")

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
    


george = Employee('George', 1000)
conjee = Employee('Conjee', 2000)


conjee.displayCount()
conjee.displayEmployee()
george.displayEmployee()

print(hasattr(george, 'name'))
print(hasattr(george, 'age'))
george.age =30
print(hasattr(george, 'age'))


print('-------')
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)


del george
del conjee
print('haha')