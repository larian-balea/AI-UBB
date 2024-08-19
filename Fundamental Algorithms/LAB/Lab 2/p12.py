# 12. Determine if two natural numbers have the following property:
#     the same digits are necessary to write them in base 10.

"""
Desc: Determines if two natural numbers have the same digits
Arguments:
    a: integer, the first number
    b: integer, the second number
Returns:
    boolean, True if the numbers have the same digits
             False otherwise
"""

a = set(input('Read a: ')) # we convert the input to a set to remove duplicates
b = set(input('Read b: ')) # sets are unordered collections of unique elements

if a == b:
    print(True)
else:
    print(False)
