import numpy as np

'''
schimbari la VALUES in __init__, get_values, set_values, add_scalar, add_vector, sub_vector, mul_vector, 
                       sum_of_elements, product_of_elements, average_of_elements, minimum, maximum
'''


class MyVectorNP:
    def __init__(self, name_id, color, thistype, values):
        """
        Creates a new vector with name_id, color, type and values
        """
        self.__name_id = name_id
        self.__color = color
        self.__type = thistype
        self.__values = np.array(values[:])

    def validate(self):
        """
        Validates the vector
        In: -
        Out: error message
        Error: -
        """
        er = ""
        if not isinstance(self.__name_id, int):
            er += "Invalid name_id! Should be integer!\n"
        elif self.__name_id < 0:
            er += "Invalid name_id! Should be greater or equal to 0!\n"
        if self.__color not in ['r', 'g', 'b', 'y', 'm']:
            er += "Invalid color! Color must be either r, b, y, g, m!\n"
        if not isinstance(self.__type, int):
            er += "Invalid type! Should be integer!\n"
        elif self.__type < 1:
            er += "Invalid type! Should be greater or equal to 1!\n"
        ok = 0
        for i in self.__values:
            if not isinstance(i, int) and not isinstance(i, float):
                ok = 1
        if ok == 1:
            er += "Invalid values! Should be integers or floats!\n"
        if er != "":
            raise ValueError(er)
        return 0

    def get_name_id(self):
        """
        Returns the name_id of the vector
        In: -
        Out: the name_id of the vector
        Error: -
        """
        return self.__name_id

    def get_color(self):
        """
        Returns the color of the vector
        In: -
        Out: the color of the vector
        Error: -
        """
        return self.__color

    def get_type(self):
        """
        Returns the type of the vector
        In: -
        Out: the type of the vector
        Error: -
        """
        return self.__type

    def get_values(self):
        """
        Returns the values of the vector
        In: -
        Out: the values of the vector
        Error: -
        """
        return self.__values[:]

    def set_name_id(self, new_name_id):
        """
        Sets a new name_id for the vector
        In: new_name_id - int
        Out: -
        Error: ValueError if new_name_id is not integer or is negative
        """
        if not isinstance(new_name_id, int):
            raise ValueError("Should be integer!\n")
        if new_name_id < 0:
            raise ValueError("Invalid name_id!\n")
        self.__name_id = new_name_id

    def set_color(self, new_color):
        """
        Sets a new color for the vector
        In: new_color - string (one from: 'r', 'g', 'b', 'y', 'm')
        Out: -
        Error: ValueError if new_color is not one of the above
        """
        if new_color in ['r', 'g', 'b', 'y', 'm']:
            self.__color = new_color
        else:
            raise ValueError("Invalid color! Colour must be either r, b, y, g, m!\n")

    def set_type(self, new_type):
        """
        Sets a new type for the vector
        In: new_type - int
        Out: -
        Error: ValueError if new_type is not integer or is negative
        """
        if isinstance(new_type, int) and new_type >= 1:
            self.__type = new_type
        else:
            raise ValueError("Invalid type!\n")

    def set_values(self, new_values):
        """
        Sets new values for the vector
        In: new_values - list of integers or floats
        Out: -
        Error: ValueError if new_values is not a list of integers or floats
        """
        for i in new_values:
            if not isinstance(i, int) or not isinstance(i, float):
                raise ValueError("Invalid values!\n")
        self.__values = np.array(new_values[:])

    def __str__(self):
        """
        Returns a string representation of the vector
        In: -
        Out: string
        Error: -
        """
        return "Vector " + self.get_name_id() + \
               " with color " + self.get_color() + \
               " and type " + str(self.get_type()) + \
               " has values " + str(self.get_values())

    # 1. Scalar operations

    def add_scalar(self, scalar):
        """
        Adds a scalar to the vector
        In: scalar - integer or float
        Out: -
        Error: ValueError if scalar is not integer or float
        """
        if not isinstance(scalar, (int, float)):
            raise ValueError("Invalid scalar!\n")
        self.set_values(self.get_values() + scalar)

    # 2. Vector operations

    def add_vector(self, other):
        """
        Adds two vectors
        In: other - vector
        Out: myvalues - list of integers and/or floats, sum of the values of the two vectors
        Error: ValueError if other is not a vector or if the vectors have different lengths
        """
        if not isinstance(other, MyVectorNP):
            raise ValueError("Invalid type!\n")
        my_values = self.get_values()
        other_values = other.get_values()
        if len(my_values) != len(other_values):
            raise ValueError("Different lenghts of value lists!\n")
        return my_values + other_values

    def sub_vector(self, other):
        """
        Subtracts two vectors
        In: other - vector
        Out: myvalues - list of integers and/or floats, difference of the values of the two vectors
        Error: ValueError if other is not a vector or if the vectors have different lengths
        """
        if not isinstance(other, MyVectorNP):
            raise ValueError("Invalid type!\n")
        my_values = self.get_values()
        other_values = other.get_values()
        if len(my_values) != len(other_values):
            raise ValueError("Different lenghts of value lists!\n")
        return my_values - other_values

    def mul_vector(self, other):
        """
        Multiplies two vectors
        In: other - vector
        Out: mul - integer or float, multiplication of the values of the two vectors
        Error: ValueError if other is not a vector or if the vectors have different lengths
        """
        if not isinstance(other, MyVectorNP):
            raise ValueError("Invalid type!\n")
        my_values = self.get_values()
        other_values = other.get_values()
        if len(my_values) != len(other_values):
            raise ValueError("Different lenghts of value lists!\n")
        return np.sum(my_values * other_values)

    # 3. Reduction operations

    def sum_of_elements(self):
        """
        Returns the sum of the elements of the vector
        In: -
        Out: summ - integer or float, sum of the elements of the vector
        Error: ValueError if the list is empty
        """
        myvalues = self.get_values()
        if len(myvalues) == 0:
            raise ValueError("The list is empty!\n")
        return np.sum(myvalues)

    def prod_of_elements(self):
        """
        Returns the product of the elements of the vector
        In: -
        Out: prod - integer or float, product of the elements of the vector
        Error: ValueError if the list is empty
        """
        myvalues = self.get_values()
        if len(myvalues) == 0:
            raise ValueError("The list is empty!\n")
        return np.prod(myvalues)

    def average_of_elements(self):
        """
        Returns the average of the elements of the vector
        In: -
        Out: avg - integer, average of the elements of the vector
        Error: ValueError if the list is empty
        """
        myvalues = self.get_values()
        if len(myvalues) == 0:
            raise ValueError("The list is empty!\n")
        return np.average(myvalues)

    def minimum_of_elements(self):
        """
        Returns the minimum of the elements of the vector
        In: -
        Out: mini - integer or float, minimum of the elements of the vector
        Error: ValueError if the list is empty
        """
        myvalues = self.get_values()
        if len(myvalues) == 0:
            raise ValueError("The list is empty!\n")
        return np.amin(myvalues)

    def maximum_of_elements(self):
        """
        Returns the maximum of the elements of the vector
        In: -
        Out: maxi - integer or float, maximum of the elements of the vector
        Error: ValueError if the list is empty
        """
        myvalues = self.get_values()
        if len(myvalues) == 0:
            raise ValueError("The list is empty!\n")
        return np.amax(myvalues)


# p1 = MyVectorNP(1, 'r', 1, [1, 2.0, -3])
# print(p1.maximum_of_elements())
# print(p1.minimum_of_elements())
#
# p2 = MyVectorNP(2, 'g', 1, [1, 2.0, 4])
# print(p2.average_of_elements())
