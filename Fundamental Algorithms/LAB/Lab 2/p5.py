# 5. Determine the value of the element at index 𝒌 in the array 1, 2, 2, 3, 3, 3, 4, 4, 4, 4,…
#    without reading or effectively creating the array.

"""
Desc: Determines the value of the element at index k in the array 1, 2, 2, 3, 3, 3, 4, 4, 4, 4,…
Arguments:
    k: int
Returns:
    integer, the value of the element at index k
"""

k = int(input('Read k: '))
i = 1
while k > i:
    k -= i
    i += 1
print(i)
