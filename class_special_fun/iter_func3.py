class Eg2:
    """
    可迭代对象
    """

    def __init__(self, text):
        self.data = text.split(' ')

    def __iter__(self):
        return Eg2Iterator(self.data)


class Eg2Iterator:
    """
    Eg2对象的迭代器
    """

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        try:
            subtext = self.data[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return subtext

    def __iter__(self):
        return self


o2 = Eg2("hello, the wonderful new world!")
for i in o2:
    print(i, end=" | ")
