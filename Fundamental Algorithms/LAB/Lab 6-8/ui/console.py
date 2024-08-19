from repository.point_repository import PointRepository
from domain.mypoint import MyPoint


def print_menu():
    """the menu interface for the application"""
    print("▶ 0. End the program                                 ▶ 7.  Update a point at a given index \n"
          "▶ 1. Add a point to the repository list              ▶ 8.  Delete a point at a given index \n"
          "▶ 2. Get all points                                  ▶ 9.  Delete all points that are inside a given square \n"
          "▶ 3. Get a point at a given index                    ▶ 10. Plot all points inside a chart \n"
          "▶ 4. Get all points of a given color                 ▶ 13. Get the maximum distance between 2 points \n"
          "▶ 5. Get all points that are inside a given square   ▶ 16. Shift all points on the x-axis \n"
          "▶ 6. Get the minimum distance between 2 points       ▶ 19. Delete all points that are inside a given circle \n"
          )


def console():
    print_menu()
    """
    repo = PointRepository()
    """

    repo = PointRepository([MyPoint(0, 0, 'red'),
                            MyPoint(0, 1, 'green'),
                            MyPoint(0, 2, 'blue'),
                            MyPoint(0, 3, 'red'),
                            MyPoint(2, 5, 'magenta'),
                            MyPoint(1, 2, 'red'),
                            MyPoint(2, 3, 'yellow'),
                            MyPoint(3, 4, 'green'),
                            MyPoint(1, 1, 'blue'),
                            MyPoint(2, 2, 'red'),
                            ])

    while True:
        try:
            command = int(input("● Which feature would you like to use? give any number [0-13]: "))
        except ValueError:
            print("❗ Command should be an integer [0-13] ❗")
            continue

        if command == 0:
            print("▶ The program has ended")
            break

        elif command == 1:
            try:
                x = int(input("● Give the coordonate x: "))
                y = int(input("● Give the coordonate y: "))
                color = input("● Give the color: ")
                point = MyPoint(x, y, color)
                repo.add_point(point)
                print("▶ The point was added successfully")
            except ValueError as err:
                print(err)
            except Exception as err:
                print(err)

        elif command == 2:
            print("▶ The list of points is: ")
            for point in repo.get_all():
                print(point)

        elif command == 3:
            try:
                index = int(input("● Give the index: "))
                print("▶ The point at the given index is: ", repo.get_point(index))
            except ValueError as err:
                print(err)
            except Exception as err:
                print(err)

        elif command == 4:
            color = input("● Give the color: ")
            if color not in ['red', 'green', 'blue', 'yellow', 'magenta']:
                print("❗ Invalid color ❗")
            else:
                print("▶ The list of points at the given color is: ")
                for point in repo.get_points_of_color(color):
                    print(point)

        elif command == 5:
            try:
                up_left_corner_x = int(input("● Give the coordonate x of the up left corner: "))
                up_left_corner_y = int(input("● Give the coordonate y of the up left corner: "))
                lenght = int(input("● Give the lenght of the square: "))
                print("▶ The list of points inside the square is: ")
                for point in repo.get_points_in_square(up_left_corner_x, up_left_corner_y, lenght):
                    print(point)
            except ValueError as err:
                print(err)
            except Exception as err:
                print(err)

        elif command == 6:
            try:
                print("▶ The minimum distance is: ", repo.minimum_distance())
            except ValueError as err:
                print(err)
            except Exception as err:
                print(err)

        elif command == 7:
            try:
                index = int(input("● Give the index: "))
                x = int(input("● Give the coordonate x: "))
                y = int(input("● Give the coordonate y: "))
                color = input("● Give the color: ")
                point = MyPoint(x, y, color)
                repo.update_point(index, point)
                print("▶ The point was updated successfully")
            except ValueError as err:
                print(err)
            except Exception as err:
                print(err)

        elif command == 8:
            try:
                index = int(input("● Give the index: "))
                repo.delete_point(index)
                print("▶ The point was deleted successfully")
            except ValueError as err:
                print(err)
            except Exception as err:
                print(err)

        elif command == 9:
            try:
                up_left_corner_x = int(input("● Give the coordonate x of the up left corner: "))
                up_left_corner_y = int(input("● Give the coordonate y of the up left corner: "))
                lenght = int(input("● Give the lenght of the square: "))
                repo.delete_points_in_square(up_left_corner_x, up_left_corner_y, lenght)
                print("▶ The points were deleted successfully")
            except ValueError as err:
                print(err)
            except Exception as err:
                print(err)

        elif command == 10:
            repo.plot_points()
            print("▶ The points were plotted successfully")

        elif command == 13:
            try:
                print("▶ The maximum distance is: ", repo.maximum_distance())
            except ValueError as err:
                print(err)
            except Exception as err:
                print(err)

        elif command == 16:
            try:
                amount = int(input("● Give the amount to add to all x coordinate of all points: "))
                repo.shift_points_on_x_axis(amount)
            except ValueError as err:
                print(err)
            except Exception as err:
                print(err)

        elif command == 19:
            try:
                center_x = int(input("● Give the coordonate x of the center: "))
                center_y = int(input("● Give the coordonate y of the center: "))
                radius = int(input("● Give the radius of the circle: "))
                repo.delete_points_in_circle(center_x, center_y, radius)
                print("▶ The points were deleted successfully")
            except ValueError as err:
                print(err)
            except Exception as err:
                print(err)

        else:
            print("❗ That number is not on the list of options ❗")
