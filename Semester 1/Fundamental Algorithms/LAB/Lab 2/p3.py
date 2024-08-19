# 3. Print all powers less than k of a given integer number n.

"""
Desc: Prints all powers less than k of n
Arguments:
    n: int
    k: int
Returns:
    integers, powers of n less than k
"""

n = input('Read n: ')
k = input('Read k: ')
power = 1
while power < int(k):
    print(power, end=" ")
    power *= int(n)      
