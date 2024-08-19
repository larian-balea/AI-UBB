undo_list = []


# 1. Add numbers in the array

def add(my_list, value):
    """
    Description: It adds an element at the end of a list
    Input: my_list, value
    Precondition: my_list - list of ints, value - int
    Outcome: the element is added at the end of the list
    """
    my_list.append(value)
    undo_list.append(len(my_list) - 1)
    undo_list.append("add")


def insert(my_list, index, value):
    """
    Description: It inserts an element at a given index in a list
    Input: my_list, index, value
    Precondition: my_list - list of ints, index - int, value - int
    Outcome: the element is inserted at the given index in the list
    """
    my_list.insert(index, value)
    undo_list.append(index)
    undo_list.append("insert")


# 2. Modify elements in the array

def remove(my_list, index):
    """
    Description: It removes an element from a given index in a list
    Input: my_list, index
    Precondition: my_list - list of ints, index - int
    Outcome: the element is removed from the given index in the list
    """
    value = my_list[index]
    my_list.pop(index)
    undo_list.append(value)
    undo_list.append(index)
    undo_list.append("remove")


def remove_interval(my_list, from_index, to_index):
    """
    Description: It removes elements from a given index to another given index in a list
    Input: my_list, from_index, to_index
    Precondition: my_list - list of ints, from_index - int, to_index - int
    Outcome: the elements are removed from the given index to the other given index in the list
    """
    values_list = []
    while to_index >= from_index:
        values_list.append(my_list[from_index])
        my_list.pop(from_index)
        to_index -= 1
    undo_list.append(values_list)
    undo_list.append(from_index)
    undo_list.append("remove_interval")


def replace(my_list, old_value, new_value, positions=None):
    """
    Description: It replaces all occurances of a value with a new one
    Input: my_list, old_value, new_value, positions
    Precondition: my_list - list of ints, old_value - list of ints, new_value - list of ints, positions - list of ints
    Outcome: all occurances of a value are replaced with a new one
    """
    if positions is None:
        positions = []
    positions_list = []
    for i in range(len(my_list)):
        if my_list[i:i + len(old_value)] == old_value and (i in positions or positions == []):
            positions_list.append(i)
    new_list = my_list.copy()
    p = 0
    for i in range(len(new_list)):
        if new_list[i:i + len(old_value)] == old_value and (i + p in positions or positions == []):
            my_list[i + p:i + len(old_value) + p] = new_value
            p += len(new_value) - len(old_value)
    undo_list.append(positions_list)
    undo_list.append(old_value)
    undo_list.append(new_value)
    undo_list.append("replace")


# 3. Get the numbers that have certain properties

def is_prime(n):
    """
    Description: It checks if a number is prime
    Input: n
    Precondition: n - int
    Output: bool
    Postcondition: True if n is prime, False otherwise
    """
    if n < 2:
        return False
    truth = True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            truth = False
            break
    return truth


def prime(my_list, from_index, to_index):
    """
    Description: It returns a list of prime numbers between 2 indexes
    Input: my_list, from_index, to_index
    Precondition: my_list - list of ints, from_index - int, to_index - int
    Output: primes
    Postcondition: primes - list of ints
    """
    primes = []
    for i in range(from_index, to_index + 1):
        if is_prime(my_list[i]):
            primes.append(my_list[i])
    return primes


def odd(my_list, from_index, to_index):
    """
    Description: It returns a list of odd numbers between 2 indexes
    Input: my_list, from_index, to_index
    Precondition: my_list - list of ints, from_index - int, to_index - int
    Output: odds
    Postcondition: odds - list of ints
    """
    odds = []
    for i in range(from_index, to_index + 1):
        if my_list[i] % 2 == 1:
            odds.append(my_list[i])
    return odds


# 4. Obtain different characteristics from sub-arrays

def summ(my_list, from_index, to_index):
    """
    Description: It returns the sum of elements between 2 indexes
    Input: my_list, from_index, to_index
    Precondition: my_list - list of ints, from_index - int, to_index - int
    Output: s
    Postcondition: s - int
    """
    s = 0
    for i in range(from_index, to_index + 1):
        s += my_list[i]
    return s


def gcd(my_list, from_index, to_index):
    """
    Description: It returns the greatest common divisor of elements between 2 indexes
    Input: my_list, from_index, to_index
    Precondition: my_list - list of ints, from_index - int, to_index - int
    Output: g
    Postcondition: g - int
    """
    g = my_list[from_index]
    for i in range(from_index + 1, to_index + 1):
        copy = i
        while g != copy:
            if g > copy:
                g = g - copy
            else:
                copy = copy - g
    return g


def maxx(my_list, from_index, to_index):
    """
    Description: It returns the maximum of elements between 2 indexes
    Input: my_list, from_index, to_index
    Precondition: my_list - list of ints, from_index - int, to_index - int
    Output: m
    Postcondition: m - int
    """
    m = my_list[from_index]
    for i in range(from_index + 1, to_index + 1):
        if m < my_list[i]:
            m = my_list[i]
    return m


# 5. Filter values

def filter_prime(my_list):
    """
    Description: It returns a list of prime numbers from a list
    Input: my_list
    Precondition: my_list - list of ints
    Output: new_list
    Postcondition: new_list - list of ints
    """
    new_list = prime(my_list, 0, len(my_list) - 1)
    return new_list


def filter_negative(my_list):
    """
    Description: It returns a list of negative numbers from a list
    Input: my_list
    Precondition: my_list - list of ints
    Output: new_list
    Postcondition: new_list - list of ints
    """
    new_list = []
    for i in my_list:
        if i < 0:
            new_list.append(i)
    return new_list


# 7. Work with files

def read_file(file_name, my_list):
    """
    Description: It reads a list of numbers from a file
    Input: file_name
    Precondition: file_name - string
    Output: my_list
    Postcondition: my_list - list of ints
    """
    try:
        with open(file_name, "r") as file:
            new_list = file.read().split()
    except FileNotFoundError:
        print("File not found")
    new_list = list(map(int, new_list))
    undo_list.append(my_list.copy())
    undo_list.append("read")
    my_list.clear()
    for i in new_list:
        my_list.append(i)


def write_file(file_name, my_list):
    """
    Description: It writes a list of numbers to a file
    Input: file_name, my_list
    Precondition: file_name - string, my_list - list of ints
    """
    with open(file_name, "w") as file:
        for i in my_list:
            file.write(str(i) + " ")


# Main

def show_menu():
    """
    Description: It prints the menu
    """
    print("\n Options: \n \n"
          "0. Print array \n"
          "1. Add numbers in the array  \n"
          "2. Modify elements in the array \n"
          "3. Get the numbers that have certain properties \n"
          "4. Obtain different characteristics from sub-arrays \n"
          "5. Filter values \n"
          "6. Undo \n"
          "7. Work with files \n"
          "e. Exit \n"
          )


def add_numbers_in_the_array(current_list):
    """
    Description: Runs the addition methods
    """
    print("Add numbers in the array \n"
          "1. Add value as last element in list \n"
          "2. Insert value at index \n"
          "e. Exit \n"
          )
    command = input("Enter option: ")
    if command == 'e':
        return
    elif command == '1':
        print("Add value as last element in list \n")
        value = int(input("Enter value: "))
        add(current_list, value)
    elif command == '2':
        print("Insert value at index \n")
        value = int(input("Enter value: "))
        index = int(input("Enter index: "))
        insert(current_list, index, value)


def modify_elements_in_the_array(current_list):
    """
    Description: Runs the modification methods
    """
    print("Modify elements in the array \n"
          "1. Remove element at index \n"
          "2. Remove elements between 2 indexes \n"
          "3. Replace all occurances of a value with a new one \n"
          "e. Exit \n"
          )
    command = input("Enter option: ")
    if command == 'e':
        return
    elif command == '1':
        print("Remove element at index \n")
        index = int(input("Enter index: "))
        remove(current_list, index)
    elif command == '2':
        print("Remove elements between 2 indexes \n")
        from_index = int(input("Enter index from which to remove: "))
        to_index = int(input("Enter index up to which to delete: "))
        remove_interval(current_list, from_index, to_index)
    elif command == '3':
        print("Replace all occurances of a value with a new one \n")
        old_value = input("Enter a list of numbers separated by spaces: ")
        old_value = list(map(int, old_value.split()))
        new_value = input("Enter a list of numbers separated by spaces: ")
        new_value = list(map(int, new_value.split()))
        replace(current_list, old_value, new_value)


def get_numbers_that_have_certain_properties(current_list):
    """
    Description: Runs the methods that get numbers with certain properties
    """
    print("Get the numbers that have certain properties \n"
          "1. Get prime numbers between 2 indexes \n"
          "2. Get odd numbers between 2 indexes \n"
          "e. Exit \n"
          )
    command = input("Enter option: ")
    if command == 'e':
        return
    elif command == '1':
        print("Get prime numbers between 2 indexes \n")
        from_index = int(input("Enter index from which to search: "))
        to_index = int(input("Enter index up to which to search: "))
        for i in prime(current_list, from_index, to_index):
            print(i, end=' ')
    elif command == '2':
        print("Get odd numbers between 2 indexes \n")
        from_index = int(input("Enter index from which to search: "))
        to_index = int(input("Enter index up to which to search: "))
        for i in odd(current_list, from_index, to_index):
            print(i, end=' ')


def obtain_different_characteristics_from_sub_arrays(current_list):
    """
    Description: Runs the methods that get different characteristics from sub-arrays
    """
    print("Obtain different characteristics from sub-arrays \n"
          "1. Get sum of elements between 2 indexes \n"
          "2. Get common greatest divisor of elements between 2 indexes \n"
          "3. Get maximum of elements between 2 indexes \n"
          "e. Exit \n"
          )
    command = input("Enter option: ")
    if command == 'e':
        return
    elif command == '1':
        print("Get sum of elements between 2 indexes \n")
        from_index = int(input("Enter index from which to search: "))
        to_index = int(input("Enter index up to which to search: "))
        print(summ(current_list, from_index, to_index))
    elif command == '2':
        print("Get common greatest divisor of elements between 2 indexes \n")
        from_index = int(input("Enter index from which to search: "))
        to_index = int(input("Enter index up to which to search: "))
        print(gcd(current_list, from_index, to_index))
    elif command == '3':
        print("Get maximum of elements between 2 indexes \n")
        from_index = int(input("Enter index from which to search: "))
        to_index = int(input("Enter index up to which to search: "))
        print(maxx(current_list, from_index, to_index))


def filter_values(current_list):
    """
    Description: Runs the methods that filter values
    """
    print("Filter values \n"
          "1. Filter list so only prime values remain \n"
          "2. Filter list so only negative values remain \n"
          "e. Exit \n"
          )
    command = input("Enter option: ")
    if command == 'e':
        return
    elif command == '1':
        print("Filter list so only prime values remain \n")
        for i in filter_prime(current_list):
            print(i, end=' ')
    elif command == '2':
        print("Filter list so only negative values remain \n")
        for i in filter_negative(current_list):
            print(i, end=' ')


def undo(current_list):
    """
    Description: It undoes the last operation that modified the list
    """
    print("Undo the last operation that modified the array \n")
    if len(undo_list) == 0:
        print("No more undos")
    elif undo_list[-1] in ["add", "insert"]:
        undo_list.pop()
        remove(current_list, undo_list[-1])
        undo_list.pop()
    elif undo_list[-1] == "remove":
        undo_list.pop()
        insert(current_list, undo_list[-1], undo_list[-2])
        del undo_list[-2:]
    elif undo_list[-1] == "remove_interval":
        undo_list.pop()
        for i in list(reversed(undo_list[-2])):
            insert(current_list, int(undo_list[-1]), i)
            del undo_list[-2:]
        del undo_list[-2:]
    elif undo_list[-1] == "replace":
        undo_list.pop()
        replace(current_list, undo_list[-1], undo_list[-2], undo_list[-3])
        del undo_list[-7:]
    elif undo_list[-1] == "read":
        undo_list.pop()
        current_list.clear()
        for i in undo_list[-1]:
            current_list.append(i)
        undo_list.pop()


def work_with_files(current_list):
    """
    Description: Runs the methods that work with files
    """
    print("Work with files \n"
          "1. Read current list from file \n"
          "2. Write current list of numbers to file \n"
          "e. Exit \n"
          )
    command = input("Enter option: ")
    if command == 'e':
        return
    elif command == '1':
        print("Read current list from file \n")
        file_name = input("Enter file name: ")
        read_file(file_name, current_list)
    elif command == '2':
        print("Write current list of numbers to file \n")
        file_name = input("Enter file name: ")
        write_file(file_name, current_list)


def main():
    """
    Description: It runs the program
    """

    my_list = [-3, 4, -2, 7]
    while True:
        show_menu()
        command = input("Enter option: ")
        if command == 'e':
            break
        elif command == '0':
            print(my_list)
        elif command == '1':
            add_numbers_in_the_array(my_list)
        elif command == '2':
            modify_elements_in_the_array(my_list)
        elif command == '3':
            get_numbers_that_have_certain_properties(my_list)
        elif command == '4':
            obtain_different_characteristics_from_sub_arrays(my_list)
        elif command == '5':
            filter_values(my_list)
        elif command == '6':
            undo(my_list)
        elif command == '7':
            work_with_files(my_list)


if __name__ == "__main__":
    main()
