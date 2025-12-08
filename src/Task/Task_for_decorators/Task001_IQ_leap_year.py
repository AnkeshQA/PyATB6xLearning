# checking for a leap year  , 2024 -- yes
# leap day occur in each year that is a multiple of 4
# except for the evenly divisible by 100 , but not by 400
# the year is multiple of 400
# the year is multiple of 4 and not multiple of 100
from src.Task.Task_for_Functions.Task001_positive_square import result


def check_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

year = 2024
results = check_leap_year(year)
print(f"{year} is a leap year: {results}")
