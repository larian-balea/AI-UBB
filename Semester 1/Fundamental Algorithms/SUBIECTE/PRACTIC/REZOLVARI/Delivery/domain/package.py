class Package:
    def __init__(self, serial_number, destination, weight):
        self.__serial_number = serial_number
        self.__destination = destination
        self.__weight = weight

    def get_serial_number(self):
        return self.__serial_number

    def get_destination(self):
        return self.__destination

    def get_weight(self):
        return self.__weight

    def set_serial_number(self, serial_number):
        if not isinstance(serial_number, int):
            raise ValueError("not int!")
        self.__serial_number = serial_number

    def set_destination(self, destination):
        if not isinstance(destination, str):
            raise ValueError("not str!")
        self.__destination = destination

    def set_weight(self, weight):
        if isinstance(weight, int):
            weight = float(weight)
        if not isinstance(weight, float):
            raise ValueError("not float!")
        self.__weight = weight

    def validate(self):
        serial_number = self.get_serial_number()
        destination = self.get_destination()
        weight = self.get_weight()
        error = ""
        if not isinstance(serial_number, int):
            error += "not int!\n"
        if not isinstance(destination, str):
            error += "not str!\n"
        if isinstance(weight, int):
            weight = float(weight)
        if not isinstance(weight, float):
            error += "not float!\n"
        if error == "":
            return 0
        raise ValueError(error)

    def __str__(self):
        return str(self.get_serial_number()) + ' - ' + self.get_destination() + ' - ' + str(self.get_weight())
