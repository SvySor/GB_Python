# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_element = int(input(f"Введите первый элемент массива: "))
delta = int(input(f"Введите разность: "))
quantity = int(input(f"Введите количество элементов: "))

# Через цикл for

progression = []
for i in range(quantity):
    progression.append(first_element + i * delta)
print(progression)

# Через list comprehension

progression = [(first_element + i * delta) for i in range(quantity)]
print(progression)


# Использование List Comprehensions
# List comprehensions — это третий способ составления списков. При таком элегантном подходе мы можем переписать цикл for из первого примера всего в одну строку кода:

# >>> squares = [i * i for i in range(10)]
# >>> squares
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Вместо того, чтобы создавать пустой список и добавлять каждый элемент в конец, мы просто определяем список и его содержимое одновременно, следуя этому формату:

# new_list = [expression for member in iterable]

# Каждое представление списков в Python включает три элемента:

# expression какое либо вычисление, вызов метода или любое другое допустимое выражение, которое возвращает значение. В приведенном выше примере выражение i * i является квадратом значения члена.
# member является объектом или значением в списке или итерируемым объекте (iterable). В приведенном выше примере значением элемента является i.
# iterable список, множество, последовательность, генератор или любой другой объект, который может возвращать свои элементы по одному. В приведенном выше примере iterable является range(10).