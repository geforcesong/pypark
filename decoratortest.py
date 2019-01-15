import time

def simple(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log(text, num):
    def decorator(func):
        def wrapper(*args, **kw):
            print('call (%s, %s) %s():' % (text, num, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

def perf(func):
    def wrapper(*args, **kw):
        startTime = time.time()
        ret = func(*args, **kw)
        print ('total is:', time.time() -  startTime)
        return ret
    return wrapper

@perf
@simple
@log('12312', 456)
def is_odd(n):
    return n % 2 == 1


# @simple
# def is_odd(n):
#     return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))


print(L)
