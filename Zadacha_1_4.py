# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

pointX1 = float(input("Input X1 coordinate: "))
pointY1 = float(input("Input Y1 coordinate: "))
pointX2 = float(input("Input X2 coordinate: "))
pointY2 = float(input("Input Y2 coordinate: "))

Distance = ((pointX1-pointX2)**2 + (pointY1-pointY2)**2)**0.5

print(Distance)
