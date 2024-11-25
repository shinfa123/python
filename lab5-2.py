import datetime
import time

# Get the current date and time using datetime module
current_datetime = datetime.datetime.now()

# a) Current date and time
current_date_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# b) Current year
current_year = current_datetime.year

# c) Month of the year
current_month = current_datetime.strftime("%B")  # Full month name (e.g., January, February)

# d) Week number of the year
week_number = current_datetime.strftime("%U")  # Week number (Sunday as the first day of the week)

# e) Weekday of the week
weekday_name = current_datetime.strftime("%A")  # Full weekday name (e.g., Monday, Tuesday)

# f) Day of the year
day_of_year = current_datetime.strftime("%j")  # Day of the year (1-366)

# g) Day of the month
day_of_month = current_datetime.day

# h) Day of the week using time module
# time.localtime() returns a struct_time object, and we use tm_wday (0 = Monday, 6 = Sunday)
day_of_week_time_module = time.localtime().tm_wday  # 0 = Monday, 6 = Sunday
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_of_week = days_of_week[day_of_week_time_module]

# Display the results
print(f"a) Current Date and Time: {current_date_time}")
print(f"b) Current Year: {current_year}")
print(f"c) Month of the Year: {current_month}")
print(f"d) Week Number of the Year: {week_number}")
print(f"e) Weekday of the Week: {weekday_name}")
print(f"f) Day of the Year: {day_of_year}")
print(f"g) Day of the Month: {day_of_month}")
print(f"h) Day of the Week (using time module): {day_of_week}")

