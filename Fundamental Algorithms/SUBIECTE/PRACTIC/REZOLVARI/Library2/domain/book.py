class Book:
    def __init__(self, number_of_pages, title):
        self.__number_of_pages = number_of_pages
        self.__title = title

    def get_number_of_pages(self):
        return self.__number_of_pages

    def get_title(self):
        return self.__title

    def set_number_of_pages(self, number):
        if not isinstance(number, int):
            raise ValueError("not int!")
        self.__number_of_pages = number

    def set_title(self, title):
        if not isinstance(title, str):
            raise ValueError("not string!")
        self.__title = title

    def __str__(self):
        return str(self.get_number_of_pages()) + " - " + self.get_title()
