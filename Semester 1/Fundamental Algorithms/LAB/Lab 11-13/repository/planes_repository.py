from domain.plane import Plane


class PlanesRepository:
    def __init__(self, initial_values=None):
        if initial_values is None:
            initial_values = []
        self.__planes = []
        if initial_values is not None:
            for value in initial_values:
                if isinstance(value, Plane):
                    self.__planes.append(value)

    def check_if_plane_exists(self, plane):
        for p in self.__planes:
            if p.get_name() == plane.get_name():
                return True
        return False

    def add_plane(self, plane):
        if not isinstance(plane, Plane):
            raise ValueError("The object is not a plane!\n")
        if self.check_if_plane_exists(plane):
            raise ValueError("Plane already in repository!\n")
        self.__planes.append(plane)

    def get_all(self):
        if len(self.__planes) == 0:
            raise ValueError("Empty repository!\n")
        return self.__planes

    def get_plane_by_name(self, name):
        for plane in self.__planes:
            if plane.get_name() == name:
                return plane
        raise ValueError("There is no plane with this name!\n")

    def get_planes_by_destination(self, destination):
        list_of_planes = []
        for plane in self.__planes:
            if plane.get_destination() == destination:
                list_of_planes.append(plane)
        if len(list_of_planes) == 0:
            raise ValueError("No plane with this destination!\n")
        return list_of_planes

    def get_planes_by_number_of_seats(self, number_of_seats):
        list_of_planes = []
        for plane in self.__planes:
            if plane.get_number_of_seats() == number_of_seats:
                list_of_planes.append(plane)
        if len(list_of_planes) == 0:
            raise ValueError("No plane with this number of seats!\n")
        return list_of_planes

    def update_plane(self, plane, up_plane):
        if not isinstance(plane, Plane):
            raise ValueError("The object is not a plane!\n")
        if not isinstance(up_plane, Plane):
            raise ValueError("The object is not a plane!\n")
        if self.check_if_plane_exists(plane):
            raise ValueError("Plane to be updated not in repository!\n")
        if self.check_if_plane_exists(up_plane):
            raise ValueError("Updated plane already in repository!\n")
        plane.set_name(up_plane.get_name())
        plane.set_airline_company(up_plane.get_airline_company())
        plane.set_number_of_seats(up_plane.get_number_of_seats())
        plane.set_destination(up_plane.get_destination())

    def remove_plane(self, plane):
        if plane not in self.__planes:
            raise ValueError("Plane not in repository!\n")
        self.__planes.remove(plane)

    def remove_plane_by_name(self, name):
        for plane in self.__planes:
            if plane.get_name() == name:
                self.__planes.remove(plane)
                return
        raise ValueError("Plane not in repository!\n")

    def __len__(self):
        return len(self.__planes)

    def __str__(self):
        repo_str = ""
        all_planes = self.get_all()
        for plane in all_planes:
            repo_str += str(plane) + "\n"
        if repo_str == "":
            repo_str = "No planes!\n"
        return repo_str
