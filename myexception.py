class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise Networkerror('there is no wifi')
except Networkerror:
    print('wifi error')
finally:
    print('can you try 4G?')