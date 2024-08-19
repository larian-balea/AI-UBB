from domain.my_vector import MyVector
import matplotlib.pyplot as plt


class VectorRepository:
    def __init__(self, initial_values=None):
        """
        Initializes the repository
        """
        if initial_values is None:
            initial_values = []
        self.__vectors = []
        if initial_values is not None:
            for value in initial_values:
                if isinstance(value, MyVector):
                    self.__vectors.append(value)

    def __str__(self):
        """
        String representation of the repository
        In: -
        Out: string
        Error: ValueError if the repository is empty
        """
        repo_str = ""
        all_vectors = self.get_all()
        for vector in all_vectors:
            repo_str += str(vector) + "\n"
        if repo_str == "":
            raise ValueError("Empty repository!\n")
        return repo_str

    def check_if_exists(self, vector):
        """
        Checks if a vector already exists in the repository
        In: vector - MyVector
        Out: True if the vector already exists(if it has the same name_id), False otherwise
        Error: -
        """
        if vector.get_name_id() in [v.get_name_id() for v in self.__vectors]:
            return True
        return False

    # 1. Add
    def add(self, vector):
        """
        Adds a vector to the repository
        In: vector - MyVector
        Out: -
        Error: ValueError if the vector is not of type MyVector, is not valid or already exists
        """
        if not isinstance(vector, MyVector):
            raise ValueError("Invalid type!\n")
        er = vector.validate()
        if er != 0:
            raise ValueError(er)
        if self.check_if_exists(vector):
            raise ValueError("Vector already exists!\n")
        self.__vectors.append(vector)

    # 2. Get all vectors
    def get_all(self):
        """
        Returns all vectors in the repository
        In: -
        Out: list of MyVector
        Error: -
        """
        return self.__vectors

    # 3. Get vector at index
    def get_at_index(self, index):
        """
        Returns the vector at the given index
        In: index - int
        Out: MyVector
        Error: ValueError if index is not valid
        """
        if not isinstance(index, int):
            raise ValueError("Invalid index! Should be integer!\n")
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        if index < 0 or index >= len(vectors):
            raise ValueError("Invalid index! Should be between 0 and lenght of list!\n")
        return self.get_all()[index]

    # 4. Update vector at index
    def update_at_index(self, index, vector):
        """
        Updates the vector at the given index
        In: index - int, vector - MyVector
        Out: -
        Error: ValueError if index is not valid,
                          if vector is not of type MyVector, is not valid or already exists
        """
        if not isinstance(index, int):
            raise ValueError("Invalid index! Should be integer!\n")
        if not isinstance(vector, MyVector):
            raise ValueError("Invalid type!\n")
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        if index < 0 or index >= len(vectors):
            raise ValueError("Invalid index! Should be between 0 and lenght of list!\n")
        er = vector.validate()
        if er != 0:
            raise ValueError(er)
        if self.check_if_exists(vector):
            raise ValueError("Vector already exists!\n")
        vectors[index].set_name_id(vector.get_name_id())
        vectors[index].set_color(vector.get_color())
        vectors[index].set_type(vector.get_type())
        vectors[index].set_values(vector.get_values())

    # 5. Update vector by name_id
    def update_by_name_id(self, vector):
        """
        Updates the vector with the given name_id
        In: vector - MyVector
        Out: -
        Error: ValueError if vector is not of type MyVector, is not valid or already exists
        """
        if not isinstance(vector, MyVector):
            raise ValueError("Invalid type!\n")
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        er = vector.validate()
        if er != 0:
            raise ValueError(er)
        if not self.check_if_exists(vector):
            raise ValueError("Vector doesn't exist!\n")
        for v in vectors:
            if v.get_name_id() == vector.get_name_id():
                v.set_color(vector.get_color())
                v.set_type(vector.get_type())
                v.set_values(vector.get_values())

    # 6. Delete vector at index
    def delete_at_index(self, index):
        """
        Deletes the vector at the given index
        In: index - int
        Out: -
        Error: ValueError if index is not valid
        """
        if not isinstance(index, int):
            raise ValueError("Invalid index! Should be integer!\n")
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        if index < 0 or index >= len(self.get_all()):
            raise ValueError("Invalid index! Should be between 0 and lenght of list!\n")
        del vectors[index]

    # 7. Delete vector by name_id
    def delete_by_name_id(self, name_id):
        """
        Deletes the vector with the given name_id
        In: name_id - int
        Out: -
        Error: ValueError if name_id is not valid
        """
        if not isinstance(name_id, int):
            raise ValueError("Invalid name_id! Should be integer!\n")
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        if name_id < 0:
            raise ValueError("Invalid name_id! Should be greater or equal to 0!\n")
        updated_vectors = []
        for vector in vectors:
            if vector.get_name_id() != name_id:
                updated_vectors.append(vector)
        if len(updated_vectors) == len(vectors):
            raise ValueError("Name_id not in list!\n")
        self.__vectors = updated_vectors

    # 8. Plot all vectors in a chart
    def chart(self):
        """
        Plots all vectors in a chart
        In: -
        Out: -
        Error: -
        """
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        plt.grid()
        m = {
            1: "o",
            2: "s",
            3: "^",
            4: "D"
        }
        for vector in vectors:
            this_type = vector.get_type()
            if this_type not in m.keys():
                this_type = "D"
            else:
                this_type = m[this_type]
            plt.plot([i for i in range(len(vector.get_values()))],
                     vector.get_values(),
                     c=vector.get_color(),
                     marker=this_type
                     )
        plt.show()

    # 9. Get the sum of elements of all vectors
    def sum_of_all_elements(self):
        """
        Returns the sum of elements of all vectors
        In: -
        Out: summ - float
        Errors: ValueError if there are no vectors
        """
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        summ = 0
        for vector in vectors:
            summ += vector.sum_of_elements()
        return summ

    # 10. Get the vector sum of all vectors
    def get_vector_sum_of_all_vectors(self):
        """
        Returns the vector sum of all vectors
        In: -
        Out: vector_sum - list of float
        Errors: ValueError if there are no vectors
        """
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        vector_sum = MyVector(1, 'r', 1, [0 for _ in range(len(vectors[0].get_values()))])
        for vector in vectors:
            vector_sum.add_vector(vector)
        return vector_sum.get_values()

    # 11. Get elements with given sum of elements
    def get_elements_with_given_sum(self, summ):
        """
        Returns all vectors with the given sum of elements
        In: sum - int
        Out: list of MyVector
        Error: ValueError if summ is not valid
        """
        if not isinstance(summ, (int, float)):
            raise ValueError("Invalid sum! Should be integer or float!\n")
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        vectors_with_given_sum = []
        for vector in vectors:
            if summ == vector.sum_of_elements():
                vectors_with_given_sum.append(vector)
        return vectors_with_given_sum

    # 12. Get vectors with minimum less than value
    def get_vectors_with_minimum_less_than_value(self, value):
        """
        Returns all vectors with minimum less than value
        In: value - int
        Out: list of MyVector
        Error: ValueError if value is not valid
        """
        if not isinstance(value, (int, float)):
            raise ValueError("Invalid value! Should be integer or float!\n")
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        vectors_with_minimum_less_than_value = []
        for vector in vectors:
            if vector.minimum_of_elements() < value:
                vectors_with_minimum_less_than_value.append(vector)
        return vectors_with_minimum_less_than_value

    # 13. Get sum of elements of vectors of color
    def get_sum_of_elements_of_vectors_of_color(self, color):
        """
        Returns the sum of elements of vectors of color
        In: color - string
        Out: sum - int
        Error: ValueError if color is not valid
        """
        if color not in ['r', 'g', 'b', 'y', 'm']:
            raise ValueError("Invalid color! Color must be either r, b, y, g, m!\n")
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        summ = 0
        for vector in vectors:
            if vector.get_color() == color:
                summ += vector.sum_of_elements()
        return summ

    # 14. Get the max of vectors with sum greater than value
    def get_max_of_vectors_with_sum_greater_than_value(self, value):
        """
        Returns the max of vectors with sum greater than value
        In: value - int
        Out: max - float/int
        Error: ValueError if value is not valid
        """
        if not isinstance(value, (int, float)):
            raise ValueError("Invalid value! Should be integer or float!\n")
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        maxn = vectors[0]
        for vector in vectors:
            if vector.sum_of_elements() > value:
                if vector.average_of_elements() > maxn.average_of_elements():
                    maxn = vector
        return maxn.get_values()

    # 15. Get the min of all vectors
    def get_min_of_all_vectors(self):
        """
        Returns the minimum vector(by average of values)
        In: -
        Out: min - float/int
        Errors: ValueError if there are no vectors
        """
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        minn = vectors[0]
        for vector in vectors:
            if vector.average_of_elements() < minn.average_of_elements():
                minn = vector
        return minn.get_values()

    # 16. Get list of values multiplication of consecutive vectors
    def get_list_of_values_multiplication_of_consecutive_vectors(self):
        """
        Returns a list of values multiplication of consecutive vectors
        In: -
        Out: list of float
        Errors: ValueError if there are no vectors
        """
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        list_of_values_multiplication_of_consecutive_vectors = []
        for i in range(len(vectors) - 1):
            list_of_values_multiplication_of_consecutive_vectors.append(vectors[i].mul_vector(vectors[i + 1]))
        return list_of_values_multiplication_of_consecutive_vectors

    # 17. Delete all vectors
    def delete_all(self):
        """
        Deletes all vectors
        In: -
        Out: -
        Error: -
        """
        self.__vectors = []

    # 18,1. Delete vectors of color
    def delete_vectors_of_color(self, color):
        """
        Deletes all vectors of color
        In: color - string
        Out: -
        Error: ValueError if color is not valid
        """
        if color not in ['r', 'g', 'b', 'y', 'm']:
            raise ValueError("Invalid color! Color must be either r, b, y, g, m!\n")
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        updated_vectors = []
        for vector in vectors:
            if vector.get_color() != color:
                updated_vectors.append(vector)
        self.__vectors = updated_vectors

    # 18,2. Delete vectors with product of elements greater than value
    def delete_vectors_with_product_of_elements_greater_than_value(self, value):
        """
        Deletes all vectors with product of elements greater than value
        In: value - int
        Out: -
        Error: ValueError if value is not valid
        """
        if not isinstance(value, (int, float)):
            raise ValueError("Invalid value! Should be integer or float!\n")
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        updated_vectors = []
        for vector in vectors:
            if vector.prod_of_elements() <= value:
                updated_vectors.append(vector)
        self.__vectors = updated_vectors

    # 19. Delete vectors between two indexes
    def delete_vectors_between_two_indexes(self, index1, index2):
        """
        Deletes all vectors between the given indexes
        In: index1 - int
            index2 - int
        Out: -
        Error: ValueError if index1 or index2 are not valid
        """
        if not isinstance(index1, int):
            raise ValueError("Invalid index1! Should be integer!\n")
        if not isinstance(index2, int):
            raise ValueError("Invalid index2! Should be integer!\n")
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        if index1 < 0 or index1 >= len(self.get_all()):
            raise ValueError("Invalid index1! Should be between 0 and lenght of list-1!\n")
        if index2 < 0 or index2 >= len(self.get_all()):
            raise ValueError("Invalid index2! Should be between 0 and lenght of list-1!\n")

        if index1 > index2:
            index1, index2 = index2, index1
        updated_vectors = []
        for i in range(len(vectors)):
            if i < index1 or i > index2:
                updated_vectors.append(vectors[i])
        self.__vectors = updated_vectors

    # 20. Delete vectors with maximum equal to value
    def delete_vectors_with_maximum_equal_to_value(self, value):
        """
        Deletes all vectors with maximum equal to value
        In: value - int
        Out: -
        Error: ValueError if value is not valid
        """
        if not isinstance(value, (int, float)):
            raise ValueError("Invalid value! Should be integer or float!\n")
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        updated_vectors = []
        for vector in vectors:
            if vector.maximum_of_elements() != value:
                updated_vectors.append(vector)
        self.__vectors = updated_vectors

    # 21. Update all vectors by adding a scalar
    def add_scalar_to_all(self, scalar):
        """
        It adds a float or int scalar to all elements in all vectors
        In: scalar - float
        Out: -
        Error: ValueError if there are no vectors or scalar is not float
        """
        if not isinstance(scalar, (int, float)):
            raise ValueError("Invalid scalar! Should be integer or float!\n")
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        for vector in vectors:
            vector.add_scalar(scalar)

    # 22. Update color of vector with name_id
    def update_color_of_vectors_with_name_id(self, name_id, new_color):
        """
        Updates the color of vector with name_id
        In: name_id - int
            new_color - string
        Out: -
        Error: ValueError if name_id is not valid or new_color is not valid
        """
        if not isinstance(name_id, int):
            raise ValueError("Invalid name_id! Should be integer!\n")
        elif name_id < 0:
            raise ValueError("Invalid name_id! Should be greater or equal to 0!\n")
        if new_color not in ['r', 'g', 'b', 'y', 'm']:
            raise ValueError("Invalid color! Color must be either r, b, y, g, m!\n")
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        for vector in vectors:
            if vector.get_name_id() == name_id:
                vector.set_color(new_color)

    # 23. Update vectors of a given type by setting their color to a given color
    def update_vectors_of_type_by_setting_color(self, given_type, given_color):
        """
        Updates all vectors of a given type by setting their color to a given color
        In: given_type - int
            given_color - string
        Out: -
        Error: ValueError if given_type or given_color are not valid
        """
        if not isinstance(given_type, int):
            raise ValueError("Invalid type! Should be integer!\n")
        if given_type < 0:
            raise ValueError("Invalid type! Should be greater or equal to 0!\n")
        if given_color not in ['r', 'g', 'b', 'y', 'm']:
            raise ValueError("Invalid color! Color must be either r, g, b, y, m!\n")
        vectors = self.get_all()
        if len(vectors) == 0:
            raise ValueError("The list is empty!\n")
        for vector in vectors:
            if vector.get_type() == given_type:
                vector.set_color(given_color)


# v1 = MyVector(1, 'r', 3, [1, 2, 3, 4])
# v2 = MyVector(2, 'g', 2, [4, 5, 6])
# repo = VectorRepository([v1, v2])
# repo.chart()
#
# v3 = MyVector(3, 'b', 1, [7, 8, 9, 10])
# repo.add(v3)
# print(repo.check_if_exists(v3))
# print(repo.get_all())
# print(repo)
#
# v4 = MyVector(4, 'y', 4, [11, 12, 13, 14])
# v5 = MyVector(5, 'y', 4, [11, 12, 13, 14])
# repo.add(v4)
#
# print(repo.get_at_index(0))
# repo.update_at_index(0, v5)
# print(repo.get_at_index(0))
