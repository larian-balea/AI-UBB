# 2. Determine a date (as day, month, year) starting from two integer numbers that
#    represent the year and the number of the day in that year

"""
Desc: Determines the date starting from the year and the day in that year
Arguments:
    year: int
    day: int
Returns:
    integer, the date
"""


def is_leap_year(y):
    if y % 400 == 0:
        return True
    if y % 4 == 0 and y % 100 != 0:
        return True
    return False


days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = input('Read year: ')
day = input('Read day: ')

if is_leap_year(int(year)):
    days[1] = 29

for i in range(12):
    if int(day) <= days[i]:
        print(day, i+1, year)
        break
    day = int(day) - days[i]
