# 1. Compute the control digit of an integer by summing up its digits, then summing
#    up the digits of the sum, so on, until a sum of only one digit is obtained.

"""
Desc: Computes the control digit of an integer
Arguments:
    n: integer, the number
Returns:
    integer, the control digit
"""

n = input('Read n: ')
while len(n) > 1:
    s = 0
    for i in n:
        s += int(i)
    n = str(s)
print(n)
