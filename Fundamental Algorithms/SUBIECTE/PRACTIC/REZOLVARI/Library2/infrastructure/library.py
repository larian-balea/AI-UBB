from domain.book import Book


class Repo:
    def __init__(self, books):
        self.__books = books

    def get_all(self):
        return self.__books

    def delete_book(self, position):
        """
        Deletes book at position in list
        In: position - int
        Out: -
        Errors: ValueError - if list is empty or the position is greater than number of books in list
        """
        books = self.get_all()
        if not books:
            raise ValueError("no books in list!")
        if len(books) < position:
            raise ValueError("position greater than number of books in list!")
        books.pop(position)

    def get_books_with_average_number_of_pages(self):
        """
        Gets books with average number of pages
        In: -
        Out: list of Books
        Errors: ValueError - if list is empty or there are no such books
        """
        books = self.get_all()
        if not books:
            raise ValueError("no books in list!")
        average = 0
        for b in books:
            average += b.get_number_of_pages()
        average /= len(books)
        acceptable = list(filter(lambda x: x.get_number_of_pages() == average, books))
        if not acceptable:
            raise ValueError("no books with average number of pages!")
        return acceptable

    def filter_books_which_contain_string_1(self, string):
        books = self.get_all()
        if not books:
            raise ValueError("no books in list!")
        acceptable = list(filter(lambda x: string in x.get_title(), books))
        if not acceptable:
            raise ValueError("no books with average number of pages!")
        return acceptable

    def filter_books_which_contain_string_2(self, string):
        books = self.get_all()
        if not books:
            raise ValueError("no books in list!")
        acceptable = []
        for b in books:
            if string in b.get_title():
                acceptable.append(b)
        if not acceptable:
            raise ValueError("no books with average number of pages!")
        return acceptable

    @staticmethod
    def test_get_books_with_average_number_of_pages():
        books = []
        repo = Repo(books)
        try:
            repo.get_books_with_average_number_of_pages()
            assert False
        except ValueError as ve:
            assert str(ve) == "no books in list!"

        books = [Book(358, "Darkness at noon")]
        repo = Repo(books)
        assert repo.get_books_with_average_number_of_pages() == [Book]
