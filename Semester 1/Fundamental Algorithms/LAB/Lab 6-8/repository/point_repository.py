from domain.mypoint import MyPoint
import matplotlib.pyplot as plt


class PointRepository:
    def __init__(self, initial_values=None):
        if initial_values is None:
            initial_values = []
        self.__points = []
        if initial_values is not None:
            for value in initial_values:
                if isinstance(value, MyPoint):
                    self.__points.append(value)

    def check_if_exists(self, point_to_add):
        for i in range(len(self.__points)):
            if self.__points[i].get_x() == point_to_add.get_x() and \
                    self.__points[i].get_y() == point_to_add.get_y():
                return True
        return False

    # 1. Add a point
    def add_point(self, point):
        """
        Add a point to the list
        In: point - Point - (int, int, str)
        Out: -
        Error: RepoError - if the point is already in the list
        """
        if self.check_if_exists(point) is True:
            raise ValueError("Point already exists!\n")
        else:
            self.__points.append(point)

    # 2. Get all points
    def get_all(self):
        """
        Return all the points
        In: -
        Out: points - list of points
        Error: -
        """
        return self.__points

    # 3. Get a point from a given index
    def get_point(self, index):
        """
        Return the point from the given index
        In: index - int
        Out: point - Point - (int, int, str)
        Error: RepoError - if the index is not valid
        """
        if index < 0 or index >= len(self.__points):
            raise ValueError("Invalid index!\n")
        else:
            return self.__points[index]

    # 4. Get all points of a given color
    def get_points_of_color(self, color):
        """
        Return all the points of the given color
        In: color - str
        Out: points - list of points
        Error: -
        """
        return [point for point in self.__points if point.get_color() == color]

    # 5. Get all points in a given square
    def get_points_in_square(self, up_left_corner_x, up_left_corner_y, lenght):
        """
        Return all the points in the given square
        In: up_left_corner_x - int
            up_left_corner_y - int
            lenght - int
        Out: in_square - list of points
        Error: -
        """
        in_square = []
        for point in self.__points:
            if up_left_corner_x <= point.get_x() <= up_left_corner_x + lenght and \
               up_left_corner_y - lenght <= point.get_y() <= up_left_corner_y:
                in_square.append(point)
        return in_square

    # Get the distance between two points
    @staticmethod
    def distance(point1, point2):
        """
        Return the distance between two points
        In: point1 - Point - (int, int, str)
            point2 - Point - (int, int, str)
        Out: distance - float
        Error: -
        """
        return ((point1.get_x() - point2.get_x()) ** 2 + (point1.get_y() - point2.get_y()) ** 2) ** 0.5

    # 6. Get the minimum distance between 2 points
    def minimum_distance(self):
        """
        Return the minimum distance between 2 point of the list
        In:
        Out: minimum - float
        Error:
        """
        minimum = self.distance(self.get_all()[0], self.get_all()[1])
        for point1 in self.get_all():
            copy = self.get_all()[:]
            copy.remove(point1)
            for point2 in copy:
                minimum = min(self.distance(point1, point2), minimum)
        return minimum

    # 7. Update a point
    def update_point(self, index, new_point):
        """
        Update a point from the list
        In: index - int
            new_point - Point - (int, int, str)
        Out: -
        Error: ValueError - if the index is not valid
        """
        if index < 0 or index >= len(self.__points):
            raise ValueError("Invalid index!\n")
        else:
            self.__points[index] = new_point

    # 8. Delete a point at given index
    def delete_point(self, index):
        """
        Delete a point from the list
        In: index - int
        Out: -
        Error: ValueError - if the index is not valid
        """
        if index < 0 or index >= len(self.__points):
            raise ValueError("Invalid index!\n")
        else:
            self.__points.pop(index)

    # 9. Delete all points that are inside a given square
    def delete_points_in_square(self, up_left_corner_x, up_left_corner_y, lenght):
        """
        Delete all the points in the given square
        In: up_left_corner_x - int
            up_left_corner_y - int
            lenght - int
        Out: -
        Error: -
        """
        to_delete = self.get_points_in_square(up_left_corner_x, up_left_corner_y, lenght)
        for point in to_delete:
            self.__points.remove(point)

    # 10.
    def plot_points(self):
        """
        Plot the points
        """
        x = [float(point.get_x()) for point in self.__points]
        y = [float(point.get_y()) for point in self.__points]
        color = [point.get_color() for point in self.__points]
        plt.scatter(x, y, c=color)
        plt.show()

    # 11. Get all points in a given circle
    def get_points_in_circle(self, center_x, center_y, radius):
        """
        Return all the points in the given circle
        In: center_x - int
            center_y - int
            radius - int
        Out: in_circle - list of points
        Error: -
        """
        in_circle = []
        center = MyPoint(center_x, center_y, 'red')
        for point in self.__points:
            if self.distance(point, center) <= radius:
                in_circle.append(point)
        return in_circle

    # 12. Get all points in a given rectangle
    def get_points_in_rectangle(self, up_left_corner_x, up_left_corner_y, lenght, width):
        """
        Returns all points in the given rectangle
        In: up_left_corner_x - int
            up_left_corner_y - int
            lenght - int
            width - int
        Out: in_rectangle - list of points
        Error: -
        """
        in_rectangle = []
        for point in self.__points:
            if up_left_corner_x <= point.get_x() <= up_left_corner_x + lenght and \
                    up_left_corner_y - width <= point.get_y() <= up_left_corner_y:
                in_rectangle.append(point)
        return in_rectangle

    # 13. Get the maximum distance between 2 points
    def maximum_distance(self):
        """
        Return the maximum distance between 2 point of the list
        In:
        Out: maximum - float
        Error:
        """
        maximum = 0
        for point1 in self.get_all():
            copy = self.get_all()[:]
            copy.remove(point1)
            for point2 in copy:
                maximum = max(self.distance(point1, point2), maximum)
        return maximum

    # 14. Get the number of points of a given color
    def get_number_of_points_of_color(self, color):
        return len(self.get_points_of_color(color))

    # 15. Update color of point by coordinates
    def update_color_of_point_by_coordinates(self, coordinate_x, coordinate_y, color):
        """
        It updates the color of a point by coordinates
        In: coordinate_x - int
            coordinate_y - int
            color - str
        Out: -
        Error: if the point does not exist
        """
        for point in self.get_all():
            if point.get_x() == coordinate_x and point.get_y() == coordinate_y:
                point.set_color(color)
                break
        else:
            raise ValueError("Point (" + str(coordinate_x) + ", " + str(coordinate_y) + ") does not exist!\n")

    # 16. Shift all points on the x-axis
    def shift_points_on_x_axis(self, amount):
        """
        It shifts all points on the x-axis by a given amount
        In: amount - int
        Out: -
        Error: -
        :return:
        """
        for point in self.get_all():
            point.set_x(point.get_x() + amount)

    # 17. Shift all points on the y-axis
    def shift_points_on_y_axis(self, amount):
        """
        It shifts all points on the y-axis by a given amount
        In: amount - int
        Out: -
        Error: -
        :return:
        """
        for point in self.get_all():
            point.set_x(point.get_y() + amount)

    # 18. Delete a point by coordinates
    def delete_point_by_coordinates(self, coordinate_x, coordinate_y):
        """
        It deletes a point by coordinates
        In: coordinate_x - int
            coordinate_y - int
        Out: -
        Error: if the point does not exist
        """
        for point in self.get_all():
            if point.get_x() == coordinate_x and point.get_y() == coordinate_y:
                self.delete_point(self.get_all().index(point))
                break
        else:
            raise ValueError("Point (" + str(coordinate_x) + ", " + str(coordinate_y) + ") does not exist!\n")

    # 19. Delete all points that are inside a given circle
    def delete_points_in_circle(self, center_x, center_y, radius):
        """
        Delete all the points in the given circle
        In: center_x - int
            center_y - int
            radius - int
        Out: -
        Error: -
        """
        to_delete = self.get_points_in_circle(center_x, center_y, radius)
        for point in to_delete:
            self.__points.remove(point)

    # 20. Delete all points within a certain distance from a given point
    def delete_points_within_distance_from_point(self, coordinate_x, coordinate_y, distance):
        """
        It deletes all points within a certain distance from a given point
        In: coordinate_x - int
            coordinate_y - int
            distance - int
        Out: -
        Error: -
        """
        to_delete = []
        for point in self.get_all():
            if self.distance(point, MyPoint(coordinate_x, coordinate_y, 'Should not be added')) <= distance:
                to_delete.append(point)
        for point in to_delete:
            self.__points.remove(point)
