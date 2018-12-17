import copy
students = [
    {
        'name': 's1',
        'room': [12, 13]
    },
    {
        'name': 's2',
        'room': [15, 16]
    }
]
students1 = students[:]
students2 = copy.deepcopy(students)
print(students)
print(students1)
print(students2)

students1[0]['name']= 'ssss'
students1[0]['room'][0]= 8888

print('*'*20)
print(students)
print(students1)
print(students2)

print('#'*20)

print(students)
print(students1)
print(students2)
