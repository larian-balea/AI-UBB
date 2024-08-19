from domain.my_vector import MyVector
from repository.vector_repository import VectorRepository


# vector functions

def console_add_scalar(boolean):
    if boolean:
        name_id = 1
        color = "r"
        thistype = 1
    else:
        try:
            name_id = int(input("Enter name_id: "))
            color = input("Enter color: ")
            thistype = int(input("Enter type: "))
        except ValueError as ve:
            print(ve)
            return
    try:
        values = input("Enter values: ")
        values = values.split()
        values = [float(i) for i in values]
        vector = MyVector(name_id, color, thistype, values)

        scalar = float(input("Enter scalar: "))

        if boolean:
            print("Old values: ", values)
            vector.add_scalar(scalar)
            print("New values: ", vector.get_values())
        else:
            print("Old vector:", vector)
            vector.add_scalar(scalar)
            print("New vector:", vector)
    except ValueError as ve:
        print(ve)


def console_add_vectors(boolean):
    if boolean:
        name_id1 = 1
        color1 = "r"
        thistype1 = 1
        name_id2 = 2
        color2 = "b"
        thistype2 = 1
    else:
        try:
            name_id1 = int(input("Enter name_id: "))
            color1 = input("Enter color: ")
            thistype1 = int(input("Enter type: "))
            name_id2 = int(input("Enter name_id: "))
            color2 = input("Enter color: ")
            thistype2 = int(input("Enter type: "))
        except ValueError as ve:
            print(ve)
            return

    try:
        values1 = input("Enter values: ")
        values1 = values1.split()
        values1 = [float(i) for i in values1]
        vector1 = MyVector(name_id1, color1, thistype1, values1)

        values2 = input("Enter values: ")
        values2 = values2.split()
        values2 = [float(i) for i in values2]
        vector2 = MyVector(name_id2, color2, thistype2, values2)

        print(vector1.add_vector(vector2))
    except ValueError as ve:
        print(ve)


def console_subtract_vectors(boolean):
    if boolean:
        name_id1 = 1
        color1 = "r"
        thistype1 = 1
        name_id2 = 2
        color2 = "b"
        thistype2 = 1
    else:
        try:
            name_id1 = int(input("Enter name_id: "))
            color1 = input("Enter color: ")
            thistype1 = int(input("Enter type: "))
            name_id2 = int(input("Enter name_id: "))
            color2 = input("Enter color: ")
            thistype2 = int(input("Enter type: "))
        except ValueError as ve:
            print(ve)
            return
    try:
        values1 = input("Enter values: ")
        values1 = values1.split()
        values1 = [float(i) for i in values1]
        vector1 = MyVector(name_id1, color1, thistype1, values1)

        values2 = input("Enter values: ")
        values2 = values2.split()
        values2 = [float(i) for i in values2]
        vector2 = MyVector(name_id2, color2, thistype2, values2)

        print(vector1.sub_vector(vector2))
    except ValueError as ve:
        print(ve)


def console_multiply_vectors(boolean):
    if boolean:
        name_id1 = 1
        color1 = "r"
        thistype1 = 1
        name_id2 = 2
        color2 = "b"
        thistype2 = 1
    else:
        try:
            name_id1 = int(input("Enter name_id: "))
            color1 = input("Enter color: ")
            thistype1 = int(input("Enter type: "))
            name_id2 = int(input("Enter name_id: "))
            color2 = input("Enter color: ")
            thistype2 = int(input("Enter type: "))
        except ValueError as ve:
            print(ve)
            return

    try:
        values1 = input("Enter values: ")
        values1 = values1.split()
        values1 = [float(i) for i in values1]
        vector1 = MyVector(name_id1, color1, thistype1, values1)

        values2 = input("Enter values: ")
        values2 = values2.split()
        values2 = [float(i) for i in values2]
        vector2 = MyVector(name_id2, color2, thistype2, values2)

        print(vector1.mul_vector(vector2))
    except ValueError as ve:
        print(ve)


def console_sum_of_elements(boolean):
    if boolean:
        name_id = 1
        color = "r"
        thistype = 1
    else:
        try:
            name_id = int(input("Enter name_id: "))
            color = input("Enter color: ")
            thistype = int(input("Enter type: "))
        except ValueError as ve:
            print(ve)
            return

    try:
        values = input("Enter values: ")
        values = values.split()
        values = [float(i) for i in values]
        vector = MyVector(name_id, color, thistype, values)

        print(vector.sum_of_elements())
    except ValueError as ve:
        print(ve)


def console_product_of_elements(boolean):
    if boolean:
        name_id = 1
        color = "r"
        thistype = 1
    else:
        try:
            name_id = int(input("Enter name_id: "))
            color = input("Enter color: ")
            thistype = int(input("Enter type: "))
        except ValueError as ve:
            print(ve)
            return

    try:
        values = input("Enter values: ")
        values = values.split()
        values = [float(i) for i in values]
        vector = MyVector(name_id, color, thistype, values)

        print(vector.prod_of_elements())
    except ValueError as ve:
        print(ve)


def console_average_of_elements(boolean):
    if boolean:
        name_id = 1
        color = "r"
        thistype = 1
    else:
        try:
            name_id = int(input("Enter name_id: "))
            color = input("Enter color: ")
            thistype = int(input("Enter type: "))
        except ValueError as ve:
            print(ve)
            return

    try:
        values = input("Enter values: ")
        values = values.split()
        values = [float(i) for i in values]
        vector = MyVector(name_id, color, thistype, values)

        print(vector.average_of_elements())
    except ValueError as ve:
        print(ve)


def console_minimum_of_vector(boolean):
    if boolean:
        name_id = 1
        color = "r"
        thistype = 1
    else:
        try:
            name_id = int(input("Enter name_id: "))
            color = input("Enter color: ")
            thistype = int(input("Enter type: "))
        except ValueError as ve:
            print(ve)
            return

    try:
        values = input("Enter values: ")
        values = values.split()
        values = [float(i) for i in values]
        vector = MyVector(name_id, color, thistype, values)

        print(vector.minimum_of_elements())
    except ValueError as ve:
        print(ve)


def console_maximum_of_vector(boolean):
    if boolean:
        name_id = 1
        color = "r"
        thistype = 1
    else:
        try:
            name_id = int(input("Enter name_id: "))
            color = input("Enter color: ")
            thistype = int(input("Enter type: "))
        except ValueError as ve:
            print(ve)
            return

    try:
        values = input("Enter values: ")
        values = values.split()
        values = [float(i) for i in values]
        vector = MyVector(name_id, color, thistype, values)

        print(vector.maximum_of_elements())
    except ValueError as ve:
        print(ve)


# repo functions

# 1
def console_add_vector(repo):
    try:
        name_id = int(input("Enter name_id: "))
        color = input("Enter color: ")
        thistype = int(input("Enter type: "))

        values = input("Enter values: ")
        values = values.split()
        values = [float(i) for i in values]
        vector = MyVector(name_id, color, thistype, values)

        repo.add(vector)
    except ValueError as ve:
        print(ve)


# 2
def console_get_all_vectors(repo):
    try:
        # print(repo.get_all())
        print(str(repo))
    except ValueError as ve:
        print(ve)


# 3
def console_get_vector_at_index(repo):
    try:
        index = int(input("Enter index: "))
        print(repo.get_at_index(index))
    except ValueError as ve:
        print(ve)


# 4
def console_update_vector_at_index(repo):
    try:
        index = int(input("Enter index: "))
        name_id = int(input("Enter name_id: "))
        color = input("Enter color: ")
        thistype = int(input("Enter type: "))

        values = input("Enter values: ")
        values = values.split()
        values = [float(i) for i in values]
        vector = MyVector(name_id, color, thistype, values)

        repo.update_at_index(index, vector)
    except ValueError as ve:
        print(ve)


# 5
def console_update_vector_by_name_id(repo):
    try:
        name_id = int(input("Enter name_id: "))
        color = input("Enter color: ")
        thistype = int(input("Enter type: "))

        values = input("Enter values: ")
        values = values.split()
        values = [float(i) for i in values]
        vector = MyVector(name_id, color, thistype, values)

        repo.update_by_name_id(name_id, vector)
    except ValueError as ve:
        print(ve)


# 6
def console_delete_vector_at_index(repo):
    try:
        index = int(input("Enter index: "))
        repo.delete_at_index(index)
    except ValueError as ve:
        print(ve)


# 7
def console_delete_vector_by_name_id(repo):
    try:
        name_id = int(input("Enter name_id: "))
        repo.delete_by_name_id(name_id)
    except ValueError as ve:
        print(ve)


# 8
def console_plot_vectors(repo):
    repo.chart()


# 9
def console_sum_of_all_elements(repo):
    try:
        print(repo.sum_of_all_elements())
    except ValueError as ve:
        print(ve)


# 10
def console_get_vector_sum_of_all_vectors(repo):
    try:
        print(repo.get_vector_sum_of_all_vectors())
    except ValueError as ve:
        print(ve)


# 11
def console_get_elements_with_given_sum(repo):
    try:
        summ = float(input("Enter sum: "))
        print(repo.get_elements_with_given_sum(summ))
    except ValueError as ve:
        print(ve)


# 12
def console_get_vectors_with_minimum_less_than_value(repo):
    try:
        value = float(input("Enter value: "))
        print(repo.get_vectors_with_minimum_less_than_value(value))
    except ValueError as ve:
        print(ve)


# 13
def console_get_sum_of_elements_of_vectors_of_color(repo):
    try:
        color = input("Enter color: ")
        print(repo.get_sum_of_elements_of_vectors_of_color(color))
    except ValueError as ve:
        print(ve)


# 14
def console_get_max_of_vectors_with_sum_greater_than_value(repo):
    try:
        value = float(input("Enter value: "))
        print(repo.get_max_of_vectors_with_sum_greater_than_value(value))
    except ValueError as ve:
        print(ve)


# 15
def console_get_min_of_all_vectors(repo):
    try:
        print(repo.get_min_of_all_vectors())
    except ValueError as ve:
        print(ve)


# 16
def console_get_list_of_values_multiplication_of_consecutive_vectors(repo):
    try:
        print(repo.get_list_of_values_multiplication_of_consecutive_vectors())
    except ValueError as ve:
        print(ve)


# 17
def console_delete_all_vectors(repo):
    repo.delete_all()


# 18.1
def console_delete_vectors_of_color(repo):
    try:
        color = input("Enter color: ")
        value = float(input("Enter value: "))
        repo.delete_vectors_of_color(color, value)
    except ValueError as ve:
        print(ve)


# 18.2
def console_delete_vectors_with_product_of_elements_greater_than_value(repo):
    try:
        value = float(input("Enter value: "))
        repo.delete_vectors_with_product_of_elements_greater_than_value(value)
    except ValueError as ve:
        print(ve)


# 19
def console_delete_vectors_between_two_indexes(repo):
    try:
        index1 = int(input("Enter index1: "))
        index2 = int(input("Enter index2: "))
        repo.delete_vectors_between_two_indexes(index1, index2)
    except ValueError as ve:
        print(ve)


# 20
def console_delete_vectors_with_maximum_equal_to_value(repo):
    try:
        value = float(input("Enter value: "))
        repo.delete_vectors_with_maximum_equal_to_value(value)
    except ValueError as ve:
        print(ve)


# 21
def console_add_scalar_to_all(repo):
    try:
        scalar = float(input("Enter scalar: "))
        repo.add_scalar_to_all(scalar)
    except ValueError as ve:
        print(ve)


# 22
def console_update_color_of_vectors_with_name_id(repo):
    try:
        name_id = int(input("Enter name_id: "))
        color = input("Enter color: ")
        repo.update_color_of_vectors_with_name_id(name_id, color)
    except ValueError as ve:
        print(ve)


# 23
def console_update_vectors_of_type_by_setting_color(repo):
    try:
        given_type = int(input("Enter type: "))
        given_color = input("Enter color: ")
        repo.update_vectors_of_type_by_setting_color(given_type, given_color)
    except ValueError as ve:
        print(ve)


def print_menu():
    print("\n   ▶ 0. Exit                   \n"
          "   ▶ 1. Vector operations      \n"
          "   ▶ 2. Vector list operations \n"
          )


def print_vector_menu():
    print("\n   ▶ 0. Back to main menu                                        \n"
          "Scalar operations:         Reduction operations:                 \n"
          "   ▶ 1. Add scalar            ▶ 5. Sum of elements in vector     \n"
          "Vector operations:            ▶ 6. Product of elements in vector \n"
          "   ▶ 2. Add vectors           ▶ 7. Average of elements in vector \n"
          "   ▶ 3. Subtract vectors      ▶ 8. Minimum of a vector           \n"
          "   ▶ 4. Multiply vectors      ▶ 9. Maximum of a vector           \n"
          )


def print_vector_list_menu():
    print("\n"
          "   ▶ 0. Back to main menu                       ▶ 12. Get vectors with minimum lass than value            \n"
          "   ▶ 1. Add a vector to the repository list     ▶ 13. Get sum of elements of vectors of color             \n"
          "   ▶ 2. Get all vectors                         ▶ 14. Get the max of vectors with sum greater than value  \n"
          "   ▶ 3. Get a vector at a given index           ▶ 15. Get the min of all vectors.                         \n"
          "   ▶ 4. Update a vector at given index          ▶ 16. Get list of values multiplication of consecutive vectors \n"
          "   ▶ 5. Update a vector identified by name_id   ▶ 17. Delete all vectors                                  \n"
          "   ▶ 6. Delete a vector by index                ▶ 18. Delete vectors of color / vectors with product of elements greater than value \n"
          "   ▶ 7. Delete a vector by name_id              ▶ 19. Delete vectors between 2 indexes                    \n"
          "   ▶ 8. Plot all vectors                        ▶ 20. Delete vectors with maximum equal to value                         \n"
          "   ▶ 9. Get the sum of elements of all vectors  ▶ 21. Update all vectors by adding a scalar               \n"
          "   ▶ 10. Get the vector sum of all vectors      ▶ 22. Update color of vector with name_id                 \n"
          "   ▶ 11. Get the elements with a given sum      ▶ 23. Update vectors of type with color                   \n"
          )


def console_vector_menu():
    print_vector_menu()
    commands = {1: console_add_scalar,
                2: console_add_vectors,
                3: console_subtract_vectors,
                4: console_multiply_vectors,
                5: console_sum_of_elements,
                6: console_product_of_elements,
                7: console_average_of_elements,
                8: console_minimum_of_vector,
                9: console_maximum_of_vector
                }
    while True:
        try:
            boolean = False
            command = int(input("Enter command: "))
            if 1 <= command <= 9:
                print("If you want to, you can use a pre-written vector.")
                trying = input("Do you want to? (y/n): ")
                if trying == "y":
                    boolean = True
                elif trying == "n":
                    boolean = False
            if command == 0:
                return
            elif command in commands.keys():
                commands[command](boolean)
            else:
                print("Invalid command!\n")
        except ValueError as ve:
            print(ve)


def console_vector_list_menu():
    repo = VectorRepository()

    boolean = input("   ● Do you want a pre-written repository? y/n: ")
    if boolean == '0':
        return
    while boolean != "y" and boolean != "n":
        print("Invalid command!")
        boolean = input("   ● Do you want a pre-written repository? y/n: ")
        if boolean == '0':
            return
    if boolean == "y":
        repo.add(MyVector(1, "r", 1, [1, 2, 3]))
        repo.add(MyVector(2, "b", 1, [1, 1, 1]))
        repo.add(MyVector(3, "g", 1, [1, 2, 4]))
        repo.add(MyVector(4, "y", 1, [1, 2, 3]))
        repo.add(MyVector(5, "m", 1, [1, 2, 3]))
        repo.add(MyVector(6, "r", 2, [1, 2, 3]))
        repo.add(MyVector(7, "b", 3, [1, 2, 3]))
        repo.add(MyVector(8, "g", 4, [1, 2, 3]))
        repo.add(MyVector(9, "y", 5, [1, 2, 3]))
        repo.add(MyVector(10, "m", 10, [1, 2, 3]))

    print_vector_list_menu()
    commands = {1: console_add_vector,
                2: console_get_all_vectors,
                3: console_get_vector_at_index,
                4: console_update_vector_at_index,
                5: console_update_vector_by_name_id,
                6: console_delete_vector_at_index,
                7: console_delete_vector_by_name_id,
                8: console_plot_vectors,
                9: console_sum_of_all_elements,
                10: console_get_vector_sum_of_all_vectors,
                11: console_get_elements_with_given_sum,
                12: console_get_vectors_with_minimum_less_than_value,
                13: console_get_sum_of_elements_of_vectors_of_color,
                14: console_get_max_of_vectors_with_sum_greater_than_value,
                15: console_get_min_of_all_vectors,
                16: console_get_list_of_values_multiplication_of_consecutive_vectors,
                17: console_delete_all_vectors,
                19: console_delete_vectors_between_two_indexes,
                20: console_delete_vectors_with_maximum_equal_to_value,
                21: console_add_scalar_to_all,
                22: console_update_color_of_vectors_with_name_id,
                23: console_update_vectors_of_type_by_setting_color
                }
    while True:
        try:
            command = int(input("   ● Enter command: "))
            if command == 0:
                return
            elif command in commands.keys():
                commands[command](repo)
            elif command == 18:
                boolean = input("Do you want to delete vectors of color or vectors with product of elements greater than value? (c/v): ")
                while boolean != "c" and boolean != "v":
                    print("Invalid command!")
                    boolean = input("Do you want to delete vectors of color or vectors with product of elements greater than value? (c/v): ")
                if boolean == "c":
                    console_delete_vectors_of_color(repo)
                elif boolean == "v":
                    console_delete_vectors_with_product_of_elements_greater_than_value(repo)
            else:
                print("Invalid command!\n")
        except ValueError as ve:
            print(ve)


def console():
    while True:
        print_menu()
        try:
            command = int(input("Enter command: "))
            if command == 0:
                print("Bye!")
                return
            elif command == 1:
                console_vector_menu()
            elif command == 2:
                console_vector_list_menu()
            else:
                print("Invalid command!\n")
        except ValueError as ve:
            print(ve)
