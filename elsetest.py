# 循环后的 else 子句只会在循环没有触发 break 语句, 正常结束的情况下才会执行.
def findExist(l, to_find):
    for num in l:
        if num == to_find:
            print('Exists')
            break
    else:
        print('Does not exist')


some_list = [1, 2, 3, 4, 5]
findExist(some_list, 4)
findExist(some_list, -1)

#try之后的else子句也被称为 "完成子句",因为在 try 语句中到达 else 子句意味着try块实际上已成功完成.
try:
    pass
except:
    print("Exception occurred!!!")
else:
    print("Try block executed successfully...")
