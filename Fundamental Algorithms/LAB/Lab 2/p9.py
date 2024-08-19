# 9. Print all numbers with maximum 2 digits of form 𝒙𝒚
#    with the property that the last digit of (𝒙𝒚)^2 is 𝒚.

"""
Desc: Print all numbers with maximum 2 digits of form 𝒙𝒚
        with the property that the last digit of (𝒙𝒚)^2 is 𝒚.
Arguments:
    -
Returns:
    integers, numbers with the property that the last digit of (𝒙𝒚)^2 is 𝒚
"""

for i in range(0, 100):  # we go through all 2-digit numbers
    if (i ** 2) % 10 == i % 10:
        print(i, end=' ')

print()

for i in range(0, 10):  # we build the 2-digit
    for j in 0, 1, 5, 6:
        print(i * 10 + j, end=' ')
