from domain.passenger import Passenger


class PassengersRepository:
    def __init__(self, initial_values=None):
        if initial_values is None:
            initial_values = []
        self.__passengers = []
        if initial_values is not None:
            for value in initial_values:
                if isinstance(value, Passenger):
                    self.__passengers.append(value)

    def check_if_passenger_exists(self, passenger):
        for p in self.__passengers:
            if p.get_passport_number() == passenger.get_passport_number():
                return True
        return False

    def add_passenger(self, passenger):
        if not isinstance(passenger, Passenger):
            raise ValueError("The object is not a passenger!\n")
        if self.check_if_passenger_exists(passenger):
            raise ValueError("Passenger already in repository!\n")
        self.__passengers.append(passenger)

    def get_all(self):
        if len(self.__passengers) == 0:
            raise ValueError("Empty repository!\n")
        return self.__passengers

    def get_passenger_by_name(self, name):
        for passenger in self.__passengers:
            if passenger.get_first_name() + ' ' + passenger.get_last_name() == name:
                return passenger
            raise ValueError("There is no passenger with this name!\n")

    def get_passenger_by_passport_number(self, passport_number):
        for passenger in self.__passengers:
            if passenger.get_passport_number() == passport_number:
                return passenger
            raise ValueError("There is no passenger with this passport number!\n")

    def update_passenger(self, passenger, up_passenger):
        if not isinstance(passenger, Passenger):
            raise ValueError("Object to be updated is not a passenger!\n")
        if not isinstance(up_passenger, Passenger):
            raise ValueError("Object is not a passenger!\n")
        if self.check_if_passenger_exists(passenger):
            raise ValueError("Passenger to be updated not in repository!\n")
        if self.check_if_passenger_exists(up_passenger):
            raise ValueError("Updated passenger already in repository!\n")
        passenger.set_first_name(up_passenger.get_first_name())
        passenger.set_last_name(up_passenger.get_last_name())
        passenger.set_passport_number(up_passenger.get_passport_number())

    def remove_passenger_by_passport_number(self, passport_number):
        for passenger in self.__passengers:
            if passenger.get_passport_number() == passport_number:
                self.__passengers.remove(passenger)
                print("Passenger removed successfully!\n")
                return
        raise ValueError("Passenger not in repository!\n")

    def __len__(self):
        return len(self.__passengers)

    def __str__(self):
        repo_str = ""
        all_passengers = self.get_all()
        for passenger in all_passengers:
            repo_str += str(passenger) + "\n"
        if repo_str == "":
            raise ValueError("Empty repository!\n")
        return repo_str
