import os
import sys
import shutil

# print('sys.argv = ', sys.argv)
# print('sys.path = ', sys.path)
# print('sys.executable =', sys.executable)
# print('sys.modules = ', sys.modules)
# print('sys.platform = ', sys.platform)

# for path in sys.path:
#     print(path)
# print(os.getcwd())
# print(os.listdir())
# print(1000)

# Easy part
# Task one
"""
# print("Текущая рабочая директория %s" % path)
# print("{}{}".format('Текущая рабочая директория ', os.getcwd()))
# 
# print("{}{}".format('Создана новая директория', os.mkdir('test'))) ## почему формат не отображает название директории?
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

# Task two
"""
os.mkdir('test')
os.chdir('test')
clndr = ['jan', 'feb', 'march', 'aprl', 'may', 'jun', 'jul', 'aug']
for month in clndr:
    os.makedirs(month)
print("{}{}".format('Текущая рабочая директория ', os.getcwd()))
os.chdir('C:/Users/Reverdatto/pycharmProjects/Rev-Phy-found')
print("{}{}{}{}".format('Текущая рабочая директория: ', os.getcwd(), '. Список директорий: ', os.listdir('test')))
#print(os.listdir('test'))
# shutil.rmtree('test')
"""
# Task three
"""
shutil.copy2('Python-1-Lesson-5.py', 'new_py.py')
"""

# DZ
print('sys.argv = ', sys.argv)
def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

do = {
    "help": print_help,
    "mkdir": make_dir,
}
try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None
try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
