from domain.workout import Workout
from infrastructure.repo import Repo


def main():
    w = [Workout(1, "Ana", "strenght", 5, 90),
         Workout(2, "Mihai", "cardio", 3, 20),
         ]

    r = Repo(w)

    for i in r.get_all():
        print(str(i))
    print("\n")

    r.add(3, "Irina", "flexibility", 4, 15)

    try:
        r.add(1, "Irina", "flexibility", 4, 15)
    except ValueError as ve:
        print(str(ve))

    for i in r.get_all():
        print(str(i))
    print("\n")

    for i in r.sort_descending():
        print(str(i))
    print("\n")

    r.remove_workouts()

    for i in r.get_all():
        print(str(i))
    print("\n")


main()
