weekdayNumber = int(input("Enter weekday number: "))
if 5 < weekdayNumber <= 7:
    print("Weekend")
elif 0 < weekdayNumber <= 5:
    print("Work Day")
else:
    print("The number is not a weekday number")
