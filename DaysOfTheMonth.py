days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

month = int(input("Enter month number (1-12): "))

if month in days_in_month:
    if month == 2:
        leap = input("Is it a leap year? (yes/no): ").lower()    # asks the user if the year is a leap year
        if leap == "yes":
            print("February has 29 days.")
        else:
            print("February has 28 days.")
    else:
        print(f"This month has {days_in_month[month]} days.")    # tells the user how many days there are in the month
else:
    print("Invalid month number.")