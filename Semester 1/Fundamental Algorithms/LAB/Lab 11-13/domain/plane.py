class Plane:
    def __init__(self, name, airline_company, number_of_seats, destination, passengers):
        self.name = name
        self.airline_company = airline_company
        self.number_of_seats = number_of_seats
        self.destination = destination
        self.passengers = passengers

    def validate(self):
        er = ""
        if self.name == "":
            er += "Name cannot be empty!\n"
        if self.airline_company == "":
            er += "Airline_company cannot be empty!\n"
        if self.number_of_seats < 0:
            er += "Number of seats should be positive!\n"
        if self.destination == "":
            er += "Destination cannot be empty!\n"
        if er != "":
            raise ValueError(er)
        return 1

    def get_name(self):
        return self.name

    def get_airline_company(self):
        return self.airline_company

    def get_number_of_seats(self):
        return self.number_of_seats

    def get_destination(self):
        return self.destination

    def get_passengers(self):
        return self.passengers

    def set_name(self, name):
        if name == "":
            raise ValueError('Name cannot be empty!')
        self.name = name

    def set_airline_company(self, airline_company):
        if airline_company == "":
            raise ValueError('Airline_company cannot be empty!')
        self.airline_company = airline_company

    def set_number_of_seats(self, number_of_seats):
        if not isinstance(number_of_seats, int):
            raise ValueError('Number of seats must be an integer!')
        if number_of_seats < 0:
            raise ValueError('Number of seats must be positive!')
        self.number_of_seats = number_of_seats

    def set_destination(self, destination):
        if destination == "":
            raise ValueError('Destination cannot be empty!')
        self.destination = destination

    def set_passengers(self, passengers):
        if not isinstance(passengers, list):
            raise ValueError('Passengers must be a list!')
        self.passengers = passengers

    def __str__(self):
        return 'Name: ' + self.name + ' ; Airline company: ' + self.airline_company + ' ; Number of seats: ' + str(self.number_of_seats) + ' ; Destination: ' + self.destination + '\n'


# airplane_names = ["Airbus A380", "Boeing 747", "Airbus A320", "Boeing 777", "Boeing 737", "Airbus A330", "Boeing 767", "Airbus A350", "Boeing 757", "Airbus A340"]
# p1 = Plane("Boeing 777-1", "American Airlines", 10, "Bucharest", [])
# print(p1)
