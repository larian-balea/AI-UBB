from domain.book import Book
from infrastructure.library import Library

books = [Book(386, "Brave new word"),
           Book(228, "The sound and the fury"),
           Book(150, "Lolita"),
           Book(248, "An american tragedy"),
           Book(135, "Darkness at noon")]


def print_menu():
    print("\n"
          "0. Exit \n"
          "1. Udpate book at position \n"
          "2. Get books with maximum number of pages \n"
          "3. Get books with title lenght equal to value 1 \n"
          "4. Get books with title lenght equal to value 2 \n")


def main():
    repo = Library(books)
    while True:
        repo.print_all()
        print_menu()
        x = int(input("Enter command: "))
        if x == 0:
            return
        elif x == 1:
            position = input("Enter position: ")
            pages = input("Enter number of pages: ")
            name = input("Enter name: ")
            try:
                position = int(position)
                pages = int(pages)
                repo.update_book_at_position(position, pages, name)
            except ValueError as ve:
                print(str(ve))
        elif x == 2:
            try:
                maxx = repo.get_books_with_max_number_of_pages()
                for book in maxx:
                    print(str(book))
            except ValueError as ve:
                print(str(ve))
        elif x == 3:
            value = input("Enter value: ")
            try:
                value = int(value)
                filtered = repo.get_books_with_title_lenght_equal_to_value1(value)
                for book in filtered:
                    print(str(book))
            except ValueError as ve:
                print(str(ve))
        elif x == 4:
            value = input("Enter value: ")
            try:
                value = int(value)
                filtered = repo.get_books_with_title_lenght_equal_to_value2(value)
                for book in filtered:
                    print(str(book))
            except ValueError as ve:
                print(str(ve))
        else:
            print("Invalid command!")


main()
