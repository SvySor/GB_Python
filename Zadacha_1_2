#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

numberX = int(input("Enter X: "))
numberY = int(input("Enter Y: "))
numberZ = int(input("Enter Z: "))

leftValue = not (numberX or numberY or numberZ)
rightValue = not numberX and not numberY and not numberZ
checkResult = leftValue == rightValue
if checkResult == True:
    print("Statement is correct")
else:
    print("Statement of false")
