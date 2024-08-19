class WorkoutRoutine:
    def __init__(self, id, name, type, difficulty, duration):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__difficulty = difficulty
        self.__duration = duration

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_difficulty(self):
        return self.__difficulty

    def get_duration(self):
        return self.__duration

    def set_id(self, id):
        if not id or not isinstance(id, int) or id < 0:
            raise ValueError("Invalid id!")
        self.__id = id

    def set_name(self, name):
        if name == "":
            raise ValueError("Invalid name!")
        self.__name = name

    def set_type(self, type):
        if type not in ["cardio", "strenght", "flexibility"]:
            raise ValueError("Invalid type!")
        self.__type = type

    def set_difficulty(self, difficulty):
        if not isinstance(difficulty, int) or not 0 <= difficulty <= 5:
            raise ValueError("Invalid difficulty level!")
        self.__difficulty = difficulty

    def set_duration(self, duration):
        if not isinstance(duration, int) or duration < 1:
            raise ValueError("Invalid duration!")
        self.__duration = duration

    def validate(self):
        er = ""
        id = self.get_id()
        name = self.get_name()
        type = self.get_type()
        difficulty = self.get_difficulty()
        duration = self.get_duration()

        if not id or not isinstance(id, int) or id < 0:
            er += "Invalid id!\n"
        if name == "":
            er += "Invalid name!\n"
        if type not in ["cardio", "strenght", "flexibility"]:
            er += "Invalid type!\n"
        if not isinstance(difficulty, int) or not 0 <= difficulty <= 5:
            er += "Invalid difficulty level!\n"
        if not isinstance(duration, int) or duration < 1:
            er += "Invalid duration!\n"
        if er != "":
            raise ValueError(er)
        return 1

    def __str__(self):
        return str(self.get_id()) + ". " + self.get_name() + " - " + self.get_type() + " - " + str(self.get_difficulty()) + " - " + str(self.get_duration())

    def __eq__(self, other):
        if not isinstance(other, WorkoutRoutine):
            raise ValueError("other not of type!")
        return self.get_id() == other.get_id()
