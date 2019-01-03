def okfun():
    print('step1')
    yield 1
    print('step2')
    yield 2
    print('step3')
    yield 3
    return 'Finished'


for i in okfun():
    print('value', i)

print('*'*30)

g = okfun()
while(True):
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator Value:', e.value)
        break
