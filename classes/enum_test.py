# two ways of using enum
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.Feb, Month.Feb.name, Month.Feb.value)

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

print('*'*60)

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1)

day2 =Weekday['Tue']
print(day2, day2.name, day2.value)

day3 = Weekday(5)
print(day3, day3.name, day3.value)