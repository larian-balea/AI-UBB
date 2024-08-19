# 13. Read a natural number 𝒏. Form another number from
#     its digits found at odd positions (from left to right).

"""
Desc: Forms a number from the digits found at odd positions
Arguments:
    n: integer, the number
Returns:
    integer, the number formed from the digits found at odd positions
"""

n = input('Read n: ')

odd = ''
for i in range(0, len(n), 2):
    odd += n[i]

print(odd)