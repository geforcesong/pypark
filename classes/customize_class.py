class Student:
    def __init__(self, name):
        self.name = name
        self.scores = [100, 99, 96]
        self.scoreIndex = 0

    # This is print/user string
    def __str__(self):
        return 'Hello %s!' % (self.name)

    # This is debugging string
    #__repr__ = __str__ this is simplified version
    def __repr__(self):
        return 'This is %s' % self.name

    def __iter__(self):
        return self

    def __next__(self):
        if(self.scoreIndex >= len(self.scores)):
            self.scoreIndex = 0
            raise StopIteration()
        self.scoreIndex += 1
        return self.scores[self.scoreIndex-1]

    def __getitem__(self, n):
        if isinstance(n, int):
            if 0 <= n < len(self.scores):
                return self.scores[n]
            return None
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            return self.scores[start: stop]

    def __call__(self):
        print('I am called!!!')

    # def __getattribute__(self, para):
    #     print('__getattribute__ is called')

    # when field is not existed, this function will be called.
    def __getattr__(self, para):
        print('__getatt__ is called')
        if para == 'sex':
            return 'Male'

s = Student('George')
print(s)
for x in s:
    print(x)

print('Score1:', s[1])
print('Non existed score:', s[100])
print('Slice score:', s[0:2])

if(callable(s)):
    s()

print(s.sex)
