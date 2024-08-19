from domain.workout import Workout


class Repo:
    def __init__(self, workouts):
        self.__workouts = workouts

    def get_all(self):
        return self.__workouts

    def add(self, id, name, type, difficutly, duration):
        """
        It adds an item to the list
        In: id: int
            name: str
            type: str
            difficutly: int
            duration: int
        Out: -
        Error: ValueError
        """
        listt = self.get_all()
        w = Workout(id, name, type, difficutly, duration)
        try:
            w.validation()
            for x in listt:
                if x.get_id() == id:
                    raise ValueError("already in list!")
            listt.append(w)
        except ValueError as ve:
            raise ValueError(ve)

    def sort_descending(self):
        """
        It sorts the list in descending order by difficulty
        In: -
        Out: list of Workout objects
        Error: ValueError
        """
        listt = self.get_all()
        if not listt:
            raise ValueError("empty list")
        return list(sorted(listt, key=lambda x: x.get_difficulty(), reverse=True))

    def remove_workouts(self):
        listt = self.get_all()
        if not listt:
            raise ValueError("empty list")
        for i in listt[:]:
            if i.get_type() == "strenght" and i.get_difficulty() > 3:
                listt.remove(i)

    def tests(self):
        w = [Workout(1, "Ana", "strenght", 5, 90),
             Workout(2, "Mihai", "cardio", 3, 20),
             ]
        r = Repo(w)
        r.add(3, "Irina", "flexibility", 4, 15)
        assert len(r.get_all()) == 3

