class Book:
    def __init__(self, pages, title):
        self.__pages = pages
        self.__title = title

    def get_pages(self):
        return self.__pages

    def get_title(self):
        return self.__title

    def __str__(self):
        return str(self.get_pages()) + " - " + self.get_title()
