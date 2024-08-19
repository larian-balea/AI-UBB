from domain.passenger import Passenger
from domain.plane import Plane
from ui.console import Console
from repository.passengers_repository import PassengersRepository
from repository.planes_repository import PlanesRepository
from service.all_service import Service
from tests.tests import run_tests


def main():
    # 3 - p1: Jane Abc, Anne Lmn, John Zyx
    # 4     : p2, p1, p3
    # 5 - Lm: p1, p3, p2
    # 6     : p2, p1, p3
    # 7     : p3
    # 8 - p3: Jo - John Zyx, Jane Jo
    # 9 - "John Zyx" : p1, p3
    # 10
    # 11
    passengers1 = [Passenger("John", "Zyx", "123456789"),
                   Passenger("Jane", "Abc", "987654321"),
                   Passenger("Anne", "Lmn", "135792468")]

    passengers2 = [Passenger("Mary", "Xyz", "000456789"),
                   Passenger("Lmarty", "Abc", "987654321")]

    passengers3 = [Passenger("John", "Zyx", "123456789"),
                   Passenger("Jane", "Jo", "987654321"),
                   Passenger("Anne", "Zyx", "135792468"),
                   Passenger("Mary", "Lmn", "123456789"),
                   Passenger("Marty", "Lmo", "987654321")]

    passengers4 = [Passenger("Scooby", "Doo", "101"),
                   Passenger("Shaggy", "Rogers", "102"),
                   Passenger("Fred", "Jones", "103"),
                   Passenger("Daphne", "Blake", "104"),
                   Passenger("Velma", "Dinkley", "105"),
                   Passenger("Scrappy", "Doo", "106")]

    passengers5 = [Passenger("Anthony", "Soprano", "201"),
                   Passenger("Carmela", "Soprano", "202"),
                   Passenger("Meadow", "Soprano", "203"),
                   Passenger("AJ", "Soprano", "204"),
                   Passenger("Jennifer", "Melfi", "205"),
                   Passenger("Christopher", "Moltisanti", "206"),
                   Passenger("Paulie", "Gualtieri", "207"),
                   Passenger("Silvio", "Dante", "208"),
                   Passenger("Bobby", "Bacala", "209"),
                   Passenger("Janice", "Soprano", "210"),
                   Passenger("Artie", "Bucco", "211"),
                   Passenger("Richie", "Aprile", "212"),
                   Passenger("Junior", "Soprano", "213")]

    passengers6 = [Passenger("Charles", "Xavier", "301"),
                     Passenger("Scott", "Summers", "302"),
                     Passenger("Jean", "Grey", "303"),
                     Passenger("Logan", "Howlett", "304"),
                     Passenger("Ororo", "Munroe", "305"),
                     Passenger("Hank", "McCoy", "306"),
                     Passenger("Kurt", "Wagner", "307"),
                     Passenger("Bobby", "Drake", "308"),
                     Passenger("Warren", "Worthington", "309"),
                     Passenger("Remy", "LeBeau", "310"),
                     Passenger("Piotr", "Rasputin", "311"),
                     Passenger("Kitty", "Pryde", "312"),
                     Passenger("Jubilee", "Lee", "313"),
                     Passenger("Emma", "Frost", "314")]

    plane1 = Plane("Plane1", "Airline1", 90, "Destination1", passengers1)
    plane2 = Plane("Plane2", "Airline2", 80, "Destination2", passengers2)
    plane3 = Plane("Plane3", "Airline3", 100, "Destination3", passengers3)
    plane4 = Plane("Mistery Machine", "Airline1", 100, "Destination4", passengers4)
    plane5 = Plane("Sopranos", "Airline2", 100, "Destination5", passengers5)
    plane6 = Plane("X-men", "Airline3", 100, "Destination6", passengers6)

    planes = [plane1, plane2, plane3]

    passengers_repository = PassengersRepository()
    planes_repository = PlanesRepository(planes)
    service = Service(passengers_repository, planes_repository)
    console = Console(service)
    console.run()


if __name__ == "__main__":
    run_tests()
    main()
