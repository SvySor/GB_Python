# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def IsSimple(num):
    Check = True
    if num != 1:
        for i in range(2, num):
            if num % i == 0:
                Check = False
    return Check

# number = int(input(f"Введите натуральное число N: "))
number = 100000002
DeviderList = []
inDeviderList = False
if number == 0:
    print("У числа 0 бесконечное количество делителей")
else:
    for i in range(1, number + 1):
        inDeviderList = False
        # print("i ", i)
        for j in range(1, len(DeviderList)):
            # print("j ", j)
            if (i % DeviderList[j] == 0):
                inDeviderList = True
        if inDeviderList == False:
            if number % i == 0:
                if IsSimple(i) == True:
                    DeviderList.append(i)
print("Делители числа N :", DeviderList)