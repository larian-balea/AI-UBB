# 18. Print the number of common digits of two numbers, as well as the digits.

"""
Desc: Prints the number of common digits of two numbers, as well as the digits
Arguments:
    n1, n2: integers, the numbers
Returns:
    integer, the number of common digits
"""

n1 = input('Read n1: ')
n2 = input('Read n2: ')

common_digits = 0
common = []

n1.sort()
n2.sort()

n1 = [n1[i] for i in range(len(n1)) if i == 0 or n1[i] != n1[i - 1]]  # remove duplicates
n2 = [n2[i] for i in range(len(n2)) if i == 0 or n2[i] != n2[i - 1]]  # remove duplicates

i = 0
j = 0
while i < len(n1) and j < len(n2):
    if n1[i] == n2[j]:
        common_digits += 1
        common.append(n1[i])
        i += 1
        j += 1
    elif n1[i] < n2[j]:
        i += 1
    else:
        j += 1

print(common_digits)
print(common[0], end='')
for i in range(1, len(common)):
    print(', ', common[i], end='')
