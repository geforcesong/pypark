def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x)
    return acts


acts = makeActions()

for f in acts:
    print(f(2))

print('*'*30)


def makeActions1():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x) # must retain the value here 
    return acts

acts1 = makeActions1()

for f in acts1:
    print(f(2))