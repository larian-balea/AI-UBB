# 8. Consider an integer number 𝒏. Print the nearest prime number to 𝒏.

"""
Desc: Print the nearest prime number to n
Arguments:
    n: integer, the number
Returns:
    integer, the nearest prime number to n
"""


def is_prime(num):
    if num < 2:
        return False
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True


n = int(input("Read n: "))

if is_prime(n):
    print(n)
else:
    i = 1
    ok = True
    while ok:
        if is_prime(n - i):
            print(n - i)
            ok = False
        if is_prime(n + i):
            print(n + i)
            ok = False
        i += 1
