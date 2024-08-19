# 20.  Given a natural number 𝒏, determine the greatest number 𝒑
#      having the property that 2𝒑 is smaller or equal to 𝒏.

"""
Desc: Determines the greatest number p having the property that 2^p is smaller or equal to n
Arguments:
    n: integer, the number
Returns:
    integer, the greatest number p
"""

n = int(input('Read n: '))
p = 0
while 2 ** (p + 1) <= n:
    p += 1

print(p)
