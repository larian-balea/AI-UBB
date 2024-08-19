from domain.book import Book


class Library:
    def __init__(self, books):
        self.__books = books

    def get_all(self):
        return self.__books

    def print_all(self):
        for book in self.get_all():
            print(str(book))

    def update_book_at_position(self, position, pages, name):
        books = self.get_all()
        if len(books) == 0:
            raise ValueError("There are no books!")
        if pages <= 0:
            raise ValueError("Number of pages should be greater than 0!")
        if len(filter(lambda x: x.get_name() == name, books)) != 0:
            raise ValueError("There is already book with given name!")
        if not 0 <= position <= len(books-1):
            raise ValueError("Given position not in list limits!")
        books[position].set_name(name)
        books[position].set_pages(pages)

    def get_books_with_max_number_of_pages(self):
        books = self.get_all()
        if len(books) == 0:
            raise ValueError("There are no books!")
        maximum = list(sorted(books, key=lambda x: x.get_pages()))[0]
        return list[filter(lambda x: x.get_pages() == maximum, books)]

    def get_books_with_title_lenght_equal_to_value1(self, value):
        books = self.get_all()
        if len(books) == 0:
            raise ValueError("There are no books!")
        return list(filter(lambda x: len(x.get_name()) == value, books))

    def get_books_with_title_lenght_equal_to_value2(self, value):
        books = self.get_all()
        if len(books) == 0:
            raise ValueError("There are no books!")
        for book in books:
            if len(book.get_name()) == value:
                yield book


def library_tests():
    books = []
    repo = Library(books)
    try:
        repo.get_books_with_max_number_of_pages()
        assert False
    except ValueError as ve:
        assert str(ve) == "There are no books!"
    b1 = Book(120, "Metamorphosis")
    books.append(b1)
    assert repo.get_books_with_max_number_of_pages() == [b1]
    b2 = Book(500, "The idiot")
    b3 = Book(500, "The Master and Margarita")
    assert repo.get_books_with_max_number_of_pages() == [b2, b3]


library_tests()
