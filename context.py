name = 'george'


def f1():
    # name = 'jenny'
    print(name)
    # name = 'haha'  #在改变之前没有定义会报错


def f2():
    global name
    name = 'jenny'
    print(name)


f1()
print(name)

print('-----------')
f2()
print(name)


"""
在函数中无法修改作用域外的变量
加入global可以访问外部变量
"""
