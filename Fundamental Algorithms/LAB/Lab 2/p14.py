# 14. Read a natural number 𝒏. Print the number of 1s
#     from the binary representation of 𝒏.

"""
Desc: Prints the number of 1s from the binary representation of a number
Arguments:
    n: integer, the number
Returns:
    integer, the number of 1s from the binary representation
"""

n = input('Read n: ')
n = int(n)

ones = 0
while n > 0:
    ones += n & 1  # we compare the last bit of n with 1
    n >>= 1        # we shift n to the right by 1 bit

print(ones)
