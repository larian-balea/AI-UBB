from domain.my_vector import MyVector
from domain.my_vector_np import MyVectorNP
from repository.vector_repository import VectorRepository
import unittest


class VectorTests(unittest.TestCase):

    def test_validate(self):
        """
        this will test the validate function
        """
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        assert self.vector1.validate() == 0

        try:
            MyVector('agua', 'r', 1, [1, 2, 3]).validate()
            assert False
        except ValueError as error:
            assert str(error) == "Invalid name_id! Should be integer!\n"

        try:
            MyVector(-1, 'r', 1, [1, 2, 3]).validate()
            assert False
        except ValueError as error:
            assert str(error) == "Invalid name_id! Should be greater or equal to 0!\n"

        try:
            MyVector(1, 'a', 1, [1, 2, 3]).validate()
            assert False
        except ValueError as error:
            assert str(error) == "Invalid color! Color must be either r, b, y, g, m!\n"

        try:
            MyVector(1, 'r', 'agua', [1, 2, 3]).validate()
            assert False
        except ValueError as error:
            assert str(error) == "Invalid type! Should be integer!\n"

        try:
            MyVector(1, 'r', 0, [1, 2, 3]).validate()
            assert False
        except ValueError as error:
            assert str(error) == "Invalid type! Should be greater or equal to 1!\n"

        try:
            MyVector(1, 'r', 1, [1, 2, 3, 'a']).validate()
            assert False
        except ValueError as error:
            assert str(error) == "Invalid values! Should be integers or floats!\n"

        try:
            MyVector(-1, 'a', 0, ['a']).validate()
            assert False
        except ValueError as error:
            assert str(error) == "Invalid name_id! Should be greater or equal to 0!\n" \
                                 "Invalid color! Color must be either r, b, y, g, m!\n" \
                                 "Invalid type! Should be greater or equal to 1!\n" \
                                 "Invalid values! Should be integers or floats!\n"

    def test_getters(self):
        """
            this will test the getters
        """
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        assert self.vector1.get_name_id() == 1
        assert self.vector1.get_color() == 'r'
        assert self.vector1.get_type() == 1
        assert self.vector1.get_values() == [1, 2, 3]

    def test_setters(self):
        """
            this will test the setters
        """
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector1.set_name_id(2)
        assert self.vector1.get_name_id() == 2
        self.vector1.set_color('b')
        assert self.vector1.get_color() == 'b'
        self.vector1.set_type(2)
        assert self.vector1.get_type() == 2
        self.vector1.set_values([1, 2, 3, 4])
        assert self.vector1.get_values() == [1, 2, 3, 4]

        try:
            self.vector1.set_name_id(-1)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid name_id!\n"

        try:
            self.vector1.set_color('a')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid color! Color must be either r, b, y, g, m!\n"

        try:
            self.vector1.set_type(-1)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid type!\n"

        try:
            self.vector1.set_values([1, 2, 3, 4, "a"])
            assert False
        except ValueError as error:
            assert str(error) == "Invalid values!\n"

    def test_string(self):
        """
            this will test the string function
        """
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [3, 2, 1])
        assert str(self.vector1) == "Vector " + str(self.vector1.get_name_id()) + \
                                    " with color " + self.vector1.get_color() + \
                                    " and type " + str(self.vector1.get_type()) + \
                                    " has values " + str(self.vector1.get_values())

        assert str(self.vector2) == "Vector " + str(self.vector2.get_name_id()) + \
                                    " with color " + self.vector2.get_color() + \
                                    " and type " + str(self.vector2.get_type()) + \
                                    " has values " + str(self.vector2.get_values())

    def test_add_scalar(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [3, 2, 1])

        self.vector1.add_scalar(2)
        assert self.vector1.get_values() == [3, 4, 5]

        self.vector2.add_scalar(1.5)
        assert self.vector2.get_values() == [4.5, 3.5, 2.5]

        try:
            assert self.vector2.add_scalar('a')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid scalar!\n"

    def test_add_vector(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [3, 2, 1])
        self.vector3 = MyVector(3, 'b', 3, [1, 2, 3, 4.5])
        self.vector1.add_vector(self.vector2)
        assert self.vector1.get_values() == [4, 4, 4]

        try:
            self.vector1.add_vector('Bud Spencer')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid type!\n"

        try:
            self.vector1.add_vector(self.vector3)
            assert False
        except ValueError as error:
            assert str(error) == "Different lenghts of value lists!\n"

    def test_sub_vector(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [3, 2, 1])
        self.vector3 = MyVector(3, 'b', 3, [1, 2, 3, 4.5])
        self.vector1.sub_vector(self.vector2)
        assert self.vector1.get_values() == [-2, 0, 2]

        try:
            self.vector1.sub_vector('Bud Spencer')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid type!\n"

        try:
            self.vector1.sub_vector(self.vector3)
            assert False
        except ValueError as error:
            assert str(error) == "Different lenghts of value lists!\n"

    def test_mul_vector(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [3, 2, 1])
        self.vector3 = MyVector(3, 'b', 3, [1, 2, 3, 4.5])
        assert self.vector1.mul_vector(self.vector2) == 10

        try:
            assert self.vector1.mul_vector('Bud Spencer')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid type!\n"

        try:
            assert self.vector1.mul_vector(self.vector3)
            assert False
        except ValueError as error:
            assert str(error) == "Different lenghts of value lists!\n"

    def test_sum_of_elements(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector3 = MyVector(3, 'b', 3, [1, 2, 3, 4.5])
        self.vector4 = MyVector(4, 'y', 4, [])
        assert self.vector1.sum_of_elements() == 6

        assert self.vector3.sum_of_elements() == 10.5

        try:
            assert self.vector4.sum_of_elements()
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

    def test_prod_of_elements(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector3 = MyVector(3, 'b', 3, [1, 2, 3, 4.5])
        self.vector4 = MyVector(4, 'y', 4, [])
        assert self.vector1.prod_of_elements() == 6

        assert self.vector3.prod_of_elements() == 27

        try:
            assert self.vector4.prod_of_elements()
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

    def test_average_of_elements(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector3 = MyVector(3, 'b', 3, [1, 2, 3, 4.5])
        self.vector4 = MyVector(4, 'y', 4, [])
        assert self.vector1.average_of_elements() == 2

        assert self.vector3.average_of_elements() == 2.625

        try:
            assert self.vector4.average_of_elements()
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

    def test_minimum_of_elements(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector3 = MyVector(3, 'b', 3, [1, 2, 3, 4.5])
        self.vector4 = MyVector(4, 'y', 4, [])
        assert self.vector1.minimum_of_elements() == 1

        assert self.vector3.minimum_of_elements() == 1

        try:
            assert self.vector4.minimum_of_elements()
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

    def test_maximum_of_elements(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector3 = MyVector(3, 'b', 3, [1, 2, 3, 4.5])
        self.vector4 = MyVector(4, 'y', 4, [])
        assert self.vector1.maximum_of_elements() == 3

        assert self.vector3.maximum_of_elements() == 4.5

        try:
            assert self.vector4.maximum_of_elements()
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

    def test_vector_domain(self):
        self.test_validate()
        self.test_getters()
        self.test_setters()
        self.test_add_scalar()
        self.test_add_vector()
        self.test_sub_vector()
        self.test_mul_vector()
        self.test_sum_of_elements()
        self.test_prod_of_elements()
        self.test_average_of_elements()
        self.test_minimum_of_elements()
        self.test_maximum_of_elements()


class VectorNPTests(unittest.TestCase):
    def test_validate(self):
        """
        this will test the validate function
        """
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        assert self.vector1.validate() == 0

        try:
            MyVector('agua', 'r', 1, [1, 2, 3]).validate()
            assert False
        except ValueError as error:
            assert str(error) == "Invalid name_id! Should be integer!\n"

        try:
            MyVector(-1, 'r', 1, [1, 2, 3]).validate()
            assert False
        except ValueError as error:
            assert str(error) == "Invalid name_id! Should be greater or equal to 0!\n"

        try:
            MyVector(1, 'a', 1, [1, 2, 3]).validate()
            assert False
        except ValueError as error:
            assert str(error) == "Invalid color! Color must be either r, b, y, g, m!\n"

        try:
            MyVector(1, 'r', 'agua', [1, 2, 3]).validate()
            assert False
        except ValueError as error:
            assert str(error) == "Invalid type! Should be integer!\n"

        try:
            MyVector(1, 'r', 0, [1, 2, 3]).validate()
            assert False
        except ValueError as error:
            assert str(error) == "Invalid type! Should be greater or equal to 1!\n"

        try:
            MyVector(1, 'r', 1, [1, 2, 3, 'a']).validate()
            assert False
        except ValueError as error:
            assert str(error) == "Invalid values! Should be integers or floats!\n"

        try:
            MyVector(-1, 'a', 0, ['a']).validate()
            assert False
        except ValueError as error:
            assert str(error) == "Invalid name_id! Should be greater or equal to 0!\n" \
                                 "Invalid color! Color must be either r, b, y, g, m!\n" \
                                 "Invalid type! Should be greater or equal to 1!\n" \
                                 "Invalid values! Should be integers or floats!\n"

    def test_getters(self):
        """
            this will test the getters
        """
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        assert self.vector1.get_name_id() == 1
        assert self.vector1.get_color() == 'r'
        assert self.vector1.get_type() == 1
        assert self.vector1.get_values() == [1, 2, 3]

    def test_setters(self):
        """
            this will test the setters
        """
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector1.set_name_id(2)
        assert self.vector1.get_name_id() == 2
        self.vector1.set_color('b')
        assert self.vector1.get_color() == 'b'
        self.vector1.set_type(2)
        assert self.vector1.get_type() == 2
        self.vector1.set_values([1, 2, 3, 4])
        assert self.vector1.get_values() == [1, 2, 3, 4]

        try:
            self.vector1.set_name_id(-1)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid name_id!\n"

        try:
            self.vector1.set_color('a')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid color! Color must be either r, b, y, g, m!\n"

        try:
            self.vector1.set_type(-1)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid type!\n"

        try:
            self.vector1.set_values([1, 2, 3, 4, "a"])
            assert False
        except ValueError as error:
            assert str(error) == "Invalid values!\n"

    def test_string(self):
        """
            this will test the string function
        """
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [3, 2, 1])
        assert str(self.vector1) == "Vector " + str(self.vector1.get_name_id()) + \
                                    " with color " + self.vector1.get_color() + \
                                    " and type " + str(self.vector1.get_type()) + \
                                    " has values " + str(self.vector1.get_values())

        assert str(self.vector2) == "Vector " + str(self.vector2.get_name_id()) + \
                                    " with color " + self.vector2.get_color() + \
                                    " and type " + str(self.vector2.get_type()) + \
                                    " has values " + str(self.vector2.get_values())

    def test_add_scalar(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [3, 2, 1])

        self.vector1.add_scalar(2)
        assert self.vector1.get_values() == [3, 4, 5]

        self.vector2.add_scalar(1.5)
        assert self.vector2.get_values() == [4.5, 3.5, 2.5]

        try:
            assert self.vector2.add_scalar('a')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid scalar!\n"

    def test_add_vector(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [3, 2, 1])
        self.vector3 = MyVector(3, 'b', 3, [1, 2, 3, 4.5])
        self.vector1.add_vector(self.vector2)
        assert self.vector1.get_values() == [4, 4, 4]

        try:
            self.vector1.add_vector('Bud Spencer')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid type!\n"

        try:
            self.vector1.add_vector(self.vector3)
            assert False
        except ValueError as error:
            assert str(error) == "Different lenghts of value lists!\n"

    def test_sub_vector(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [3, 2, 1])
        self.vector3 = MyVector(3, 'b', 3, [1, 2, 3, 4.5])
        self.vector1.sub_vector(self.vector2)
        assert self.vector1.get_values() == [-2, 0, 2]

        try:
            self.vector1.sub_vector('Bud Spencer')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid type!\n"

        try:
            self.vector1.sub_vector(self.vector3)
            assert False
        except ValueError as error:
            assert str(error) == "Different lenghts of value lists!\n"

    def test_mul_vector(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [3, 2, 1])
        self.vector3 = MyVector(3, 'b', 3, [1, 2, 3, 4.5])
        assert self.vector1.mul_vector(self.vector2) == 10

        try:
            assert self.vector1.mul_vector('Bud Spencer')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid type!\n"

        try:
            assert self.vector1.mul_vector(self.vector3)
            assert False
        except ValueError as error:
            assert str(error) == "Different lenghts of value lists!\n"

    def test_sum_of_elements(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector3 = MyVector(3, 'b', 3, [1, 2, 3, 4.5])
        self.vector4 = MyVector(4, 'y', 4, [])
        assert self.vector1.sum_of_elements() == 6

        assert self.vector3.sum_of_elements() == 10.5

        try:
            assert self.vector4.sum_of_elements()
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

    def test_prod_of_elements(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector3 = MyVector(3, 'b', 3, [1, 2, 3, 4.5])
        self.vector4 = MyVector(4, 'y', 4, [])
        assert self.vector1.prod_of_elements() == 6

        assert self.vector3.prod_of_elements() == 27

        try:
            assert self.vector4.prod_of_elements()
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

    def test_average_of_elements(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVectorNP(2, 'b', 2, [1, 2, 3, 4.5])
        self.vector3 = MyVectorNP(3, 'y', 3, [])
        assert self.vector1.average_of_elements() == 2

        assert self.vector2.average_of_elements() == 2.625

        try:
            assert self.vector3.average_of_elements()
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

    def test_minimum_of_elements(self):
        self.vector1 = MyVectorNP(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVectorNP(2, 'b', 2, [0, 1, 2, 3, 4.5])
        self.vector3 = MyVectorNP(3, 'y', 3, [])
        assert self.vector1.minimum_of_elements() == 1.0

        assert self.vector2.minimum_of_elements() == 0.0

        try:
            assert self.vector3.minimum_of_elements()
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

    def test_maximum_of_elements(self):
        self.vector1 = MyVectorNP(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVectorNP(2, 'b', 2, [0, 1, 2, 3, 4.5])
        self.vector3 = MyVectorNP(3, 'y', 3, [])
        assert self.vector1.maximum_of_elements() == 3.0

        assert self.vector2.maximum_of_elements() == 4.5

        try:
            assert self.vector3.maximum_of_elements()
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

    def test_vector_np_domain(self):
        self.test_validate()
        self.test_getters()
        self.test_setters()
        self.test_add_scalar()
        self.test_add_vector()
        self.test_sub_vector()
        self.test_mul_vector()
        self.test_sum_of_elements()
        self.test_prod_of_elements()
        self.test_average_of_elements()
        self.test_minimum_of_elements()
        self.test_maximum_of_elements()


class VectorRepositoryTests(unittest.TestCase):

    # 1
    def test_add(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector4 = "Bud Spencer"
        self.vector5 = MyVector(-1, 'a', 0, ['a'])

        self.repo = VectorRepository()

        self.repo.add(self.vector1)
        assert self.repo.get_all() == [self.vector1]

        try:
            self.repo.add(self.vector4)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid type!\n"

        try:
            self.repo.add(self.vector5)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid name_id! Should be greater or equal to 0!\n" \
                                 "Invalid color! Color must be either r, b, y, g, m!\n" \
                                 "Invalid type! Should be greater or equal to 1!\n" \
                                 "Invalid values! Should be integers or floats!\n"

        try:
            self.repo.add(self.vector1)
            assert False
        except ValueError as error:
            assert str(error) == "Vector already exists!\n"

    # 2
    def test_get_all(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [3, 2, 1])
        self.vector3 = MyVector(3, 'b', 3, [1, 2, 3, 4.5])

        self.repo = VectorRepository()

        self.repo.add(self.vector1)
        assert self.repo.get_all() == [self.vector1]

        self.repo.add(self.vector2)
        assert self.repo.get_all() == [self.vector1, self.vector2]

        self.repo.add(self.vector3)
        assert self.repo.get_all() == [self.vector1, self.vector2, self.vector3]

    # 3
    def test_get_at_index(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [3, 2, 1])

        self.repo = VectorRepository()

        try:
            assert self.repo.get_at_index(1)
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        self.repo.add(self.vector1)
        self.repo.add(self.vector2)

        assert self.repo.get_at_index(0) == self.vector1
        assert self.repo.get_at_index(1) == self.vector2

        try:
            assert self.repo.get_at_index('a')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid index! Should be integer!\n"

        try:
            assert self.repo.get_at_index(2)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid index! Should be between 0 and lenght of list!\n"

        try:
            assert self.repo.get_at_index(-1)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid index! Should be between 0 and lenght of list!\n"

    # 4
    def test_update_at_index(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [3, 2, 1])
        self.vector3 = MyVector(3, 'b', 3, [1, 2, 3, 4.5])
        self.vector4 = "Bud Spencer"
        self.vector5 = MyVector(-1, 'a', 0, ['a'])

        self.repo = VectorRepository()

        try:
            self.repo.update_at_index(1, self.vector2)
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        self.repo.add(self.vector1)
        assert self.repo.get_at_index(0) == self.vector1

        self.repo.update_at_index(0, self.vector2)
        assert str(self.repo.get_at_index(0)) == str(self.vector2)

        try:
            self.repo.update_at_index('a', self.vector2)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid index! Should be integer!\n"

        try:
            self.repo.update_at_index(1, self.vector2)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid index! Should be between 0 and lenght of list!\n"

        try:
            self.repo.update_at_index(0, self.vector4)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid type!\n"

        try:
            self.repo.update_at_index(0, self.vector5)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid name_id! Should be greater or equal to 0!\n" \
                                 "Invalid color! Color must be either r, b, y, g, m!\n" \
                                 "Invalid type! Should be greater or equal to 1!\n" \
                                 "Invalid values! Should be integers or floats!\n"

        self.repo.add(self.vector3)
        try:
            self.repo.update_at_index(0, self.vector3)
            assert False
        except ValueError as error:
            assert str(error) == "Vector already exists!\n"

    # 5
    def test_update_by_name_id(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [3, 2, 1])
        self.vector3 = MyVector(3, 'b', 3, [1, 2, 3, 4.5])
        self.vector4 = "Bud Spencer"
        self.vector5 = MyVector(-1, 'a', 0, ['a'])
        self.vector6 = MyVector('a', 'r', 1, [1, 2, 3])

        self.repo = VectorRepository()

        try:
            self.repo.update_by_name_id(self.vector2)
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        self.repo.add(self.vector1)
        assert self.repo.get_at_index(0) == self.vector1

        try:
            self.repo.update_by_name_id(self.vector6)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid name_id! Should be integer!\n"

        self.vector2.set_name_id(self.vector1.get_name_id())
        self.repo.update_by_name_id(self.vector2)
        assert str(self.repo.get_at_index(0)) == str(self.vector2)

        try:
            self.repo.update_by_name_id(self.vector4)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid type!\n"

        try:
            self.repo.update_by_name_id(self.vector5)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid name_id! Should be greater or equal to 0!\n" \
                                 "Invalid color! Color must be either r, b, y, g, m!\n" \
                                 "Invalid type! Should be greater or equal to 1!\n" \
                                 "Invalid values! Should be integers or floats!\n"

        try:
            self.repo.update_by_name_id(self.vector3)
            assert False
        except ValueError as error:
            assert str(error) == "Vector doesn't exist!\n"

    # 6
    def test_delete_at_index(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])

        self.repo = VectorRepository()

        try:
            self.repo.delete_at_index(1)
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        self.repo.add(self.vector1)

        try:
            self.repo.delete_at_index('a')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid index! Should be integer!\n"

        try:
            self.repo.delete_at_index(1)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid index! Should be between 0 and lenght of list!\n"

        assert self.repo.get_all() == [self.vector1]
        self.repo.delete_at_index(0)
        assert self.repo.get_all() == []

    # 7
    def test_delete_by_name_id(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [3, 2, 1])

        self.repo = VectorRepository()

        try:
            self.repo.delete_by_name_id(1)
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        name_id1 = self.vector1.get_name_id()
        name_id2 = self.vector2.get_name_id()
        self.repo.add(self.vector1)

        try:
            self.repo.delete_by_name_id('a')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid name_id! Should be integer!\n"

        try:
            self.repo.delete_by_name_id(-1)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid name_id! Should be greater or equal to 0!\n"

        try:
            self.repo.delete_by_name_id(name_id2)
            assert False
        except ValueError as error:
            assert str(error) == "Name_id not in list!\n"

        assert self.repo.get_all() == [self.vector1]
        self.repo.delete_by_name_id(name_id1)
        assert self.repo.get_all() == []

    # 9
    def test_sum_of_all_elements(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [3, 2, 1])

        self.repo = VectorRepository()

        try:
            self.repo.sum_of_all_elements()
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        self.repo.add(self.vector1)
        assert self.repo.sum_of_all_elements() == 6
        self.repo.add(self.vector2)
        assert self.repo.sum_of_all_elements() == 12

    # 10
    def test_get_vector_sum_of_all_vectors(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [3, 2, 1])
        self.vector3 = MyVector(3, 'b', 3, [0, 0, 0])

        self.repo = VectorRepository()

        try:
            self.repo.get_vector_sum_of_all_vectors()
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        self.repo.add(self.vector1)
        assert self.repo.get_vector_sum_of_all_vectors() == self.vector1.get_values()
        self.repo.add(self.vector2)
        self.vector3.add_vector(self.vector1)
        self.vector3.add_vector(self.vector2)
        assert self.repo.get_vector_sum_of_all_vectors() == self.vector3.get_values()

    # 11
    def test_get_elements_with_given_sum(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [1, 2, 4])
        self.vector3 = MyVector(3, 'b', 3, [3, 2, 1])
        self.repo = VectorRepository()

        try:
            self.repo.get_elements_with_given_sum(6)
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        try:
            self.repo.get_elements_with_given_sum('a')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid sum! Should be integer or float!\n"

        self.repo.add(self.vector1)
        self.repo.add(self.vector2)
        assert self.repo.get_elements_with_given_sum(6) == [self.vector1]

        self.repo.add(self.vector3)
        assert self.repo.get_elements_with_given_sum(6) == [self.vector1, self.vector3]

    # 12
    def test_get_vectors_with_minimum_less_than_value(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [2, 4, 6])
        self.vector3 = MyVector(3, 'b', 3, [3, 2, 1])
        self.repo = VectorRepository()

        try:
            self.repo.get_vectors_with_minimum_less_than_value(5)
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        try:
            self.repo.get_vectors_with_minimum_less_than_value('a')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid value! Should be integer or float!\n"

        self.repo.add(self.vector1)
        assert self.repo.get_vectors_with_minimum_less_than_value(2) == [self.vector1]

        self.repo.add(self.vector2)
        assert self.repo.get_vectors_with_minimum_less_than_value(2) == [self.vector1]

        self.repo.add(self.vector3)
        assert self.repo.get_vectors_with_minimum_less_than_value(2) == [self.vector1, self.vector3]

    # 13
    def test_get_sum_of_elements_of_vectors_of_color(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [2, 4, 6])
        self.vector3 = MyVector(3, 'r', 3, [3, 2, 1])
        self.repo = VectorRepository()

        try:
            self.repo.get_sum_of_elements_of_vectors_of_color('r')
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        try:
            self.repo.get_sum_of_elements_of_vectors_of_color('a')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid color! Color must be either r, b, y, g, m!\n"

        self.repo.add(self.vector1)
        assert self.repo.get_sum_of_elements_of_vectors_of_color('r') == 6

        self.repo.add(self.vector2)
        assert self.repo.get_sum_of_elements_of_vectors_of_color('r') == 6

        self.repo.add(self.vector3)
        assert self.repo.get_sum_of_elements_of_vectors_of_color('r') == 12

    # 14
    def test_get_max_of_vectors_with_sum_greater_than_value(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [0, 1, 2, 3])
        self.repo = VectorRepository()

        try:
            self.repo.get_max_of_vectors_with_sum_greater_than_value(5)
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        try:
            self.repo.get_max_of_vectors_with_sum_greater_than_value('a')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid value! Should be integer or float!\n"

        self.repo.add(self.vector1)
        assert self.repo.get_max_of_vectors_with_sum_greater_than_value(5) == self.vector1.get_values()

        self.repo.add(self.vector2)
        assert self.repo.get_max_of_vectors_with_sum_greater_than_value(5) == self.vector1.get_values()

    # 15
    def test_get_min_of_all_vectors(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [0, 1, 2, 3])
        self.repo = VectorRepository()

        try:
            self.repo.get_min_of_all_vectors()
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        self.repo.add(self.vector1)
        assert self.repo.get_min_of_all_vectors() == self.vector1.get_values()

        self.repo.add(self.vector2)
        assert self.repo.get_min_of_all_vectors() == self.vector2.get_values()

    # 16
    def test_get_list_of_values_multiplication_of_consecutive_vectors(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [2, 4, 6])
        self.vector3 = MyVector(3, 'r', 3, [3, 2, 1])
        self.repo = VectorRepository()

        try:
            self.repo.get_list_of_values_multiplication_of_consecutive_vectors()
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        self.repo.add(self.vector1)
        self.repo.add(self.vector2)
        self.repo.add(self.vector3)
        assert self.repo.get_list_of_values_multiplication_of_consecutive_vectors() == [28, 20]

    # 17
    def test_delete_all(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])

        self.repo = VectorRepository()

        self.repo.add(self.vector1)
        assert self.repo.get_all() == [self.vector1]
        self.repo.delete_all()
        assert self.repo.get_all() == []

    # 18
    def test_delete_vectors_of_color_or_with_product_of_elements_greater_than_value(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [2, 4, 6])
        self.vector3 = MyVector(3, 'r', 3, [3, 2, 1])
        self.repo = VectorRepository()

        try:
            self.repo.delete_vectors_of_color('r')
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        self.repo.add(self.vector1)
        self.repo.add(self.vector2)
        self.repo.add(self.vector3)
        self.repo.delete_vectors_of_color('r')
        assert self.repo.get_all() == [self.vector2]
        self.repo.delete_vectors_of_color('g')
        assert self.repo.get_all() == []

        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [2, 4, 6])
        self.vector3 = MyVector(3, 'r', 3, [3, 2, 1])

        try:
            self.repo.delete_vectors_with_product_of_elements_greater_than_value(5)
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        self.repo.add(self.vector1)
        self.repo.add(self.vector2)
        self.repo.add(self.vector3)
        self.repo.delete_vectors_with_product_of_elements_greater_than_value(6)
        assert self.repo.get_all() == [self.vector1, self.vector3]
        self.repo.delete_vectors_with_product_of_elements_greater_than_value(5)
        assert self.repo.get_all() == []

    # 19
    def test_delete_vectors_between_two_indexes(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [2, 4, 6])
        self.vector3 = MyVector(3, 'r', 3, [3, 2, 1])
        self.repo = VectorRepository()

        try:
            self.repo.delete_vectors_between_two_indexes(0, 1)
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        try:
            self.repo.delete_vectors_between_two_indexes('a', 1)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid index1! Should be integer!\n"

        self.repo.add(self.vector1)
        self.repo.add(self.vector2)
        self.repo.add(self.vector3)

        try:
            self.repo.delete_vectors_between_two_indexes(0, 3)
            assert False
        except ValueError as error:
            assert str(error) == "Invalid index2! Should be between 0 and lenght of list-1!\n"

        self.repo.delete_vectors_between_two_indexes(0, 1)
        assert self.repo.get_all() == [self.vector3]

    # 20
    def test_delete_vectors_with_maximum_equal_to_value(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'g', 2, [2, 4, 6])
        self.vector3 = MyVector(3, 'r', 3, [3, 2, 1])
        self.repo = VectorRepository()

        try:
            self.repo.delete_vectors_with_maximum_equal_to_value(5)
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        try:
            self.repo.delete_vectors_with_maximum_equal_to_value('a')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid value! Should be integer or float!\n"

        self.repo.add(self.vector1)
        self.repo.add(self.vector2)
        self.repo.add(self.vector3)
        self.repo.delete_vectors_with_maximum_equal_to_value(3)
        assert self.repo.get_all() == [self.vector2]
        self.repo.delete_vectors_with_maximum_equal_to_value(6)
        assert self.repo.get_all() == []

    # 21
    def test_add_scalar_to_all(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.repo = VectorRepository()

        try:
            self.repo.add_scalar_to_all(2)
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        try:
            self.repo.add_scalar_to_all('a')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid scalar! Should be integer or float!\n"

        self.repo.add(self.vector1)
        self.repo.add_scalar_to_all(2)
        assert self.repo.get_all()[0].get_values() == [3.0, 4.0, 5.0]

    # 22
    def test_update_color_of_vectors_with_name_id(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.repo = VectorRepository()

        try:
            self.repo.update_color_of_vectors_with_name_id(1, 'g')
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        try:
            self.repo.update_color_of_vectors_with_name_id(1, 'a')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid color! Color must be either r, b, y, g, m!\n"

        self.repo.add(self.vector1)
        self.repo.update_color_of_vectors_with_name_id(1, 'g')
        assert self.repo.get_all()[0].get_color() == 'g'

    # 23
    def test_update_vectors_of_type_by_setting_color(self):
        self.vector1 = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector2 = MyVector(2, 'r', 2, [2, 4, 6])
        self.repo = VectorRepository()

        try:
            self.repo.update_vectors_of_type_by_setting_color(1, 'g')
            assert False
        except ValueError as error:
            assert str(error) == "The list is empty!\n"

        try:
            self.repo.update_vectors_of_type_by_setting_color('a', 'g')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid type! Should be integer!\n"

        try:
            self.repo.update_vectors_of_type_by_setting_color(1, 'a')
            assert False
        except ValueError as error:
            assert str(error) == "Invalid color! Color must be either r, g, b, y, m!\n"

        self.repo.add(self.vector1)
        self.repo.add(self.vector2)
        self.repo.update_vectors_of_type_by_setting_color(1, 'g')
        assert self.repo.get_all()[0].get_color() == 'g'
        assert self.repo.get_all()[1].get_color() == 'r'

    def test_vector_repository(self):
        self.test_add()
        self.test_get_all()
        self.test_get_at_index()
        self.test_update_at_index()
        self.test_update_by_name_id()
        self.test_delete_at_index()
        self.test_delete_by_name_id()
        self.test_sum_of_all_elements()
        self.test_get_vector_sum_of_all_vectors()
        self.test_get_elements_with_given_sum()
        self.test_get_vectors_with_minimum_less_than_value()
        self.test_get_sum_of_elements_of_vectors_of_color()
        self.test_get_max_of_vectors_with_sum_greater_than_value()
        self.test_get_min_of_all_vectors()
        self.test_get_list_of_values_multiplication_of_consecutive_vectors()
        self.test_delete_all()
        self.test_delete_vectors_of_color_or_with_product_of_elements_greater_than_value()
        self.test_delete_vectors_between_two_indexes()
        self.test_delete_vectors_with_maximum_equal_to_value()
        self.test_add_scalar_to_all()
        self.test_update_color_of_vectors_with_name_id()
        self.test_update_vectors_of_type_by_setting_color()


def run_tests():
    VectorTests().test_vector_domain()
    VectorNPTests().test_vector_np_domain()
    VectorRepositoryTests().test_vector_repository()
