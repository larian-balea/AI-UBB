# 4. Determine the smallest number that can be formed
#    with the digits of a number read from keyboard.

"""
Desc: Determines the smallest number that can be formed with the digits of a number
Arguments:
    n: integer
Returns:
    integer, the smallest number
"""

n = input('Read n: ')
n = list(n)
n.sort()
i = 0
while n[i] == '0':
    i += 1
n[0], n[i] = n[i], n[0]

print(''.join(n))
