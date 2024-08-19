# 10. Read integers numbers until number 0 is read. Print the number of pairs 𝒏𝟏 and
#     n𝟐 of numbers read consecutively with the property that the number of digits 5
#     from 𝒏𝟏 is strictly higher than the number of digits 5 from 𝒏𝟐.

"""
Desc: Read integers numbers until number 0 is read. Print the number of pairs n1 and n2 of numbers read consecutively with the property that the number of digits 5 from n1 is strictly higher than the number of digits 5 from n2.
Arguments:
    integers, until 0 is read
Returns:
    integer, the number of pairs
"""

count = 0
print("Read integers until 0 is read:")
n1 = int(input())
if n1 != 0:
    while True:
        n2 = int(input())
        if n2 == 0:
            break
        count1 = 0
        count2 = 0
        copy_n2 = n2
        while n1 > 0:
            if n1 % 10 == 5:
                count1 = count1 + 1
            n1 = n1 // 10
        while n2 > 0:
            if n2 % 10 == 5:
                count2 = count2 + 1
            n2 = n2 // 10
        if count1 > count2:
            count = count + 1
        n1 = copy_n2
print(count)
