from domain.workout_routine import WorkoutRoutine
from repository.repository import Repo

w = [WorkoutRoutine(1, "Ana", "cardio", 2, 45),
     WorkoutRoutine(2, "Radu", "strenght", 4, 30),
     WorkoutRoutine(3, "Cezara", "flexibility", 5, 20)]


def main():
    repo = Repo(w)
    while True:
        x = int(input("command: "))
        if x == 0:
            return
        elif x == 1:
            id = input("id: ")
            name = input("name: ")
            type = input("type: ")
            difficulty = input("diff: ")
            duration = input("duration: ")
            try:
                id = int(id)
                difficulty = int(difficulty)
                duration = int(duration)
                repo.add_workout(id, name, type, difficulty, duration)
            except ValueError as ve:
                print(ve)
        elif x == 2:
            a = repo.sort_workouts_descending_based_on_difficulty()
            for i in a:
                print(str(i))
        elif x == 3:
            repo.remove_workouts_of_strenght_and_difficulty_greater_than_3()
            for i in repo.get_all():
                print(str(i))
        else:
            print("invalid")


main()
