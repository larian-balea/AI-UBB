class Workout:
    def __init__(self, id, name, type, difficutly, duration):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__difficutly = difficutly
        self.__duration = duration

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_difficulty(self):
        return self.__difficutly

    def get_duration(self):
        return self.__duration

    def validation(self):
        id = self.__id
        name = self.__name
        type = self.__type
        difficutly = self.__difficutly
        duration = self.__duration

        er = ""
        if not id:
            er += "id empty \n"
        elif not isinstance(id, int):
            er += "id not int \n"
        if name == "":
            er += "name empty \n"
        if not type in ["cardio", "strenght", "flexibility"]:
            er += "invalid type \n"
        if not difficutly:
            er += "difficulty empty \n"
        if duration < 1:
            er += "invalid duration \n"

        if er != "":
            raise ValueError(str(er))
        return 0

    def __str__(self):
        return str(self.get_id()) + " - " + self.get_name() + " - " + self.get_type() + " - " + str(self.get_difficulty()) + " - " + str(self.get_duration())
