from domain.package import Package


class Repo:
    def __init__(self, packages):
        self.__packages = packages

    def get_all(self):
        return self.__packages

    def add(self, serial, destination, weight):
        p = Package(serial, destination, weight)
        packages = self.get_all()
        try:
            p.validate()
            if len(list(filter(lambda x: x.get_serial_number() == serial, packages))) != 0:
                raise ValueError("package already in list!")
            packages.append(p)
        except ValueError as ve:
            return str(ve)

    def average_weight(self, destination):
        packages = self.get_all()
        if not packages:
            raise ValueError("list is empty!")
        to_destination = list(filter(lambda x: x.get_destination() == destination, packages))
        if not to_destination:
            raise ValueError("there are no packages to destination!")
        total = 0
        for i in to_destination:
            total += i.get_weight()
        return total/len(to_destination)

    def sort_packages(self):
        """
        Sorts packages in ascending order by the last digit of the serial number
        In: -
        Out: list of packages
        :return:
        """
        packages = self.get_all()
        if not packages:
            raise ValueError("list is empty!")
        return list(sorted(packages, key=lambda x: x.get_serial_number() % 10))

    @staticmethod
    def test_average_weight():
        packages = []
        repo = Repo(packages)
        try:
            repo.average_weight("Cluj-Napoca")
            assert False
        except ValueError as ve:
            assert str(ve) == "list is empty!"
        repo.add(5423, "Cluj-Napoca", 2.5)
        try:
            repo.average_weight("Bucuresti")
            assert False
        except ValueError as ve:
            assert str(ve) == "there are no packages to destination!"
        assert repo.average_weight("Cluj-Napoca") == 2.5
        repo.add(4357, "Cluj-Napoca", 1)
        assert repo.average_weight("Cluj-Napoca") == 1.75

        print("TESTS PASSED!")
