# Сформировать список элементов, не повторяющихся во втором списке.
# Оптимицация через удаление дублей во втором цикле.

a = [3, 1, 3, 4, 2, 4, 12]
b = [4, 15, 43, 1, 15, 1]
b = set(b)
new = []
for elem in a:
        if elem not in b:
                new.append(elem)
print(new)

# Счёт к-ва элементов, которые больше своих соседей

my_list = [1, 2, 3, 4, 5, 1, 5, 1]
count = 0
for i in range( 1, len(my_list) - 1):
        if my_list[i-1] < my_list[i] > my_list[i+1]:
            count += 1
print(count)


# Цикл попарного сравнения

count = 0
for i in range(len(a) - 1):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            count += 1
print(count)