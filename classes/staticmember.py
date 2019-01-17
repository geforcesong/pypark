class Student:
    name='Big Student'

    def disp(self):
        print('Instance: %s, Static: %s' % (self.name, Student.name))

s = Student()
s.disp()

s.name = 'George' # instance will overwrite the static member
s.disp()

print(s.name)

del s.name #delet instance member will expose static member again

print(s.name)
s.disp()