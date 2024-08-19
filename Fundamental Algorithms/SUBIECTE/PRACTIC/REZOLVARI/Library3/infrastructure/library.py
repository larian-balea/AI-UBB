from domain.book import Book


class Library:
    def __init__(self, books):
        self.__books = books

    def get_all(self):
        return self.__books

    def delete_book(self, title):
        """
        It deletes the book with the given title
        In: title - string
        Out: -
        Error: ValueError - if there are no books or there is no book with given title
        """
        books = self.get_all()
        if not books:
            raise ValueError("there are no books!")
        ok = 0
        for book in books:
            if book.get_title() == title:
                ok = 1
                books.remove(book)
        if ok == 0:
            raise ValueError("no book with title!")

    def get_books_with_pages_more_than_value(self, value):
        """
        It returns the books that have the number of pages greater than given value
        In: value - int
        Out: ok_books - list of Book instances
        Error: ValueError - if there are no books or there are no books with given atrubute
        """
        books = self.get_all()
        if not books:
            raise ValueError("there are no books!")
        ok_books = list(filter(lambda x: x.get_pages() > value, books))
        if not ok_books:
            raise ValueError("there are no such books!")
        return ok_books

    def get_books_with_starting_title_1(self, three_letters):
        """
        It returns the books that have the first 3 letters the given 3 letters
        In: three_letters - string of 3 letters
        Out: ok_books - list of Book instances
        Error: ValueError - if there are no books or there are no books with given atrubute
        """
        if len(three_letters) != 3:
            raise ValueError("there are not 3 letters!")
        books = self.get_all()
        if not books:
            raise ValueError("there are no books!")
        ok_books = list(filter(lambda x: x.get_title()[:3] == three_letters, books))
        if not ok_books:
            raise ValueError("there are no such books!")
        return ok_books

    def get_books_with_starting_title_2(self, three_letters):
        """
        It returns the books that have the first 3 letters the given 3 letters
        In: three_letters - string of 3 letters
        Out: ok_books - list of Book instances
        Error: ValueError - if there are no books or there are no books with given atrubute
        """
        if len(three_letters) != 3:
            raise ValueError("there are not 3 letters!")
        books = self.get_all()
        if not books:
            raise ValueError("there are no books!")
        ok_books = []
        for b in books:
            if b.get_title()[:3] == three_letters:
                ok_books.append(b)
        if not ok_books:
            raise ValueError("there are no such books!")
        return ok_books

    @staticmethod
    def test_get_books_with_pages_more_than_value():
        books = []
        l = Library(books)
        try:
            l.get_books_with_pages_more_than_value(200)
            assert False
        except ValueError as ve:
            assert str(ve) == "there are no books!"

        books = [Book(172, "Under the volcano")]
        l = Library(books)

        try:
            l.get_books_with_pages_more_than_value(200)
            assert False
        except ValueError as ve:
            assert str(ve) == "there are no such books!"

        assert l.get_books_with_pages_more_than_value(100) == books
        print("TESTS PASSED!\n")
