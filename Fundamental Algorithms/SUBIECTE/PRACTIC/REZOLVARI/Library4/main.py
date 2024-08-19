from domain.book import Book
from infrastructure.library import Library


def main():

    lst = [Book(193, "Invisible man"),
           Book(301, "The lord of the rings"),
           Book(207, "Sons and lovers"),
           Book(301, "Brave new world"),
           Book(169, "Under the volcano")]

    library = Library(lst)

    library.test_books_with_maximum()

    for b in library.get_all():
        print(str(b))
    print("\n")

    library.add(-25, "Iona")
    library.add(54, "")
    library.add(520, "Maths in nature")

    for b in library.get_all():
        print(str(b))
    print("\n")

    library.delete(6)
    library.delete(5)

    for b in library.get_all():
        print(str(b))
    print("\n")

    for b in library.books_with_maximum():
        print(str(b))
    print("\n")

    for b in library.get_books_with_title_1(15):
        print(str(b))
    print("\n")

    for b in library.get_books_with_title_2(15):
        print(str(b))
    print("\n")


main()