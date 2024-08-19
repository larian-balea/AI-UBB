def is_leap_year(y):
    if y % 400 == 0:
        return True
    if y % 4 == 0 and y % 100 != 0:
        return True
    return False


days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_prime(num):
    if num < 2:
        return False
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True


def sum_of_digits(m):
    return sum(int(digit) for digit in str(m))


# 1. Compute the control digit of an integer by summing up its digits, then summing
#    up the digits of the sum, so on, until a sum of only one digit is obtained.
def control_digit(n):
    """
    Desc: Computes the control digit of an integer
    Arguments:
        n: integer, the number
    Returns:
        integer, the control digit
    """
    while len(n) > 1:
        s = 0
        for i in n:
            s += int(i)
        n = str(s)
    return n


# 2. Determine a date (as day, month, year) starting from two integer numbers that
#    represent the year and the number of the day in that year
def date_from_day(year, day):
    """
    Desc: Determines the date starting from the year and the day in that year
    Arguments:
        year: int
        day: int
    Returns:
        integer, the date
    """
    if is_leap_year(year):
        days[1] = 29

    for i in range(12):
        if int(day) <= days[i]:
            return day, i + 1, year
        day = int(day) - days[i]
    days[1] = 28


# 3. Print all powers less than k of a given integer number n.
def powers_less_then_k(n, k):
    """
    Desc: Prints all powers less than k of n
    Arguments:
        n: int
        k: int
    Returns:
        integers, powers of n less than k
    """
    power = 1
    while power < k:
        print(power, end=" ")
        power *= n


# 4. Determine the smallest number that can be formed
#    with the digits of a number read from keyboard.
def smallest_number(n):
    """
    Desc: Determines the smallest number that can be formed with the digits of a number
    Arguments:
        n: integer
    Returns:
        integer, the smallest number
    """
    n = list(n)
    n.sort()
    i = 0
    while n[i] == '0':
        i += 1
    n[0], n[i] = n[i], n[0]

    return int(''.join(n))


# 5. Determine the value of the element at index 𝒌 in the array 1, 2, 2, 3, 3, 3, 4, 4, 4, 4,…
#    without reading or effectively creating the array.
def element_at_index(k):
    """
    Desc: Determines the value of the element at index k in the array 1, 2, 2, 3, 3, 3, 4, 4, 4, 4,…
    Arguments:
        k: int
    Returns:
        integer, the value of the element at index k
    """
    i = 1
    while k > i:
        k -= i
        i += 1
    return i


# 6. Given the current date (day, month, year) and the birthdate of a person (day, month, year),
#    compute the age of the person in number of years.
def age_in_years(bd, bm, by, cd, cm, cy):
    """
    Desc: Determines the age of a person in number of years
    Arguments:
        bd: int, the day of birth
        bm: int, the month of birth
        by: int, the year of birth
        cd: int, the current day
        cm: int, the current month
        cy: int, the current year
    Returns:
        integer, the age in years
    """
    if cy < by:
        return 0
    elif cy == by and cm < bm:
        return 0
    elif cy == by and cm == bm and cd < bd:
        return 0

    age = 0
    while by < cy:
        age += 1
        by += 1
    if cm < bm or (cm == bm and cd < bd):
        age -= 1

    return age


# 7. Generate in ascending order the first 𝒏 numbers from the set M defined as:
#    a. Number 1 belongs to M
#    b. If 𝒙 belongs to M then 2𝒙 + 1 and 3𝒙 + 1 also belong to M
#    c. M does not contain any other elements
def generate_set_m(n):
    """
    Desc: Prints the first n numbers of the given set in ascending order
    Arguments:
        n: integer, the number of elements to print
    Returns:
        integers
    """
    m = [1]
    i = 0
    while len(m) < n:
        l = len(m)
        while i < l:
            m.append(m[i] * 2 + 1)
            m.append(m[i] * 3 + 1)
            i += 1
    m.sort()
    m = [m[i] for i in range(n) if i == 0 or m[i] != m[i - 1]]  # remove duplicates
    return m[:n]


# 8. Consider an integer number 𝒏. Print the nearest prime number to 𝒏.
def nearest_prime(n):
    """
    Desc: Print the nearest prime number to n
    Arguments:
        n: integer, the number
    Returns:
        integer, the nearest prime number to n
    """
    if is_prime(n):
        return n, 0  # like tuple just to be easier for the other case
    else:
        i = 1
        ok = True
        first = 0
        second = 0
        while ok:
            if is_prime(n - i):
                first = n - i
                ok = False
            if is_prime(n + i):
                second = n + i
                ok = False
            if not ok:
                return first, second  # if there are 2 primes at the same distance we return both
            i += 1


# 9. Print all numbers with maximum 2 digits of form 𝒙𝒚
#    with the property that the last digit of (𝒙𝒚)^2 is 𝒚.
def numbers_with_property():
    """
    Desc: Print all numbers with maximum 2 digits of form 𝒙𝒚
        with the property that the last digit of (𝒙𝒚)^2 is 𝒚.
    Arguments:
        -
    Returns:
        integers, numbers with the property that the last digit of (𝒙𝒚)^2 is 𝒚
    """

    numbers = []

    '''
    for i in range(0, 100):  # intuitive way
        if (i ** 2) % 10 == i % 10:
            numbers.append(i)
    '''

    for i in range(0, 10):  # tricky way
        for j in 0, 1, 5, 6:
            numbers.append(i * 10 + j)

    return numbers


# 10. Read integers numbers until number 0 is read. Print the number of pairs 𝒏𝟏 and
#     n𝟐 of numbers read consecutively with the property that the number of digits 5
#     from 𝒏𝟏 is strictly higher than the number of digits 5 from 𝒏𝟐.
def pairs_of_numbers(list_of_numbers):
    """
    Desc: Read integers numbers until number 0 is read. Print the number of pairs n1 and n2 of numbers read consecutively with the property that the number of digits 5 from n1 is strictly higher than the number of digits 5 from n2.
    Arguments:
        integers, until 0 is read
    Returns:
        integer, the number of pairs
    """

    count = 0
    n1 = list_of_numbers[0]
    if n1 != 0:
        i = 1
        while i < len(list_of_numbers):
            n2 = list_of_numbers[i]
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
            i += 1
    return count


# 11. Generate all prime numbers having n digits with the property that all its
def primes_with_property(n):
    """
    Desc: Print all prime numbers having n digits with the property that all its prefixes are also prime
    Arguments:
        n: integer, the number of digits
    Returns:
        integers, prime numbers with the property that all its prefixes are also prime
    """

    result = []
    for i in range(10 ** (n-1), 10 ** n):
        if is_prime(i):
            prime = True
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[:j])):  # we go through each prefix of lenght j
                    prime = False
                    break
            if prime:
                result.append(i)
    return result


# 12. Determine if two natural numbers have the following property:
#     the same digits are necessary to write them in base 10.
def same_digits(a, b):
    """
    Desc: Determines if two natural numbers have the same digits
    Arguments:
        a: integer, the first number
        b: integer, the second number
    Returns:
        boolean, True if the numbers have the same digits
                 False otherwise
    """
    a = set(str(a))  # we convert the input to a set to remove duplicates
    b = set(str(b))  # sets are unordered collections of unique elements

    if a == b:
        return True
    else:
        return False


# 13. Read a natural number 𝒏. Form another number from
#     its digits found at odd positions (from left to right).
def number_from_odd_positions(n):
    """
    Desc: Forms a number from the digits found at odd positions
    Arguments:
        n: integer, the number
    Returns:
        integer, the number formed from the digits found at odd positions
    """
    n = str(n)
    odd = ''
    for i in range(0, len(n), 2):
        odd += n[i]
    return int(odd)


# 14. Read a natural number 𝒏. Print the number of 1s
#     from the binary representation of 𝒏.
def number_of_ones(n):
    """
    Desc: Prints the number of 1s from the binary representation of a number
    Arguments:
        n: integer, the number
    Returns:
        integer, the number of 1s from the binary representation
    """
    ones = 0
    while n > 0:
        ones += n & 1  # we compare the last bit of n with 1
        n >>= 1        # we shift n to the right by 1 bit
    return ones


# 15. Determine the age of a person in number of days. The current date and the
#     birthdate are known
def age_in_days(bd, bm, by, cd, cm, cy):
    """
    Desc: Determines the age of a person in number of days
    Arguments:
        bd: int, the day of birth
        bm: int, the month of birth
        by: int, the year of birth
        cd: int, the current day
        cm: int, the current month
        cy: int, the current year
    Returns:
        integer, the age in days
    """
    if cy < by:
        return 0
    elif cy == by and cm < bm:
        return 0
    elif cy == by and cm == bm and cd < bd:
        return 0

    age = 0

    if by != cy:
        if not (bm > 2 or bm == 2 and bd == 29) and is_leap_year(by):
            age = age + 1
        age = age + days[bm - 1] - bd + 1
        bd = 1
        bm = bm + 1
        while bm <= 12:
            age = age + days[bm - 1]
            bm = bm + 1
        bm = 1
        by = by + 1
        while by < cy:
            if is_leap_year(by):
                age = age + 366
            else:
                age = age + 365
            by = by + 1

    # cy == by
    if cm == bm:
        return age + cd - bd + 1
    else:
        return age + days[bm - 1] - bd + 1 + cd


# 16.  Read numbers having minimum 2 digits until number 0 is given.
#      Print how many numbers have the unit figure smaller than the tens figure.
def numbers_with_unit_smaller_than_tens(list_of_numbers):
    """
    Desc: Prints how many numbers have the unit figure smaller than the tens figure
    Arguments:
        integers, the numbers having minimum 2 digits until number 0 is given
    Returns:
        integer, the number of numbers having the unit figure smaller than the tens figure
    """
    count = 0
    i = 0
    while i < len(list_of_numbers):
        n = list_of_numbers[i]
        if n == 0:
            break
        if n % 10 < n // 10 and n >= 10:
            count = count + 1
        i += 1
    return count


# 17. A number 𝒏 is special if there is a natural number 𝒎 such that 𝑛 = 𝑚 + 𝑆(𝑚)
#     where 𝑆(𝑚) is the sum of digits of 𝒎. Verify if a given number is special.
def is_special(n):
    """
    Desc: Verifies if a given number is special
    Arguments:
        n: integer, the number
    Returns:
        boolean, True if the number is special
                 False otherwise
    """
    # Iterate over possible values of m
    lower_bound = max(1, n - 9 * (len(str(n)) - 1))
    for m in range(lower_bound, n):
        if m + sum_of_digits(m) == n:
            return True
    return False


# 18. Print the number of common digits of two numbers, as well as the digits.
def common_digits(n1, n2):
    """
    Desc: Prints the number of common digits of two numbers, as well as the digits
    Arguments:
        n1, n2: integers, the numbers
    Returns:
        integer, the number of common digits
    """

    digits = 0
    common = []

    n1.sort()
    n2.sort()

    n1 = [n1[i] for i in range(len(n1)) if i == 0 or n1[i] != n1[i - 1]]  # remove duplicates
    n2 = [n2[i] for i in range(len(n2)) if i == 0 or n2[i] != n2[i - 1]]  # remove duplicates

    i = 0
    j = 0
    while i < len(n1) and j < len(n2):
        if n1[i] == n2[j]:
            digits += 1
            common.append(n1[i])
            i += 1
            j += 1
        elif n1[i] < n2[j]:
            i += 1
        else:
            j += 1

    return digits, common


# 19. Print the numbers of n digits equal to k multiplied by their product.
#     Numbers n and k (1 ≤ n ≤ 9, 1 ≤ k ≤ 100) are given.
def numbers_equal_to_k(n, k):
    """
    Desc: Prints the numbers of n digits equal to k multiplied by their product
    Arguments:
        n, k: integers, the numbers
    Returns:
        integer, the numbers of n digits equal to k multiplied by their product
    """

    numbers = []
    for i in range(10 ** (n-1), 10 ** n):
        p = 1
        c = i
        while c > 0:
            p *= c % 10
            c //= 10
        if p * k == i:
            numbers.append(i)

    return numbers


# 20.  Given a natural number 𝒏, determine the greatest number 𝒑
#      having the property that 2𝒑 is smaller or equal to 𝒏.
def greatest_p(n):
    """
    Desc: Determines the greatest number p having the property that 2^p is smaller or equal to n
    Arguments:
        n: integer, the number
    Returns:
        integer, the greatest number p
    """
    p = 0
    while 2 ** (p + 1) <= n:
        p += 1

    return p


def menu():
    print("1. Compute the control digit of an integer")
    print("2. Determine a date starting from the year and the day in that year")
    print("3. Print all powers less than k of a given integer number n")
    print("4. Determine the smallest number that can be formed with the digits of a number")
    print("5. Determine the value of the element at index k in the array 1, 2, 2, 3, 3, 3, 4, 4, 4, 4,…")
    print("6. Determine the age of a person in number of years")
    print("7. Generate in ascending order the first n numbers from the set M")
    print("8. Print the nearest prime number to n")
    print("9. Print all numbers with maximum 2 digits of form xy")
    print("10. Print the number of pairs n1 and n2 of numbers read consecutively")
    print("11. Print all prime numbers having n digits with the property that all its prefixes are also prime")
    print("12. Determine if two natural numbers have the same digits")
    print("13. Form another number from its digits found at odd positions")
    print("14. Print the number of 1s from the binary representation of n")
    print("15. Determine the age of a person in number of days")
    print("16. Print how many numbers have the unit figure smaller than the tens figure")
    print("17. Verify if a given number is special")
    print("18. Print the number of common digits of two numbers")
    print("19. Print the numbers of n digits equal to k multiplied by their product")
    print("20. Determine the greatest number p having the property that 2^p is smaller or equal to n")
    print("0. Exit")


def main():
    menu()
    while True:
        option = input("Choose an option: ")
        if option == 'm':
            menu()
        if option == '0':
            break
        elif option == '1':
            n = input("Read n: ")
            print(control_digit(n))
        elif option == '2':
            year = int(input("Read year: "))
            day = int(input("Read day: "))
            print(date_from_day(year, day))
        elif option == '3':
            n = int(input("Read n: "))
            k = int(input("Read k: "))
            powers_less_then_k(n, k)
        elif option == '4':
            n = input("Read n: ")
            print(smallest_number(n))
        elif option == '5':
            k = int(input("Read k: "))
            print(element_at_index(k))
        elif option == '6':
            bd = int(input("Read birth day: "))
            bm = int(input("Read birth month: "))
            by = int(input("Read birth year: "))
            cd = int(input("Read current day: "))
            cm = int(input("Read current month: "))
            cy = int(input("Read current year: "))
            print(age_in_years(bd, bm, by, cd, cm, cy))
        elif option == '7':
            n = int(input("Read n: "))
            print(generate_set_m(n))
        elif option == '8':
            n = int(input("Read n: "))
            print(nearest_prime(n))
        elif option == '9':
            print(numbers_with_property())
        elif option == '10':
            list_of_numbers = []
            print("Read numbers until 0 is read")
            while True:
                n = int()
                list_of_numbers.append(n)
                if n == 0:
                    break
            print(pairs_of_numbers(list_of_numbers))
        elif option == '11':
            n = int(input("Read n: "))
            print(primes_with_property(n))
        elif option == '12':
            a = int(input("Read a: "))
            b = int(input("Read b: "))
            print(same_digits(a, b))
        elif option == '13':
            n = int(input("Read n: "))
            print(number_from_odd_positions(n))
        elif option == '14':
            n = int(input("Read n: "))
            print(number_of_ones(n))
        elif option == '15':
            bd = int(input("Read birth day: "))
            bm = int(input("Read birth month: "))
            by = int(input("Read birth year: "))
            cd = int(input("Read current day: "))
            cm = int(input("Read current month: "))
            cy = int(input("Read current year: "))
            print(age_in_days(bd, bm, by, cd, cm, cy))
        elif option == '16':
            list_of_numbers = []
            print("Read numbers until 0 is read")
            while True:
                n = int()
                list_of_numbers.append(n)
                if n == 0:
                    break
            print(numbers_with_unit_smaller_than_tens(list_of_numbers))
        elif option == '17':
            n = int(input("Read n: "))
            print(is_special(n))
        elif option == '18':
            n1 = list(map(int, input("Read n1: ").split()))
            n2 = list(map(int, input("Read n2: ").split()))
            digits, common = common_digits(n1, n2)
            print(digits)
            print(common[0], end='')
            for i in range(1, len(common)):
                print(', ', common[i], end='')
        elif option == '19':
            n = int(input("Read n: "))
            k = int(input("Read k: "))
            print(numbers_equal_to_k(n, k))
        elif option == '20':
            n = int(input("Read n: "))
            print(greatest_p(n))
        else:
            print("Invalid option")


if __name__ == '__main__':
    main()
