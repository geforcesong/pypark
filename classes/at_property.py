# getScore works but not easy to assess as age, have to call get method for value

class Student:
    def getScore(self):
        return self._score

    def setScore(self, score):
        if not 0 < score < 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = score

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if not 15 <= age <= 30:
            raise ValueError('age must between 15 ~ 30!')
        self._age = age


s = Student()
s.setScore(11)

print(s.getScore())

s.age = 18
print(s.age)
