# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

numberString = input(f"Input real number: ")
numberFloat = float(numberString)
sum = 0
for i in str(numberFloat):
    checkDigit = (i != "." and i != "-")
    if checkDigit == True:
        sum += int(i)
print(f"The sum of digits is: = {sum}")