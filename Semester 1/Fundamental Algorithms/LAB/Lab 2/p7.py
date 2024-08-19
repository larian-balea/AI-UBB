# 7. Generate in ascending order the first 𝒏 numbers from the set M defined as:
#    a. Number 1 belongs to M
#    b. If 𝒙 belongs to M then 2𝒙 + 1 and 3𝒙 + 1 also belong to M
#    c. M does not contain any other elements

"""
Desc: Prints the first n numbers of the given set in ascending order
Arguments:
    n: integer, the number of elements to print
Returns:
    integers
"""

n = int(input("Read n: "))
M = [1]
i = 0
while len(M) < n:
    m = len(M)
    while i < m:
        M.append(M[i] * 2 + 1)
        M.append(M[i] * 3 + 1)
        i += 1
M.sort()
M = [M[i] for i in range(n) if i == 0 or M[i] != M[i - 1]]  # remove duplicates
print(M[:n])
