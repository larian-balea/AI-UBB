class Book:
    def __init__(self, pages, name):
        self.__pages = pages
        self.__name = name

    def get_name(self):
        return self.__name

    def get_pages(self):
        return self.__pages

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("name not string!")
        self.__name = name

    def set_pages(self, pages):
        if not isinstance(pages, int):
            raise ValueError("Number of pages not integer!")
        if pages <= 0:
            raise ValueError("Number of pages should be greater than 0!")
        self.__pages = pages

    def __str__(self):
        return str(self.get_pages()) + " pages" + " - " + self.get_name()

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, Book):
            raise ValueError("other is not Book!")
        return self.get_name() == other.get_name()
