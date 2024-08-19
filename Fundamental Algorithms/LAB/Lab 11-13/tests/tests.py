from domain.passenger import Passenger
from repository.passengers_repository import PassengersRepository
from domain.plane import Plane
from repository.planes_repository import PlanesRepository
from service.all_service import Service
import unittest


class PassengerTests(unittest.TestCase):
    def test_getters(self):
        passenger = Passenger("John", "Doe", "123456789")
        self.assertEqual(passenger.get_first_name(), "John")
        self.assertEqual(passenger.get_last_name(), "Doe")
        self.assertEqual(passenger.get_passport_number(), "123456789")

    def test_setters(self):
        passenger = Passenger("John", "Doe", "123456789")
        passenger.set_first_name("Jane")
        passenger.set_last_name("Dye")
        passenger.set_passport_number("987654321")
        self.assertEqual(passenger.get_first_name(), "Jane")
        self.assertEqual(passenger.get_last_name(), "Dye")
        self.assertEqual(passenger.get_passport_number(), "987654321")

    def test_str(self):
        passenger = Passenger("John", "Doe", "123456789")
        self.assertEqual(str(passenger), "Name: John Doe ; 123456789\n")

    def test_eq(self):
        passenger1 = Passenger("John", "Doe", "123456789")
        passenger2 = Passenger("John", "Doe", "123456789")
        self.assertTrue(passenger1 == passenger2)

    def test_validate(self):
        passenger = Passenger("John", "Doe", "123456789")
        self.assertTrue(passenger.validate())
        try:
            Passenger("", "", "").validate()
            assert False
        except ValueError as ve:
            assert str(ve) == "First name cannot be empty!\nLast name cannot be empty!\nPassport number cannot be empty!\n"
        try:
            Passenger("John1", "Doe1", "1A").validate()
            assert False
        except ValueError as ve:
            assert str(ve) == "First name must contain only letters!\nLast name must contain only letters!\nPassport number must be a number!\n"

    def test_passenger(self):
        self.test_getters()
        self.test_setters()
        self.test_str()
        self.test_eq()
        self.test_validate()
        print("Passenger tests passed!")


class PlaneTests(unittest.TestCase):
    def test_getters(self):
        plane = Plane("Boeing 737", "Ryanair", 150, "London", [])
        self.assertEqual(plane.get_name(), "Boeing 737")
        self.assertEqual(plane.get_airline_company(), "Ryanair")
        self.assertEqual(plane.get_number_of_seats(), 150)
        self.assertEqual(plane.get_destination(), "London")
        self.assertEqual(plane.get_passengers(), [])

    def test_setters(self):
        plane = Plane("Boeing 737", "Ryanair", 150, "London", [])
        plane.set_name("Boeing 747")
        plane.set_airline_company("Wizz Air")
        plane.set_number_of_seats(200)
        plane.set_destination("Paris")
        plane.set_passengers([])
        self.assertEqual(plane.get_name(), "Boeing 747")
        self.assertEqual(plane.get_airline_company(), "Wizz Air")
        self.assertEqual(plane.get_number_of_seats(), 200)
        self.assertEqual(plane.get_destination(), "Paris")
        self.assertEqual(plane.get_passengers(), [])

    def test_str(self):
        plane = Plane("Boeing 737", "Ryanair", 150, "London", [])
        self.assertEqual(str(plane), "Name: Boeing 737 ; Airline company: Ryanair ; Number of seats: 150 ; Destination: London\n")

    def test_plane(self):
        self.test_getters()
        self.test_setters()
        self.test_str()
        print("Plane tests passed!")


class PassengersRepositoryTests(unittest.TestCase):
    pass


class PlanesRepositoryTests(unittest.TestCase):
    pass


class ServiceTests(unittest.TestCase):
    def test_sort_passengers_by_last_name(self):
        self.passengers = [Passenger("John", "Zyx", "123456789"),
                           Passenger("Jane", "Abc", "987654321"),
                           Passenger("Anne", "Lmn", "135792468")]

        self.plane1 = Plane("Plane1", "Airline1", 100, "Destination1", self.passengers)
        self.plane2 = Plane("Plane2", "Airline2", 90, "Destination2", [])
        self.planes = [self.plane1, self.plane2]
        self.service = Service(PassengersRepository(), PlanesRepository(self.planes))
        sorted_passengers = self.service.sort_passengers_by_last_name("Plane1")
        self.assertEqual(sorted_passengers, ["Jane Abc", "Anne Lmn", "John Zyx"])

    def test_sort_planes_by_number_of_seats(self):
        self.plane1 = Plane("Plane1", "Airline1", 100, "Destination1", [])
        self.plane2 = Plane("Plane2", "Airline2", 90, "Destination2", [])
        self.planes = [self.plane1, self.plane2]
        self.service = Service(PassengersRepository(), PlanesRepository(self.planes))
        sorted_planes = self.service.sort_planes_by_number_of_seats()
        self.assertEqual(sorted_planes, [self.plane2.get_name(), self.plane1.get_name()])

    def test_sort_planes_by_number_of_passengers_with_given_prefix_for_first_name(self):
        self.passengers = [Passenger("John", "Zyx", "123456789"),
                           Passenger("Jane", "Abc", "987654321"),
                           Passenger("Anne", "Lmn", "135792468")]

        self.plane1 = Plane("Plane1", "Airline1", 100, "Destination1", self.passengers)
        self.plane2 = Plane("Plane2", "Airline2", 90, "Destination2", [])
        self.planes = [self.plane1, self.plane2]
        self.service = Service(PassengersRepository(), PlanesRepository(self.planes))
        sorted_planes = self.service.sort_planes_by_number_of_passengers_with_given_prefix_for_first_name("J")
        self.assertEqual(sorted_planes, [self.plane2.get_name(), self.plane1.get_name()])

    def test_sort_planes_by_concatenation_of_number_of_passengers_and_destination(self):
        self.passengers = [Passenger("John", "Zyx", "123456789"),
                           Passenger("Jane", "Abc", "987654321"),
                           Passenger("Anne", "Lmn", "135792468")]

        self.plane1 = Plane("Plane1", "Airline1", 100, "Destination1", self.passengers)
        self.plane2 = Plane("Plane2", "Airline2", 90, "Destination2", [])
        self.planes = [self.plane1, self.plane2]
        self.service = Service(PassengersRepository(), PlanesRepository(self.planes))
        sorted_planes = self.service.sort_planes_by_concatenation_of_number_of_passengers_and_destination()
        self.assertEqual(sorted_planes, [self.plane2.get_name(), self.plane1.get_name()])

    def test_filter_planes_with_passengers_with_passport_number_with_same_3_letters(self):
        self.passengers = [Passenger("John", "Zyx", "123456789"),
                           Passenger("Jane", "Abc", "987654321"),
                           Passenger("Anne", "Lmn", "135792468")]

        self.plane1 = Plane("Plane1", "Airline1", 100, "Destination1", self.passengers)
        self.plane2 = Plane("Plane2", "Airline2", 90, "Destination2", [])
        self.planes = [self.plane1, self.plane2]
        self.service = Service(PassengersRepository(), PlanesRepository(self.planes))
        filtered_planes = self.service.filter_planes_with_passengers_with_passport_number_with_same_3_letters()
        self.assertEqual(filtered_planes, [])

    def test_filter_passengers_with_string_in_name(self):
        self.passengers = [Passenger("John", "Zyx", "123456789"),
                           Passenger("Jane", "Abc", "987654321"),
                           Passenger("Anne", "Lmn", "135792468")]

        self.plane1 = Plane("Plane1", "Airline1", 100, "Destination1", self.passengers)
        self.planes = [self.plane1]
        self.service = Service(PassengersRepository(), PlanesRepository(self.planes))
        filtered_passengers = self.service.filter_passengers_with_string_in_name("Plane1", "a")
        self.assertEqual(filtered_passengers, ["Jane Abc", "Anne Lmn"])

    def test_filter_planes_with_given_passenger_name(self):
        self.passengers = [Passenger("John", "Zyx", "123456789"),
                           Passenger("Jane", "Abc", "987654321"),
                           Passenger("Anne", "Lmn", "135792468")]

        self.plane1 = Plane("Plane1", "Airline1", 100, "Destination1", self.passengers)
        self.plane2 = Plane("Plane2", "Airline2", 90, "Destination2", [])
        self.planes = [self.plane1, self.plane2]
        self.service = Service(PassengersRepository(), PlanesRepository(self.planes))
        filtered_planes = self.service.filter_planes_with_given_passenger_name("John Zyx")
        self.assertEqual(filtered_planes, [self.plane1.get_name()])

    def test_groups_of_k_passengers_with_different_last_names(self):
        self.passengers = [Passenger("John", "Zyx", "123456789"),
                           Passenger("Jane", "Abc", "987654321"),
                           Passenger("Anne", "Lmn", "135792468")]

        self.plane1 = Plane("Plane1", "Airline1", 100, "Destination1", self.passengers)
        self.planes = [self.plane1]
        self.service = Service(PassengersRepository(), PlanesRepository(self.planes))
        groups = self.service.groups_of_k_passengers_with_different_last_names("Plane1", 2)
        self.assertEqual(groups, [["John Zyx", "Jane Abc"], ["John Zyx", "Anne Lmn"], ["Jane Abc", "Anne Lmn"]])

    def test_groups_of_k_planes_with_the_same_destination_but_belonging_to_different_airline_companies(self):
        self.plane1 = Plane("Plane1", "Airline1", 100, "Destination1", [])
        self.plane2 = Plane("Plane2", "Airline2", 90, "Destination1", [])
        self.plane3 = Plane("Plane3", "Airline3", 80, "Destination1", [])
        self.plane4 = Plane("Plane4", "Airline2", 70, "Destination1", [])
        self.planes = [self.plane1, self.plane2, self.plane3, self.plane4]
        self.service = Service(PassengersRepository(), PlanesRepository(self.planes))
        groups = self.service.groups_of_k_planes_with_the_same_destination_but_belonging_to_different_airline_companies(3)
        self.assertEqual(groups, [["Plane1", "Plane2", "Plane3"], ["Plane1", "Plane3", "Plane4"]])

    def test_service(self):
        self.test_sort_passengers_by_last_name()
        self.test_sort_planes_by_number_of_seats()
        self.test_sort_planes_by_number_of_passengers_with_given_prefix_for_first_name()
        self.test_sort_planes_by_concatenation_of_number_of_passengers_and_destination()
        self.test_filter_planes_with_passengers_with_passport_number_with_same_3_letters()
        self.test_filter_passengers_with_string_in_name()
        self.test_filter_planes_with_given_passenger_name()
        self.test_groups_of_k_passengers_with_different_last_names()
        self.test_groups_of_k_planes_with_the_same_destination_but_belonging_to_different_airline_companies()
        print("Service tests passed!")


def run_tests():
    PassengerTests().test_passenger()
    PlaneTests().test_plane()
    ServiceTests().test_service()
