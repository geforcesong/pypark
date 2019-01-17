from types import MethodType

def set_age(self, age):
    self.age = age

def set_score(self, score):
    self.score = score

class Student:
    pass

Student.set_score = set_score #this can be applied to all 

stu = Student()
stu.name = 'George'
stu.set_age = MethodType(set_age, stu) #dynamic add method
print(stu.name)
stu.set_age(10)
print(stu.age)
stu.set_score(100)
print(stu.score)

# dynamic added member can't be used at all instances
stu2 = Student()
# stu2.set_age(100)
stu2.set_score(199)
print(stu2.score)

