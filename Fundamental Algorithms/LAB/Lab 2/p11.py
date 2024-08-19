# 11. Generate all prime numbers having n digits with the property that all its
#     prefixes are also prime.

"""
Desc: Print all prime numbers having n digits with the property that all its prefixes are also prime
Arguments:
    n: integer, the number of digits
Returns:
    integers, prime numbers with the property that all its prefixes are also prime
"""


def is_prime(num):
    if num < 2:
        return False
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True


n = int(input("Read n: "))
result = []
for i in range(10 ** (n-1), 10 ** n):
    if is_prime(i):
        prime = True
        for j in range(1, len(str(i))):
            if not is_prime(int(str(i)[:j])):  # we go through each prefix of lenght j
                prime = False
                break
        if prime:
            result.append(i)
print(result)
