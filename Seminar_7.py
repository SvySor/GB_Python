# Функции высшего порядка

# Try - exept

from pickle import FALSE


b = 5
c = 0
try:
    a = b / c
except ZeroDivisionError:
    print('На ноль делить нельзя')
    a = 0
print(a)
print()

# Lambda функция

summa = lambda a, b: a**2 + 2*a*b + b*2
print(summa(5,10))
print(type(summa))
print()

# Проверка равенства переменных

proverka = lambda a, b: 'yes' if a == b else 'no'
print(proverka(5,10))
print()

# Вставить одну функцию в другую

def summa(a, b):
    return a + b

def calc(a, b, operation):       # Функция calc - функция высшего порядка. В функцию передаётся переменная
    return operation(a, b)
print(calc(4, 6, summa))
print()

# Функция map()

my_list = ['6','7','3','4','5']
print(my_list)
my_list = list(map(int, my_list))
print(sum(my_list))
print()

my_list = ['6','7','3','4','5']
print(my_list)
my_list = list(map(lambda x: int(x) * 2 + 2, my_list))  # Lambda-Функция: преобразует стрчный тип в int, умножает на 2 и добавляет 2.
print(my_list)
print()

# Преобразование строки введенной с терминала в список целых чисел

print(list(map(int, input().split())))
print()

# Функкия enumerate создаёт кортежи "индекс - элемент"

my_list2 = ['hello', 'buy', 1, 4, 6, 'how are you?']
for i, elem in enumerate(my_list2):
    print(i, elem)
print()

# Функция filter()

my_list_filtered = list(filter(lambda x: x%2 == 0, my_list))      # Фильтрует чётные значения
print(my_list_filtered)
print()

my_list_filtered = list(filter(lambda x: x%10 == 3, my_list))     # Фильтрует значения, заканчивающиеся на 3
print(my_list_filtered)
print()


# Функция zip() объединяет списки в единый список кортежей

a = [1, 2, 3]
b = ['hello', 'hi', 'by']
c = [True, False, True, False]
result_zip = list(zip(a, b, c))
print(result_zip)

# Zadacha 47

