class Passenger:
    def __init__(self, first_name, last_name, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number

    def validate(self):
        er = ""
        if self.first_name == "":
            er += "First name cannot be empty!\n"
        elif not self.first_name.isalpha():
            er += "First name must contain only letters!\n"
        if self.last_name == "":
            er += "Last name cannot be empty!\n"
        elif not self.last_name.isalpha():
            er += "Last name must contain only letters!\n"
        if self.passport_number == "":
            er += "Passport number cannot be empty!\n"
        elif not self.passport_number.isnumeric():
            er += "Passport number must be a number!\n"
        if er != "":
            raise ValueError(er)
        return 1

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_passport_number(self):
        return self.passport_number

    def set_first_name(self, first_name):
        if first_name == "":
            raise ValueError('First name cannot be empty!')
        if not first_name.isalpha():
            raise ValueError('First name must contain only letters!')
        self.first_name = first_name

    def set_last_name(self, last_name):
        if last_name == "":
            raise ValueError('Last name cannot be empty!')
        if not last_name.isalpha():
            raise ValueError('Last name must contain only letters!')
        self.last_name = last_name

    def set_passport_number(self, passport_number):
        if passport_number == "":
            raise ValueError('Passport number cannot be empty!')
        if not passport_number.isnumeric():
            raise ValueError('Passport number must be a number!')
        self.passport_number = passport_number

    def __str__(self):
        return 'Name: ' + self.first_name + ' ' + self.last_name + ' ; ' + self.passport_number + '\n'

    def __eq__(self, other):
        if not isinstance(other, Passenger):
            raise ValueError('The object is not a passenger!')
        return self.passport_number == other.passport_number


# p1 = Passenger("John", "Doe", "123456789")
# p2 = Passenger("Jane", "Dye", "987654321")
# print(p1)
