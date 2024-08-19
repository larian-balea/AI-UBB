from domain.book import Book
from infrastructure.library import Repo


def main():
    books = [Book(358, "Darkness at noon"),
             Book(302, "Under the volcano"),
             Book(411, "Native son"),
             Book(330, "Sons and lovers"),
             Book(330, "Lolita")]

    repo = Repo(books)

    for b in repo.get_all():
        print(str(b))
    print("\n")

    try:
        repo.delete_book(7)
    except ValueError as ve:
        print(str(ve))

    repo.delete_book(2)

    for b in repo.get_all():
        print(str(b))
    print("\n")

    for b in repo.get_books_with_average_number_of_pages():
        print(str(b))
    print("\n")

    for b in repo.filter_books_which_contain_string_1("on"):
        print(str(b))
    print("\n")

    for b in repo.filter_books_which_contain_string_2("on"):
        print(str(b))
    print("\n")


main()
