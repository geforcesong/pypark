import time
import sys

reps = 1000
size = 10000


def tester(func, *args):
    startTime = time.time()
    for i in range(reps):
        func(*args)
    elapse = time.time()-startTime
    return elapse


def forStatement():
    res = []
    for x in range(size):
        res.append(abs(x))


def listComprehesion():
    res = [abs(x) for x in range(size)]


def generatorExpression():
    res = list(abs(x) for x in range(size))


print(sys.version)
tests = (forStatement, listComprehesion, generatorExpression)
for testfun in tests:
    print(testfun.__name__.ljust(20), '=>', tester(testfun))