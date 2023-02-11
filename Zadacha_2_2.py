# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


numberInt = int(input(f"Input integer number: "))
my_list = []
factorialI = 1
for i in range(1, numberInt+1):
    factorialI *= i
    my_list.append(factorialI)
    print(factorialI, end=' ')
print()
print(my_list)