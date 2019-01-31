class Query:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Enter context')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('exc_type=%s, exc_value=%s, traceback=%s' %
              (exc_type, exc_value, traceback))
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


c = Query('gg')
c.query()

print('*' * 50)

with Query('Bob') as q:
    q.query()

print('*' * 50)
print('Too trouble to create extra methods. here is an easier version')
print('using contextmanager')

from contextlib import contextmanager

class QueryA:
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    try:
        q = QueryA(name)
        yield q
    finally:
        print('End QueryA')


with create_query('Mazzy') as q:
    q.query()

print('*' * 50)

#如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：
# from contextlib import closing
# from urllib.request import urlopen

# with closing(urlopen('https://www.google.com')) as page:
#     for line in page:
#         print(line)