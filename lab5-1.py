import calendar

def is_leap_year(year):
    return calendar.isleap(year)

# Input: Year from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

