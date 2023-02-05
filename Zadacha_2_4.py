# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
numberInt = int(input(f"Input integer number: "))
list_1 = [randint(-numberInt, numberInt) for i in range(0, numberInt)]
print("Список из N элементов: ",list_1)
f = open('text.txt')
multiple = 1
l = [line.strip() for line in f]
print("Указанные позиции из файла text.txt : ",l)
print("Значения элементов на указанных позициях:", end = " ")
for i in l:
    print(list_1[int(i)], end = ", ")
    multiple *= list_1[int(i)]
print()
print("Произведение элементов на указанных позициях: ", multiple)
f.close()