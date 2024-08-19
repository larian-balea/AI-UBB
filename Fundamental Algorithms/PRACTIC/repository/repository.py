from domain.workout_routine import WorkoutRoutine


class Repo:
    def __init__(self, workouts):
        self.__workouts = workouts

    def get_all(self):
        return self.__workouts

    def add_workout(self, id, name, type, difficulty, duration):
        """
        It adds a workout to the repo
        In:
        :param id: int
        :param name: string
        :param type: string
        :param difficulty: int
        :param duration: int
        Out: -
        Errors: ValueError if any input is invalid
        :return:
        """
        workout = WorkoutRoutine(id, name, type, difficulty, duration)
        try:
            workout.validate()
            self.__workouts.append(workout)
        except ValueError as ve:
            return str(ve)

    def sort_workouts_descending_based_on_difficulty(self):
        """
        It sorts elements of repo based on difficulty descending
        In: -
        Out: list of workouts
        Error: -
        :return:
        """
        workouts = self.get_all()
        return list(sorted(workouts, key=lambda x: x.get_difficulty(), reverse=True))

    def remove_workouts_of_strenght_and_difficulty_greater_than_3(self):
        """

        :return:
        """
        for workout in self.get_all()[:]:
            if workout.get_type() == "strenght" and workout.get_difficulty() > 3:
                self.__workouts.remove(workout)


def repo_tests():
    w = [WorkoutRoutine(1, "Ana", "cardio", 2, 45),
         WorkoutRoutine(2, "Radu", "strenght", 4, 30),
         WorkoutRoutine(3, "Cezara", "flexibility", 5, 20)]
    workouts = []
    repo = Repo(workouts)
