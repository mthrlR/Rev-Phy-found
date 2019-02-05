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
# list_a = range(-10, 30)
# list_b = []
# for num in list_a:
#     if 0 < num:
#         if num % 3 == 0:
#             if num % 4 > 0:
#                 list_b.append(num)
# print(list_b)
list_a = [i for i in range(-10, 30) if i > 0 and i % 3 == 0 and i % 4 > 0]
print(list_a)
"""

# #NORMAL BLOCK
# name = input('Ur name?')
# surname = input('Ur surname?')
# email = input('Ur email?')

#Task two

import re
pushkin = """
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня."""
pattern = '\.{3}'
result = re.search(pattern, pushkin)
if result:
    print("Patter match found")
else:
    print("Pattern doesn't match")
