from domain.passenger import Passenger
from domain.plane import Plane
# from repository.passengers_repository import PassengersRepository
# from repository.planes_repository import PlanesRepository


class Service:
    def __init__(self, passenger_repository, plane_repository):
        self.passenger_repository = passenger_repository
        self.plane_repository = plane_repository

    "passenger service"

    @staticmethod
    def create_passenger(first_name, last_name, passport_number):
        return Passenger(first_name, last_name, passport_number)

    def add_passenger(self, first_name, last_name, passport_number):
        passenger = self.create_passenger(first_name, last_name, passport_number)
        try:
            passenger.validate()
            self.passenger_repository.add_passenger(passenger)
        except ValueError as ve:
            raise ValueError(str(ve))

    def get_all_passengers(self):
        try:
            return self.passenger_repository.get_all()
        except ValueError as ve:
            raise ValueError(str(ve))

    def get_passenger_by_name(self, name):
        try:
            return self.passenger_repository.get_passenger_by_name(name)
        except ValueError as ve:
            raise ValueError(str(ve))

    def get_passenger_by_passport_number(self, passport_number):
        try:
            return self.passenger_repository.get_passenger_by_passport_number(passport_number)
        except ValueError as ve:
            raise ValueError(str(ve))

    def update_passenger(self, passenger, first_name, last_name, passport_number):
        up_passenger = self.create_passenger(first_name, last_name, passport_number)
        try:
            up_passenger.validate()
            return self.passenger_repository.update_passenger(passenger, up_passenger)
        except ValueError as ve:
            raise ValueError(str(ve))

    def remove_passenger_by_passport_number(self, passport_number):
        try:
            return self.passenger_repository.remove_passenger_by_passport_number(passport_number)
        except ValueError as ve:
            raise ValueError(str(ve))

    "plane service"

    @staticmethod
    def create_plane(name, airline_company, number_of_seats, destination, passengers):
        return Plane(name, airline_company, number_of_seats, destination, passengers)

    def add_plane(self, name, airline_company, number_of_seats, destination, passengers):
        plane = self.create_plane(name, airline_company, number_of_seats, destination, passengers)
        try:
            plane.validate()
            self.plane_repository.add_plane(plane)
        except ValueError as ve:
            raise ValueError(str(ve))

    def get_all_planes(self):
        try:
            return self.plane_repository.get_all()
        except ValueError as ve:
            raise ValueError(str(ve))

    def get_plane_by_name(self, name):
        try:
            return self.plane_repository.get_plane_by_name(name)
        except ValueError as ve:
            raise ValueError(str(ve))

    def get_planes_by_destination(self, destination):
        try:
            return self.plane_repository.get_planes_by_destination(destination)
        except ValueError as ve:
            raise ValueError(str(ve))

    def get_planes_by_number_of_seats(self, number_of_seats):
        try:
            return self.plane_repository.get_planes_by_number_of_seats(number_of_seats)
        except ValueError as ve:
            raise ValueError(str(ve))

    def update_plane(self, plane, name, airline_company, number_of_seats, destination, passengers):
        up_plane = self.create_plane(name, airline_company, number_of_seats, destination, passengers)
        try:
            up_plane.validate()
            return self.plane_repository.update_plane(plane, up_plane)
        except ValueError as ve:
            raise ValueError(str(ve))

    def remove_plane_by_name(self, name):
        try:
            return self.plane_repository.remove_plane_by_name(name)
        except ValueError as ve:
            raise ValueError(str(ve))

    "sort and filter"

    # 3
    def sort_passengers_by_last_name(self, plane_name):
        """
        Sorts the passengers of a plane by last name
        In: plane_name - string
        Out: list of strings
        Errors: ValueError - if the plane does not exist
        """
        try:
            plane = self.get_plane_by_name(plane_name)
            names = []
            s = sorted(plane.get_passengers(), key=lambda x: x.get_last_name())
            for i in s:
                names.append(i.get_first_name() + ' ' + i.get_last_name())
            return names
        except ValueError as ve:
            raise ValueError(str(ve))

    # 4
    def sort_planes_by_number_of_seats(self):
        """
        Sorts the planes by number of seats
        In: -
        Out: list of strings
        Errors: ValueError - if there are no planes
        """
        if len(self.get_all_planes()) == 0:
            raise ValueError("There are no planes!")
        s = sorted(self.get_all_planes(), key=lambda x: x.get_number_of_seats())
        names = []
        for i in s:
            names.append(i.get_name())
        return names

    # 5
    def sort_planes_by_number_of_passengers_with_given_prefix_for_first_name(self, prefix):
        """
        Sorts the planes by number of passengers with given prefix for first name
        In: prefix - string
        Out: list of strings
        Errors: ValueError - if there are no planes
        """
        try:
            s = sorted(self.get_all_planes(), key=lambda x: len(list(filter(lambda y: y.get_first_name().startswith(prefix), x.get_passengers()))))
            names = []
            for i in s:
                names.append(i.get_name())
            return names
        except ValueError as ve:
            raise ValueError(str(ve))

    # 6
    def sort_planes_by_concatenation_of_number_of_passengers_and_destination(self):
        """
        Sorts the planes by concatenation of number of passengers and destination
        In: -
        Out: list of strings
        Errors: ValueError - if there are no planes
        """
        try:
            s = sorted(self.get_all_planes(), key=lambda x: str(len(x.get_passengers())) + x.get_destination())
            names = []
            for i in s:
                names.append(i.get_name())
            return names
        except ValueError as ve:
            raise ValueError(str(ve))

    # 7
    def filter_planes_with_passengers_with_passport_number_with_same_3_letters(self):
        """
        Filters the planes with passengers with passport number with same 3 letters
        In: -
        Out: list of strings
        Errors: ValueError - if there are no planes
        """
        try:
            s = list(filter(lambda x: any(y.get_passport_number()[0:3] == z.get_passport_number()[0:3] for y in x.get_passengers() for z in x.get_passengers() if y != z), self.get_all_planes()))
            names = []
            for i in s:
                names.append(i.get_name())
            return names
        except ValueError as ve:
            raise ValueError(str(ve))

    # 8
    def filter_passengers_with_string_in_name(self, plane_name, string):
        """
        Filters the passengers with string in name
        In: plane_name - string, string - string
        Out: list of strings
        Errors: ValueError - if the plane does not exist
        """
        try:
            plane = self.get_plane_by_name(plane_name)
            s = list(filter(lambda x: string in x.get_first_name() or string in x.get_last_name() or string[0].upper() + string[1:] in x.get_first_name() or string[0].upper() + string[1:] in x.get_last_name(), plane.get_passengers()))
            names = []
            for i in s:
                names.append(i.get_first_name() + ' ' + i.get_last_name())
            return names
        except ValueError as ve:
            raise ValueError(str(ve))

    # 9
    def filter_planes_with_given_passenger_name(self, passenger_name):
        """
        Filters the planes with given passenger name
        In: passenger_name - string
        Out: list of strings
        Errors: ValueError - if there are no planes
        """
        try:
            first_name, last_name = passenger_name.split()
            s = list(filter(lambda x: any(y.get_first_name() == first_name and y.get_last_name() == last_name for y in x.get_passengers()), self.get_all_planes()))
            names = []
            for i in s:
                names.append(i.get_name())
            return names
        except ValueError as ve:
            raise ValueError(str(ve))

    # 10
    def backtrack1(self, current_group, remaining_passengers, groups, k):
        """
        Backtracking for groups of k passengers with different last names
        In: current_group - list of passengers
            remaining_passengers - list of passengers
            groups - list of lists of passengers
            k - integer
        Out: -
        Errors: -
        """
        if len(current_group) == k:
            groups.append(current_group[:])
            return
        for i in range(len(remaining_passengers)):
            passenger = remaining_passengers[i]
            if any(p.get_last_name() == passenger.get_last_name() for p in current_group):
                continue
            current_group.append(passenger)
            self.backtrack1(current_group, remaining_passengers[i + 1:], groups, k)
            current_group.pop()

    def groups_of_k_passengers_with_different_last_names(self, plane_name, k):
        """
        Groups of k passengers with different last names
        In: plane_name - string
            k - integer
        Out: list of lists of strings
        Errors: ValueError - if the plane does not exist
        """
        plane = self.get_plane_by_name(plane_name)
        passengers = plane.get_passengers()
        groups = []
        self.backtrack1([], passengers, groups, k)
        for group in groups:
            for i in range(len(group)):
                group[i] = group[i].get_first_name() + ' ' + group[i].get_last_name()
        return groups

    # 11
    def backtrack2(self, current_group, remaining_planes, groups, k):
        """
        Backtracking for groups of k planes with the same destination but belonging to different airline companies
        In: current_group - list of planes
            remaining_planes - list of planes
            groups - list of lists of planes
            k - integer
        Out: -
        Errors: -
        """
        if len(current_group) == k:
            groups.append(current_group[:])
            return
        for i in range(len(remaining_planes)):
            plane = remaining_planes[i]
            if any(p.get_destination() != plane.get_destination() for p in current_group):
                continue
            if any(p.get_airline_company() == plane.get_airline_company() for p in current_group):
                continue
            current_group.append(plane)
            self.backtrack2(current_group, remaining_planes[i + 1:], groups, k)
            current_group.pop()

    def groups_of_k_planes_with_the_same_destination_but_belonging_to_different_airline_companies(self, k):
        """
        Groups of k planes with the same destination but belonging to different airline companies
        In: k - integer
        Out: list of lists of strings
        Errors: ValueError - if there are no planes
        """
        planes = self.get_all_planes()
        groups = []
        self.backtrack2([], planes, groups, k)
        for group in groups:
            for i in range(len(group)):
                group[i] = group[i].get_name()
        return groups

# passengers1 = [Passenger("John", "Zyx", "123456789"),
#                Passenger("Jane", "Abc", "987654321"),
#                Passenger("Anne", "Lmn", "135792468")]
#
# plane1 = Plane("Plane1", "Airline1", 100, "Destination1", passengers1)
# plane2 = Plane("Plane2", "Airline2", 90, "Destination2", [])
#
# planes = [plane1, plane2]
# service = Service(PassengersRepository(), PlanesRepository(planes))
#
# s1 = service.sort_passengers_by_last_name("Plane1")
# for p in s1:
#     print(p)
# print('\n')
#
# s2 = service.sort_planes_by_number_of_seats()
# for p in s2:
#     print(p.get_name(), ':', p.get_number_of_seats())
# print('\n')
#
# f1 = service.filter_passangers_with_string_in_name("Plane1", "a")
# for p in f1:
#     print(p)
# print('\n')
#
#
# def test_sort_passengers_by_last_name():
#     sort1 = service.sort_passengers_by_last_name("Plane1")
#     assert sort1 == [Passenger("Jane", "Abc", "987654321"), Passenger("Anne", "Lmn", "135792468"), Passenger("John", "Zyx", "123456789")]
#
#
# def test_sort_planes_by_number_of_seats():
#     sort2 = service.sort_planes_by_number_of_seats()
#     assert sort2 == [plane2, plane1]
#
#
# def test_filter_passangers_with_string_in_name():
#     filter1 = service.filter_passangers_with_string_in_name("Plane1", "a")
#     assert filter1 == [Passenger("Jane", "Abc", "987654321"), Passenger("Anne", "Lmn", "135792468")]
#
#
# test_sort_passengers_by_last_name()
# test_sort_planes_by_number_of_seats()
# test_filter_passangers_with_string_in_name()


# def planes_sorted_by_number_of_seats_when_all_planes_have_different_number_of_seats():
#     # Arrange
#     plane1 = Plane("Plane1", "Airline1", 100, "Destination1", [])
#     plane2 = Plane("Plane2", "Airline2", 90, "Destination2", [])
#     plane3 = Plane("Plane3", "Airline3", 110, "Destination3", [])
#     planes = [plane1, plane2, plane3]
#     service = Service(PassengersRepository(), PlanesRepository(planes))
#
#     # Act
#     sorted_planes = service.sort_planes_by_number_of_seats()
#
#     # Assert
#     assert sorted_planes == [plane2, plane1, plane3]
#
#
# def planes_sorted_by_number_of_seats_when_some_planes_have_same_number_of_seats():
#     # Arrange
#     plane1 = Plane("Plane1", "Airline1", 100, "Destination1", [])
#     plane2 = Plane("Plane2", "Airline2", 100, "Destination2", [])
#     plane3 = Plane("Plane3", "Airline3", 110, "Destination3", [])
#     planes = [plane1, plane2, plane3]
#     service = Service(PassengersRepository(), PlanesRepository(planes))
#
#     # Act
#     sorted_planes = service.sort_planes_by_number_of_seats()
#
#     # Assert
#     assert sorted_planes == [plane1, plane2, plane3]
#
#
# def planes_sorted_by_number_of_seats_when_no_planes_exist():
#     # Arrange
#     service = Service(PassengersRepository(), PlanesRepository([]))
#
#     # Act
#     sorted_planes = service.sort_planes_by_number_of_seats()
#
#     # Assert
#     assert sorted_planes == []

# passengers = [Passenger("John", "Zyx", "123456789"),
#                            Passenger("Jane", "Abc", "987654321"),
#                            Passenger("Anne", "Lmn", "135792468")]
#
# plane1 = Plane("Plane1", "Airline1", 100, "Destination1", passengers)
# plane2 = Plane("Plane2", "Airline2", 90, "Destination2", [])
# planes = [plane1, plane2]
# service = Service(PassengersRepository(), PlanesRepository(planes))
#
# filtered_planes = service.filter_planes_with_given_passenger_name("John Zyx")
# print(filtered_planes)
