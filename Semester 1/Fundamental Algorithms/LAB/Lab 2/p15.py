# 15. Determine the age of a person in number of days. The current date and the
#     birthdate are known

"""
Desc: Determines the age of a person in number of days
Arguments:
    bd: int, the day of birth
    bm: int, the month of birth
    by: int, the year of birth
    cd: int, the current day
    cm: int, the current month
    cy: int, the current year
Returns:
    integer, the age in days
"""


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def age_in_days(bd, bm, by, cd, cm, cy):
    if cy < by:
        return 0
    elif cy == by and cm < bm:
        return 0
    elif cy == by and cm == bm and cd < bd:
        return 0

    age = 0

    if by != cy:
        if not (bm > 2 or bm == 2 and bd == 29) and is_leap_year(by):
            age = age + 1
        age = age + days[bm - 1] - bd + 1
        bd = 1
        bm = bm + 1
        while bm <= 12:
            age = age + days[bm - 1]
            bm = bm + 1
        bm = 1
        by = by + 1
        while by < cy:
            if is_leap_year(by):
                age = age + 366
            else:
                age = age + 365
            by = by + 1

    # cy == by
    if cm == bm:
        return age + cd - bd + 1
    else:
        if cm > 2 >= bm and is_leap_year(by):
            age = age + 1
        age = age + days[bm - 1] - bd + 1
        bm = bm + 1
        while bm < cm:
            age = age + days[bm - 1]
            bm = bm + 1
        age = age + cd
    return age


birth_day = int(input("Read the day of birth: "))
birth_month = int(input("Read the month of birth: "))
birth_year = int(input("Read the year of birth: "))

current_day = int(input("Read the current day: "))
current_month = int(input("Read the current month: "))
current_year = int(input("Read the current year: "))

print(age_in_days(birth_day, birth_month, birth_year, current_day, current_month, current_year))
