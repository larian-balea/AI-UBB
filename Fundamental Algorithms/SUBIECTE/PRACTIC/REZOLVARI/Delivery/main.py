from domain.package import Package
from repo.repo import Repo


def main():
    packages = [Package(5423, "Cluj-Napoca", 2.5),
                Package(4321, "Targu-Mures", 5.5)]

    repo = Repo(packages)

    repo.test_average_weight()

    for p in repo.get_all():
        print(str(p))
    print("\n")

    repo.add(4357, "Cluj-Napoca", 1)
    for p in repo.get_all():
        print(str(p))
    print("\n")

    print(repo.average_weight("Cluj-Napoca"))
    print("\n")

    sorted_list = repo.sort_packages()
    for p in sorted_list:
        print(str(p))
    print("\n")


main()
