class MyPoint:

    def __init__(self, coord_x, coord_y, color):
        """
        Creates a new point with coordonate x, coordonate y and color
        """
        if type(coord_x) == int:
            self.__coord_x = coord_x
        else:
            raise ValueError("coordinate x must be a number")

        if type(coord_y) == int:
            self.__coord_y = coord_y
        else:
            raise ValueError("coordinate y must be a number")

        if type(color) == str:
            if color in ["red", "blue", "green", "magenta", "yellow"]:
                self.__color = color
            else:
                raise ValueError("color is not correct, must be on the list red, blue, green, magenta, yellow")
        else:
            raise ValueError("color must be a string")

    def get_x(self):
        """
        Returns the coordonate x of the point
        In: -
        Out: the coordonate x of the point
        Error: -
        """
        return self.__coord_x

    def get_y(self):
        """
        Returns the coordonate y of the point
        In: -
        Out: the coordonate y of the point
        Error: -
        """
        return self.__coord_y

    def get_color(self):
        """
        Returns the color of the point
        In: -
        Out: the color of the point
        Error: -
        """
        return self.__color

    def set_x(self, coord_x):
        """
        Sets the coordonate x of the point
        In: coord_x - int
        Out: -
        Error: -
        """
        if not isinstance(coord_x, int):
            raise ValueError("Invalid coordonate x!\n")
        self.__coord_x = coord_x

    def set_y(self, coord_y):
        """
        Sets the coordonate y of the point
        In: coord_y - int
        Out: -
        Error: -
        """
        if not isinstance(coord_y, int):
            raise ValueError("Invalid coordonate y!\n")
        self.__coord_y = coord_y

    def set_color(self, color):
        """
        Sets the color of the point
        In: color - string (one from: 'red', 'green', 'blue', 'yellow', 'magenta')
        Out: -
        Error:
        """
        if color in ['red', 'green', 'blue', 'yellow', 'magenta']:
            self.__color = color
        else:
            raise ValueError("Invalid color!\n")

    def __str__(self):
        """
        Returns a string representation of the point
        In: -
        Out: a string representation of the point
        Error: -
        """
        return 'Point (' + str(self.__coord_x) + ',' + str(self.__coord_y) + ') of color ' + self.__color


MyPoint(1, 2, 'red')
MyPoint(2, 3, 'blue')
MyPoint(3, 4, 'green')
MyPoint(4, 5, 'yellow')
MyPoint(5, 6, 'magenta')
MyPoint(6, 7, 'red')
MyPoint(7, 8, 'blue')
MyPoint(8, 9, 'green')
MyPoint(9, 10, 'yellow')
MyPoint(10, 11, 'magenta')
