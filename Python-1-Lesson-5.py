import os
import sys
import shutil

#print('sys.argv = ', sys.argv)
#print('sys.path = ', sys.path)
#print('sys.executable =', sys.executable)
#print('sys.modules = ', sys.modules)
#print('sys.platform = ', sys.platform)

# for path in sys.path:
#     print(path)
#print(os.getcwd())
#print(os.listdir())
#print(1000)

#Easy part
#Task one
"""
# print("Текущая рабочая директория %s" % path)
# print("{}{}".format('Текущая рабочая директория ', os.getcwd()))
# 
# print("{}{}".format('Создана новая директория', os.mkdir('test'))) \\ почему формат не отображает название директории?
# print("{}{}".format('Удалена директория', os.rmdir('test')))
# print("{}{}".format('Созданы новае директории', os.makedirs('1/2/3/4/5/6/7/8')))
# print("{}{}".format('Удалена директория', shutil.rmtree('1')))
print("{}{}".format('Текущая рабочая директория ', os.getcwd()))
os.mkdir('test')
os.chdir('test')
list = ['jan', 'feb', 'march', 'aprl', 'may', 'jun', 'jul', 'aug']
for month in list:
    os.makedirs(month)
print("{}{}".format('Текущая рабочая директория ', os.getcwd()))
shutil.rmtree('test')
"""

#Task two
"""
print("{}{}".format('Текущая рабочая директория ', os.getcwd()))
os.mkdir('test')
os.chdir('test')
list = ['jan', 'feb', 'march', 'aprl', 'may', 'jun', 'jul', 'aug']
for month in list:
    os.makedirs(month)
os.chdir('C:/Users/reverdatto/PycharmProjects/Rev-Phy-found')
print(os.listdir('test'))
#shutil.rmtree('test')
"""
