# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

numberInt = int(input(f"Input integer number: "))
list1 = []
sumList1 = 0
for i in range(numberInt):
    list1.append(((1 + 1 / (i + 1)) ** (i + 1)))
    sumList1 += list1[i]
print(f"Сумма элементов {numberInt} чисел последовательности $(1+\ frac 1 n)^n$ равна {round(sumList1,3)}")
    