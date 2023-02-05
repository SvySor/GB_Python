# Реализуйте алгоритм перемешивания списка.

from random import randint
numberInt = int(input(f"Input integer number: "))
list_1 = [i for i in range(0+1, numberInt+1)]
print("Исходный список: ",list_1)
for i in range(0, numberInt*100):
    k = randint(0, numberInt-1)
    m = randint(0, numberInt-1)
    temp = list_1[k]
    list_1[k] = list_1[m]
    list_1[m] = temp
print("Перемешанный список: ",list_1)
