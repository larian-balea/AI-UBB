class Recipe:
    def __init__(self, id, name, type, difficulty, time):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__difficulty = difficulty
        self.__time = time

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_difficulty(self):
        return self.__difficulty

    def get_time(self):
        return self.__time

    def set_time(self, time):
        self.__time = time

    def __str__(self):
        return str(self.get_id()) + " - " + self.get_name() + " - " + self.get_type() + " - " + str(self.get_difficulty()) + " - " + str(self.get_time())
