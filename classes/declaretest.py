class Student:

    def __init__(self, name, score, sex):
        self.name = name
        self.score = score
        self.__sex = sex #private member

    def display(self):
        print("name: %s, score: %s, grade: %s, sex: %s" % (self.name, self.score, self.getGrade(), self.__sex))

    def getGrade(self):
        if(self.score > 90):
            return 'A'
        return 'B'


s1 = Student("George", 100, 'Male')
s1.display()
s1.score = 30
s1.display()
s1._Student__sex = 'female' # force to access privte member
s1.display()
