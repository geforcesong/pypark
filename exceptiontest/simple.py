class Error100(ValueError):
    pass


try:
    print('try...')
    r = 10/10
    if(r == 1):
        raise Error100('customized error')
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
except Error100 as e:
    print('100 error except:', e)
else:  # will run when no error happens
    print('no errors')
finally:
    print('finally...')
print('END')
