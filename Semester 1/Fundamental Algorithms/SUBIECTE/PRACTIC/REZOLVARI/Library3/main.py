from domain.book import Book
from infrastructure.library import Library


def main():

    books = [Book(447, "A portrait"),
             Book(225, "The lord of the rings"),
             Book(172, "Under the volcano"),
             Book(301, "The invisible man"),
             Book(352, "An american tragedy")]

    library = Library(books)

    library.test_get_books_with_pages_more_than_value()

    for b in library.get_all():
        print(str(b))
    print("\n")

    library.delete_book("A portrait")

    for b in library.get_all():
        print(str(b))
    print("\n")

    try:
        library.get_books_with_pages_more_than_value(500)
    except ValueError as ve:
        print(str(ve))

    for b in library.get_books_with_pages_more_than_value(300):
        print(str(b))
    print("\n")

    for b in library.get_books_with_starting_title_1("The"):
        print(str(b))
    print("\n")

    for b in library.get_books_with_starting_title_2("The"):
        print(str(b))
    print("\n")


main()
