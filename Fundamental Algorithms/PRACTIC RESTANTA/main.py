from domain.recipe import Recipe
from repo.repo import Repo


def main():
    lst = [Recipe(1, "Tiramisu", "italian", 5, 60),
           Recipe(2, "Burrito", "mexican", 8, 100),
           Recipe(3, "Butter Chicken", "indian", 10, 170)]

    r = Repo(lst)

    r.tests()

    for i in r.get_all():
        print(str(i))
    print("\n")

    r.add(1, "Coffee", "italian", 1, 3)
    r.add(4, "", "italian", 1, 3)
    r.add(4, "Coffee", "irish", 1, 3)
    r.add(4, "Coffee", "italian", 11, 3)
    r.add(4, "Coffee", "italian", 1, 0)

    r.add(4, "Coffee", "italian", 1, 3)

    for i in r.get_all():
        print(str(i))
    print("\n")

    for i in r.sortt():
        print(str(i))
    print("\n")

    r.update(4, 2)

    for i in r.get_all():
        print(str(i))
    print("\n")


main()
