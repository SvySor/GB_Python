# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
#- x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


correctInput = False
while correctInput == False:
    pointX = float(input("Input X coordinate: "))
    pointY = float(input("Input Y coordinate: "))
    if pointX == 0 or pointY == 0:
        print("Enter ones more time correct coordinates")
    else:
        correctInput = True
print(f"Great, your point is: {pointX}, {pointY}")
quarterNumber = 4
if pointX > 0 and pointY > 0:
    quarterNumber = 1
elif pointX > 0 and pointY < 0:
    quarterNumber = 2
elif pointX < 0 and pointY < 0:
    quarterNumber = 3
print(f"Your point locate in {quarterNumber} quarter")