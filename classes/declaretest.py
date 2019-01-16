class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display(self):
        print("name: %s, score: %s, grade: %s" % (self.name, self.score, self.getGrade()))

    def getGrade(self):
        if(self.score > 90):
            return 'A'
        return 'B'


s1 = Student("George", 100)
s1.display()
    