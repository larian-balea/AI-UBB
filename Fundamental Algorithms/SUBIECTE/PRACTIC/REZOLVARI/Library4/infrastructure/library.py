from domain.book import Book


class Library:
    def __init__(self, lst):
        self.__lst = lst

    def get_all(self):
        return self.__lst

    def add(self, pages, title):
        if not isinstance(pages, int) or pages < 0:
            print("invalid number of pages!\n")
            return
        if not isinstance(title, str) or title == "":
            print("invalid title!\n")
            return
        lst = self.get_all()
        ok = 1
        for b in lst:
            if b.get_title() == title:
                ok = 0
        if ok == 1:
            lst.append(Book(pages, title))

    def delete(self, position):
        lst = self.get_all()
        if position < 0 or position > len(lst) - 1:
            print("outside list!\n")
            return
        lst.pop(position)

    def books_with_maximum(self):
        lst = self.get_all()
        if not lst:
            return
        maxx = list(sorted(lst, key=lambda y: y.get_pages()))[-1].get_pages()
        return list(filter(lambda x: x.get_pages() == maxx, lst))

    def get_books_with_title_1(self, value):
        lst = self.get_all()
        if not lst:
            print("empty list!")
            return
        return list(filter(lambda x: len(x.get_title()) > value, lst))

    def get_books_with_title_2(self, value):
        lst = self.get_all()
        if not lst:
            print("empty list!")
            return
        filtered = []
        for b in lst:
            if len(b.get_title()) > value:
                filtered.append(b)
        return filtered

    @staticmethod
    def test_books_with_maximum():
        lst = []
        l = Library(lst)

        # try:
        #     l.books_with_maximum()
        #     assert False
        # except ValueError as ve:
        #     assert str(ve) == "empty list!"

        assert l.books_with_maximum() is None

        b1 = Book(193, "Invisible man")
        b2 = Book(301, "The lord of the rings")

        l.add(193, "Invisible man")
        assert str(l.books_with_maximum()[0]) == str(b1)

        l.add(301, "The lord of the rings")
        assert str(l.books_with_maximum()[0]) == str(b2)

        print("All test passed!")
