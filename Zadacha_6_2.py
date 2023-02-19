# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

min = 12
max = 23
my_list = [12, 22, 32, 11, 15, 11, 52, 11]


index_list = []
for i in range(len(my_list)):
        if min <= my_list[i] <= max:
            index_list.append(i)
print(my_list)
print(index_list)