from domain.mypoint import MyPoint
from repository.point_repository import PointRepository


def test_point():
    p = MyPoint(1, 2, 'red')
    assert p.get_x() == 1
    assert p.get_y() == 2
    assert p.get_color() == 'red'

    p.set_x(3)
    assert p.get_x() == 3
    try:
        p.set_x('a')
        assert False
    except ValueError as ve:
        assert str(ve) == "Invalid coordonate x!\n"

    try:
        p.set_color('turquoise')
        assert False
    except ValueError as ve:
        assert str(ve) == "Invalid color!\n"

    assert str(p) == "Point (3,2) of color red"


def test_add_point():
    points = PointRepository()
    points.add_point(MyPoint(1, 2, 'red'))
    assert len(points.get_all()) == 1
    try:
        points.add_point(MyPoint(1, 2, 'red'))
        assert False
    except ValueError as ve:
        assert str(ve) == "Point already exists!\n"


def test_get_all():
    points = PointRepository()
    point = MyPoint(1, 2, 'red')
    points.add_point(point)
    assert len(points.get_all()) == 1
    assert points.get_all() == [point]


def test_get_point():
    points = PointRepository()
    point1 = MyPoint(1, 2, 'red')
    point2 = MyPoint(2, 3, 'blue')
    points.add_point(point1)
    points.add_point(point2)
    assert points.get_point(0) == point1
    assert points.get_point(1) == point2
    try:
        points.get_point(2)
        assert False
    except ValueError as ve:
        assert str(ve) == "Invalid index!\n"


def test_get_points_of_color():
    points = PointRepository()
    point1 = MyPoint(1, 2, 'red')
    point2 = MyPoint(2, 3, 'blue')
    point3 = MyPoint(3, 4, 'green')
    point4 = MyPoint(4, 5, 'red')
    points.add_point(point1)
    points.add_point(point2)
    points.add_point(point3)
    points.add_point(point4)
    assert points.get_points_of_color('red') == [point1, point4]
    assert points.get_points_of_color('blue') == [point2]
    assert points.get_points_of_color('yellow') == []


def test_get_points_in_square():
    points = PointRepository()
    point1 = MyPoint(1, 2, 'red')
    point2 = MyPoint(2, 3, 'blue')
    points.add_point(point1)
    points.add_point(point2)
    assert points.get_points_in_square(0, 0, 1) == []
    assert points.get_points_in_square(0, 2, 2) == [point1]
    assert points.get_points_in_square(0, 3, 3) == [point1, point2]


def test_distance():
    points = PointRepository()
    p1 = MyPoint(0, 1, 'red')
    p2 = MyPoint(0, 2, 'blue')
    assert points.distance(p1, p2) == 1.0


def test_minimum_distance():
    points = PointRepository()
    point1 = MyPoint(0, 1, 'red')
    point2 = MyPoint(0, 2, 'blue')
    point3 = MyPoint(0, 3, 'green')
    points.add_point(point1)
    points.add_point(point2)
    points.add_point(point3)
    assert points.minimum_distance() == 1


def test_update_point():
    points = PointRepository()
    point1 = MyPoint(1, 2, 'red')
    points.add_point(point1)
    new_point = MyPoint(1, 2, 'blue')
    points.update_point(0, new_point)
    assert points.get_point(0) == new_point


def test_delete_point():
    points = PointRepository()
    points.add_point(MyPoint(1, 2, 'red'))
    points.delete_point(0)
    assert len(points.get_all()) == 0
    assert points.get_all() == []


def test_delete_points_in_square():
    points = PointRepository()
    point1 = MyPoint(1, 2, 'red')
    point2 = MyPoint(2, 3, 'blue')
    point3 = MyPoint(3, 4, 'green')
    point4 = MyPoint(4, 5, 'red')
    points.add_point(point1)
    points.add_point(point2)
    points.add_point(point3)
    points.add_point(point4)
    points.delete_points_in_square(0, 3, 2)
    assert len(points.get_all()) == 2
    assert points.get_all() == [point3, point4]


def test_get_points_in_circle():
    points = PointRepository()
    point1 = MyPoint(1, 2, 'red')
    point2 = MyPoint(2, 3, 'blue')
    points.add_point(point1)
    points.add_point(point2)
    assert points.get_points_in_circle(0, 0, 1) == []
    assert points.get_points_in_circle(0, 0, 3) == [point1]


def test_get_points_in_rectangle():
    points = PointRepository()
    point1 = MyPoint(1, 2, 'red')
    point2 = MyPoint(2, 3, 'blue')
    points.add_point(point1)
    points.add_point(point2)
    assert points.get_points_in_rectangle(0, 0, 1, 1) == []
    assert points.get_points_in_rectangle(0, 2, 2, 2) == [point1]
    assert points.get_points_in_rectangle(0, 3, 3, 3) == [point1, point2]


def test_maximum_distance():
    points = PointRepository()
    point1 = MyPoint(0, 1, 'red')
    point2 = MyPoint(0, 3, 'green')
    point3 = MyPoint(0, 2, 'blue')
    points.add_point(point1)
    points.add_point(point2)
    points.add_point(point3)
    assert points.minimum_distance() == 1


def test_shift_points_on_x_axis():
    points = PointRepository()
    point1 = MyPoint(1, 2, 'red')
    point2 = MyPoint(2, 3, 'blue')
    points.add_point(point1)
    points.add_point(point2)
    points.shift_points_on_x_axis(1)
    assert point1.get_x() == 2
    assert point2.get_x() == 3


def test_delete_points_in_circle():
    points = PointRepository()
    point1 = MyPoint(1, 2, 'red')
    point2 = MyPoint(2, 3, 'blue')
    points.add_point(point1)
    points.add_point(point2)
    points.delete_points_in_circle(0, 0, 3)
    assert len(points.get_all()) == 1
    assert points.get_all() == [point2]


def run_tests():
    test_point()
    test_add_point()
    test_get_all()
    test_get_point()
    test_get_points_of_color()
    test_get_points_in_square()
    test_distance()
    test_minimum_distance()
    test_update_point()
    test_delete_point()
    test_delete_points_in_square()
    test_get_points_in_circle()
    test_get_points_in_rectangle()
    test_maximum_distance()
    test_shift_points_on_x_axis()
    test_delete_points_in_circle()
