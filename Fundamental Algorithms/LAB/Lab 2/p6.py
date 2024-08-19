# 6. Given the current date (day, month, year) and the birthdate of a person (day, month, year),
#    compute the age of the person in number of years.

"""
Desc: Determines the age of a person in number of years
Arguments:
    bd: int, the day of birth
    bm: int, the month of birth
    by: int, the year of birth
    cd: int, the current day
    cm: int, the current month
    cy: int, the current year
Returns:
    integer, the age in years
"""


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def age_in_years(bd, bm, by, cd, cm, cy):
    if cy < by:
        return 0
    elif cy == by and cm < bm:
        return 0
    elif cy == by and cm == bm and cd < bd:
        return 0

    age = 0
    while by < cy:
        age += 1
        by += 1
    if cm < bm or (cm == bm and cd < bd):
        age -= 1

    return age


birth_day = int(input("Read the day of birth: "))
birth_month = int(input("Read the month of birth: "))
birth_year = int(input("Read the year of birth: "))

current_day = int(input("Read the current day: "))
current_month = int(input("Read the current month: "))
current_year = int(input("Read the current year: "))

print(age_in_years(birth_day, birth_month, birth_year, current_day, current_month, current_year))