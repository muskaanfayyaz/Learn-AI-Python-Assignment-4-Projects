# Read input from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("That's a leap year!")
        else:
            print("That's not a leap year.")
    else:
        print("That's a leap year!")
else:
    print("That's not a leap year.")
