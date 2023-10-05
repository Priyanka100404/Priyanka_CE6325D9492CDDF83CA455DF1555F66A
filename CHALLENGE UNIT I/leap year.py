def is_leap_year(year):
    # Leap year is divisible by 4
    if (year % 4 == 0):
        # Except for years divisible by 100 but not by 400
        if (year % 100 != 0) or (year % 400 == 0):
            return True
    return False

# Input from the user
year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
