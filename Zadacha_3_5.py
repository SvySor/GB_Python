# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

number = int(input(f"Введите целое число больше нуля: "))
listFibo = []
listFiboNeg = []
if number == 0:
    listFibo = [0, ]
elif abs(number) == 1:
    listFibo = [1, 0, 1]
else:
    listFibo = [0, 1]
    listFiboNeg = [1, ]
    for i in range(2, number+1):
        positiveF = listFibo[i-1] + listFibo[i-2]
        negativeF = ((- 1) ** (i + 1)) * positiveF
        listFibo.append(positiveF)
        listFiboNeg.insert(0, negativeF)
listFibo = listFiboNeg + listFibo
print("Список чисел Фибоначчи для вашего числа:", listFibo)