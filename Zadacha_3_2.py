# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

number = int(input(f"Введите длину списка: "))
listInitial = []
for i in range(number):
    listInitial.append(int(input(f"Введите {i+1} элемент списка: ")))
print("Ваша последовательность: ", listInitial)

numberHalf = int(number/2)
if number % 2 != 0:
    numberHalf = numberHalf + 1

listPar = []
for i in range(numberHalf):
    listPar.append(listInitial[i]*listInitial[number-1-i])
print(f"Список пар чисел списка:", end = " ")
print(listPar)
