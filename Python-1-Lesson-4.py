#EASY BLOCK
#Task one
"""
def qube(x):
    return x*x

points = [i for i in range(10)]
for num in points:
    print(qube(num))

#print(map(lambda x: x*x, points)) - так и не понял почему не работает
"""
#Task two
"""
first = ['avocado', 'banana', 'blackberry', 'cranberry', 'lemon']
second = ['mango', 'lemon', 'gooseberry', 'pear', 'banana']
third = []
for a in first:
    for b in second:
        if a == b:
            third.append(a)
print(third)
"""
#Task three
"""
list_a = range(-10, 30)
list_b = []
for num in list_a:
    if 0 < num:
        if num % 3 == 0:
            if num % 4 > 0:
                list_b.append(num)
print(list_b)
"""

#NORMAL BLOCK
name = input('Ur name?')
surname = input('Ur surname?')
email = input('Ur email?')
