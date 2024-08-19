# 17. A number 𝒏 is special if there is a natural number 𝒎 such that 𝑛 = 𝑚 + 𝑆(𝑚)
#     where 𝑆(𝑚) is the sum of digits of 𝒎. Verify if a given number is special.

"""
Desc: Verifies if a given number is special
Arguments:
    n: integer, the number
Returns:
    boolean, True if the number is special
             False otherwise
"""


def sum_of_digits(m):
    return sum(int(digit) for digit in str(m))


def is_special(n):
    # Iterate over possible values of m
    lower_bound = max(1, n - 9 * (len(str(n)) - 1))
    for m in range(lower_bound, n):
        if m + sum_of_digits(m) == n:
            return True
    return False


number = int(input('Read n: '))

if is_special(number):
    print('The number is special')
else:
    print('The number is not special')
