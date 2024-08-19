# 19. Print the numbers of n digits equal to k multiplied by their product.
#     Numbers n and k (1 ≤ n ≤ 9, 1 ≤ k ≤ 100) are given.

"""
Desc: Prints the numbers of n digits equal to k multiplied by their product
Arguments:
    n, k: integers, the numbers
Returns:
    integer, the numbers of n digits equal to k multiplied by their product
"""


n = input('Read n: ')
k = input('Read k: ')
n = int(n)
k = int(k)
for i in range(10 ** (n-1), 10 ** n):
    p = 1
    c = i
    while c > 0:
        p *= c % 10
        c //= 10
    if p * k == i:
        print(i, end=' ')
