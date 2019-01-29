# Task one
"""
import math
a = [2, -5, 8, 9, -25]
result = []
for val in a:
    if val >=0
        root_num = math.sqrt(val)

        if root_num == int(root_num):
            result.append(int(root_num))
print(result)
"""
# Task two
"""
day_list = ['', 'первое', 'второе', 'третье', 'четвёртое',
                'пятое', 'шестое', 'седьмое', 'восьмое',
                'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
                'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
                'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
                'двадцать первое', 'двадцать второе', 'двадцать третье',
                'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
                'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
                'тридцатое', 'тридцать первое']
month_list = ['', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
date = '02.11.2013'
day, month, year = date.split('.')
day = int(day)
month = int(month)
year = int(year)
print(days[day], months[month], year, 'года')
"""
#Task three
"""
import random
elem_count = int(input('Введите количества элемнтов'))
i = 0
rand_list = []
while i <elem_count:
    rand_list.append(random.randint(-100, 100))
    i += 1

#for _ in range (elem_count):
#    rand_list.append(random.randint(-100, 100))
#print(rand_list)
"""
#Task four
"""
a = [1, 2, 4, 5, 6, 2, 5, 2]
first_a = list(set(a))
print(first_a)

second_a = []
for elem in a:
    if a.count(elem) == 1:
        second_a.append(elem)
print(second_a)
"""