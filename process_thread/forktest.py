import os

print('process (%s) start ...' % os.getpid())

pid = os.fork()

print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
