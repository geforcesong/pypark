from types import MethodType

def set_sex(self, sex):
    self.sex = sex


class Student:
    __slots__=('name','age','set_sex','sex')

stu = Student()
stu.name = 'George'
stu.age = 90

print(stu.name, stu.age)


#can't run the following codes, because they are not in slots
# stu.score =100
# print(stu.score)

stu.set_sex = MethodType(set_sex, stu) #dynamic add method
stu.set_sex('male')
print(stu.sex)