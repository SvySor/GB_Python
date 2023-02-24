# Чтение файла

file = open('Seminar_8.txt', 'r', encoding='utf-8')        # r - чтение, w - запись, a - добавление
text = file.read()
print(text)
file.close()
print()


# Чтение файла по строкам

file = open('Seminar_8.txt', 'r', encoding='utf-8')        # r - чтение, w - запись, a - добавление
stroka1 = file.readline()
print(stroka1)
print()
stroka2 = file.readline()
print(stroka2)
file.close()

# Чтение файла по строкам в массив

file = open('Seminar_8.txt', 'r', encoding='utf-8')        # r - чтение, w - запись, a - добавление
stroki = file.readlines()
print(stroki)
file.close()

# Запись файла
with open('Seminar_8_1.txt', 'w', encoding='utf-8') as file:
    file.write('Hello\n')
    file.write('by-by\n')
file.close()

# Запись файла из списка
my_list = ['hello\n','buy\n','goodby\n']
with open('Seminar_8_1.txt', 'w', encoding='utf-8') as file:
    file.writelines(my_list)
file.close()

# Запись чисел из списка
my_list = [1,2, 3, 4, 5]
my_list = list(map(str, my_list))
with open('Seminar_8_1.txt', 'w', encoding='utf-8') as file:
    file.writelines(my_list)
file.close()

print()

import os
import os.path
import shutil

cur_dir = os.getcwd()
print(cur_dir)
list_dir = os.listdir(cur_dir)          #   cur_dir+'/cur_subdir
print(list_dir)
my_list = list(os.walk(cur_dir))
print(my_list)
print()

# Создать телефонный справочник
# 1. Вывод на экран
# 2. Сохранять данные в текстовом файле
# 3. Поиск по имени и фамилии
# 4. Использование функций

# Д/З Дополнить телефонный справочник возможностью изменения данных
# Пользователь так же может ввести имя и фамилию и вы должны реализовать функционал для изменения и удаления данных

