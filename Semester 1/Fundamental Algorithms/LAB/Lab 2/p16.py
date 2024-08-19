# 16.  Read numbers having minimum 2 digits until number 0 is given.
#      Print how many numbers have the unit figure smaller than the tens figure.

"""
Desc: Prints how many numbers have the unit figure smaller than the tens figure
Arguments:
    integers, the numbers having minimum 2 digits until number 0 is given
Returns:
    integer, the number of numbers having the unit figure smaller than the tens figure
"""

count = 0
print("Read integers until 0 is read:")

while True:
    n = int(input())
    if n == 0:
        break
    if n % 10 < n // 10 and n >= 10:
        count = count + 1

print(count)